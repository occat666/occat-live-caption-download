"""Candidate public control: restore only pinned, reviewed third-party inputs.

Not wired into a workflow. Requires that workflow's repository GITHUB_TOKEN,
never an account token, source deploy key or diagnostics decryption key.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import os
import platform
import re
import stat
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import zipfile

RECIPES = (
    'tools/build_macos_release.py', 'tools/build_lgpl_native.py',
    'tools/build_sherpa_asr.py', 'requirements-macos-build.txt',
)
REPORTS = (
    'ffmpeg-build.json', 'ffmpeg-license-runtime.json', 'sherpa-build.json',
    'python-asr-init.patch', 'native-toolchain.json', 'native-wheel-smoke.json',
)
REPOSITORY = 'occat666/occat-live-caption-download'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def inventory(archive):
    """Reject duplicate, traversing, directory and symlink ZIP entries."""
    entries = {}
    for item in archive.infolist():
        name = item.filename
        if (not name or name in entries or '\\' in name or ':' in name
                or name.startswith('/') or any(part in ('', '.', '..') for part in name.split('/'))
                or item.is_dir() or stat.S_ISLNK(item.external_attr >> 16)):
            raise RuntimeError('Invalid native-cache ZIP member')
        entries[name] = item
    if sum(item.file_size for item in entries.values()) > 256 * 1024 * 1024:
        raise RuntimeError('Native-cache ZIP exceeds its reviewed size bound')
    return entries


def validate_cache(cache, source, arch):
    """Validate native-only closure before writing into the private checkout."""
    source = Path(source).resolve()
    if arch not in ('arm64', 'x86_64'):
        raise RuntimeError('Invalid native-cache architecture')
    expected_inputs = {name: file_digest(source / name) for name in RECIPES}
    with zipfile.ZipFile(cache) as archive:
        entries = inventory(archive)
        manifest = json.loads(archive.read('manifest.json'))
        if (manifest.get('schema_version') != 1 or manifest.get('arch') != arch
                or manifest.get('minimum_macos') != '14.0' or manifest.get('python_abi') != 'cp313'
                or manifest.get('inputs') != expected_inputs):
            raise RuntimeError('Native-cache source/ABI/architecture mismatch')
        native_names = (
            f'av-18.1.0-cp311-abi3-macosx_14_0_{arch}.whl',
            f'sherpa_onnx-1.13.8+asr.1-cp313-cp313-macosx_14_0_{arch}.whl',
            f'CorrespondingSources-macOS-{arch}.zip',
        )
        allowed = {'native/' + name for name in (*native_names, 'native-complete.json')}
        allowed |= {'reports/' + name for name in REPORTS}
        if set(entries) != allowed | {'manifest.json'} or set(manifest['files']) != allowed:
            raise RuntimeError('Native-cache contains unapproved files')
        payload = {}
        for name in sorted(allowed):
            record = manifest['files'][name]
            content = archive.read(name)
            if len(content) != record['bytes'] or digest(content) != record['sha256']:
                raise RuntimeError('Native-cache file hash mismatch')
            payload[name] = content
    completion = json.loads(payload['native/native-complete.json'])
    if (completion.get('schema_version') != 2 or completion.get('arch') != arch
            or completion.get('minimum_macos') != '14.0' or completion.get('inputs') != expected_inputs
            or not completion.get('python', '').startswith('3.13.')
            or completion.get('native_smoke', {}).get('passed') is not True
            or completion['native_smoke'] != json.loads(payload['reports/native-wheel-smoke.json'])):
        raise RuntimeError('Invalid native completion evidence')
    records = completion['files']
    if len(records) != 3 or {item['file'] for item in records} != set(native_names):
        raise RuntimeError('Unexpected native completion file set')
    for item in records:
        content = payload['native/' + item['file']]
        if len(content) != item['bytes'] or digest(content) != item['sha256']:
            raise RuntimeError('Native completion file hash mismatch')
    # The corresponding-source ZIP is already covered by the trusted outer
    # hash and prior strict run proof. Recheck recipes/license and native
    # reports against this checkout instead of trusting a changed cache record.
    import io
    with zipfile.ZipFile(io.BytesIO(payload['native/' + native_names[2]])) as native_source:
        source_entries = inventory(native_source)
        for name in (*RECIPES, 'LICENSE'):
            if native_source.read(name) != (source / name).read_bytes():
                raise RuntimeError('Cached native recipe/license changed')
        for name in REPORTS:
            if native_source.read('records/' + name) != payload['reports/' + name]:
                raise RuntimeError('Cached native report/source closure mismatch')
        if any(not (name.startswith('sources/') or name.startswith('records/')
                    or name in (*RECIPES, 'LICENSE', 'README.txt')) for name in source_entries):
            raise RuntimeError('Unexpected corresponding-source ZIP namespace')
    for name, namespace in ((native_names[0], 'av'), (native_names[1], 'sherpa_onnx')):
        with zipfile.ZipFile(io.BytesIO(payload['native/' + name])) as wheel:
            names = inventory(wheel)
            roots = {path.split('/')[0] for path in names}
            dist_info = ('av-18.1.0.dist-info' if namespace == 'av'
                         else 'sherpa_onnx-1.13.8+asr.1.dist-info')
            if roots != {namespace, dist_info}:
                raise RuntimeError('Unexpected native wheel namespace')
    return manifest, payload


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        return None


def download_asset(record, token, destination):
    asset_id = record['asset_id']
    if type(asset_id) is not int or asset_id <= 0 or not re.fullmatch('[0-9a-f]{64}', record['sha256']):
        raise RuntimeError('Invalid pinned native asset')
    expected_size = record['bytes']
    if type(expected_size) is not int or not 0 < expected_size < 128 * 1024 * 1024:
        raise RuntimeError('Invalid pinned native asset size')
    request = urllib.request.Request(
        f'https://api.github.com/repos/{REPOSITORY}/releases/assets/{asset_id}',
        headers={'Authorization': 'Bearer ' + token, 'Accept': 'application/octet-stream',
                 'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'occat-reviewed-native-cache'})
    try:
        response = urllib.request.build_opener(NoRedirect).open(request, timeout=60)
    except urllib.error.HTTPError as error:
        if error.code not in (301, 302, 303, 307, 308):
            error.close()
            raise RuntimeError('Native asset API request failed') from None
        location = error.headers['Location']
        error.close()
        target = urllib.parse.urlparse(location)
        if (target.scheme != 'https' or not target.hostname
                or not target.hostname.endswith('.githubusercontent.com')
                or target.username or target.password or target.port not in (None, 443)):
            raise RuntimeError('Unapproved native asset redirect') from None
        # Crucially do not forward the repository token to the signed asset URL.
        response = urllib.request.urlopen(location, timeout=60)
    del token, request
    count, checksum = 0, hashlib.sha256()
    with response, Path(destination).open('wb') as output:
        while data := response.read(1024 * 1024):
            count += len(data)
            if count > expected_size:
                raise RuntimeError('Native asset exceeds its pinned size')
            checksum.update(data)
            output.write(data)
    if count != expected_size or checksum.hexdigest() != record['sha256']:
        raise RuntimeError('Native asset hash/size mismatch')


def restore(source, arch, config):
    source = Path(source).resolve()
    if sys.platform != 'darwin' or platform.machine() != arch or sys.version_info[:2] != (3, 13):
        raise RuntimeError('Native cache requires matching macOS/architecture/Python 3.13')
    if tuple(int(x) for x in platform.mac_ver()[0].split('.')[:2]) < (14, 0):
        raise RuntimeError('Native cache requires macOS 14 or later')
    current_commit = os.environ.get('OCCAT_SOURCE_COMMIT', '')
    if not re.fullmatch('[0-9a-f]{40}', current_commit):
        raise RuntimeError('Missing pinned private source revision')
    record = json.loads(Path(config).read_text(encoding='utf-8'))['architectures'][arch]
    token = os.environ.pop('OCCAT_NATIVE_CACHE_TOKEN', '')
    if not token:
        raise RuntimeError('Missing short-lived repository asset token')
    with tempfile.TemporaryDirectory(prefix='occat-native-cache-') as temporary:
        archive = Path(temporary) / 'native.zip'
        download_asset(record, token, archive)
        del token
        manifest, payload = validate_cache(archive, source, arch)
        if (manifest['source_run_id'] != record['source_run_id']
                or manifest['source_commit'] != record['source_commit']):
            raise RuntimeError('Native cache provenance mismatch')
        output = source / '_deliver/macos' / arch
        for name, data in payload.items():
            target = output / name
            if target.exists() or target.is_symlink():
                raise RuntimeError('Native restore target is already populated')
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        del payload
    sys.path.insert(0, str(source))
    spec = importlib.util.spec_from_file_location('reviewed_macos_builder', source / RECIPES[0])
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    build = builder.Build(arch, 3)
    if not build.native_ready():
        raise RuntimeError('Restored native cache was rejected by current builder')
    completion = json.loads((build.native / 'native-complete.json').read_text(encoding='utf-8'))
    wheels = [build.native / item['file'] for item in completion['files'] if item['file'].endswith('.whl')]
    fresh = build.native_wheel_smoke(wheels)
    if fresh != completion['native_smoke'] or fresh.get('passed') is not True:
        raise RuntimeError('Fresh native wheel verification differs from reviewed evidence')
    proof = dict(passed=True, source_commit=current_commit, architecture=arch,
                 source_run_id=manifest['source_run_id'], native_source_commit=manifest['source_commit'],
                 cache_sha256=record['sha256'], inputs=completion['inputs'],
                 python=sys.version, macos=platform.mac_ver()[0],
                 fresh_isolated_native_wheel_smoke=fresh)
    builder.write_json(build.reports / 'native-cache-revalidation.json', proof)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('arch', choices=('arm64', 'x86_64'))
    parser.add_argument('config')
    arguments = parser.parse_args()
    restore(arguments.source, arguments.arch, arguments.config)

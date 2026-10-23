"""Public orchestration only. Private source and diagnostic output stay off public logs."""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile

ROOT = Path.cwd()
CONTROL = ROOT / '.github/macos'
ARCH = os.environ['OCCAT_ARCH']
COMMIT = os.environ['OCCAT_SOURCE_COMMIT']
assert ARCH in ('arm64', 'x86_64') and re.fullmatch('[0-9a-f]{40}', COMMIT)
# GPG's Unix-domain socket must fit macOS's short sockaddr_un path limit.
SOURCE = Path('/tmp') / ('occat-source-' + ARCH)
LOCAL = Path(os.environ['RUNNER_TEMP']) / ('occat-private-' + ARCH)
LOCAL.mkdir(exist_ok=True)

def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')

def run(args, label, *, cwd=SOURCE, env=None, timeout=7200):
    with (LOCAL / (label + '.log')).open('w', encoding='utf-8') as stream:
        result = subprocess.run([str(a) for a in args], cwd=cwd, env=env,
            stdout=stream, stderr=subprocess.STDOUT, timeout=timeout)
    if result.returncode:
        raise RuntimeError(label)

def checkout():
    key = os.environ.pop('OCCAT_SOURCE_SSH_KEY', '')
    if not key:
        raise RuntimeError('Missing read-only source deploy key')
    with tempfile.TemporaryDirectory(prefix='occat-read-key-') as temp:
        identity = Path(temp) / 'identity'
        identity.write_text(key.replace('\r\n','\n').strip() + '\n', encoding='utf-8')
        identity.chmod(0o600)
        del key
        environment = dict(os.environ)
        environment['GIT_SSH_COMMAND'] = (
            'ssh -i ' + str(identity) + ' -o IdentitiesOnly=yes -o BatchMode=yes '
            '-o StrictHostKeyChecking=yes -o UserKnownHostsFile=' + str(CONTROL / 'github_known_hosts'))
        SOURCE.mkdir()
        try:
            run(['git', 'init', '-q'], 'git-init', env=environment)
            run(['git', 'fetch', '--depth=1', 'git@github.com:occat666/occat-live-caption.git', COMMIT],
                'source-fetch', env=environment, timeout=240)
            run(['git', 'checkout', '--detach', 'FETCH_HEAD'], 'source-checkout', env=environment)
            actual = subprocess.check_output(['git','rev-parse','HEAD'],cwd=SOURCE,text=True).strip()
            if actual != COMMIT:
                raise RuntimeError('Source revision mismatch')
            inventory = subprocess.check_output(['git','ls-files','-z'],cwd=SOURCE).decode().split('\0')
            files = {name:hashlib.sha256((SOURCE / name).read_bytes()).hexdigest()
                     for name in inventory if name}
            write(LOCAL / 'source-checkout.json', {'commit': actual, 'files': files,
                'workflow_commit':os.environ['GITHUB_SHA'], 'run_id':os.environ['GITHUB_RUN_ID']})
        finally:
            shutil.rmtree(SOURCE / '.git', ignore_errors=True)

def tests():
    run([sys.executable,'-m','pip','install','--disable-pip-version-check','--no-deps',
         'packaging==26.3'], 'install-packaging')
    run([sys.executable,'tests/test_macos_build.py','-v'],'build-tests')
    run([sys.executable,'-m','unittest','discover','-s','tests','-p','test_mac_permission.py','-v'],
        'permission-tests')

def builder(stage):
    run([sys.executable,'tools/build_macos_release.py','--stage',stage,'--arch',ARCH,'--jobs','3'],
        'builder-' + stage)

def inference():
    executable = SOURCE / '_dev/macos' / ARCH / 'dist/OCCATLiveCaption.app/Contents/MacOS/OCCATLiveCaption'
    report = SOURCE / '_deliver/macos' / ARCH / 'reports/frozen-model-smoke.json'
    with tempfile.TemporaryDirectory(prefix='occat-model-test-') as directory:
        run([executable,'--macos-model-smoke',report,Path(directory) / 'tiny.en'],
            'frozen-model-smoke',timeout=600)

def package():
    # One encrypted envelope carries diagnostics and candidate files for local review.
    # Nothing from the source tree, .git, venv or PyInstaller work is archived.
    outgoing = ROOT / 'outgoing'
    outgoing.mkdir(exist_ok=True)
    archive = LOCAL / 'review.tar'
    with tarfile.open(archive,'w') as tar:
        base = SOURCE / '_deliver/macos' / ARCH
        for folder, target in ((base / 'reports', ARCH + '-diagnostics/reports'),
                               (SOURCE / '_dev/macos' / ARCH / 'logs', ARCH + '-diagnostics/logs'),
                               (LOCAL, ARCH + '-diagnostics/control'),
                               (base / 'artifacts', ARCH + '-candidates/artifacts'),
                               (base / 'native', ARCH + '-candidates/native')):
            if not folder.is_dir():
                continue
            for path in sorted(folder.rglob('*')):
                if path == archive or not path.is_file() or path.is_symlink():
                    continue
                if folder == LOCAL and path.suffix not in ('.json','.log'):
                    continue
                if folder.name == 'native' and path.suffix not in ('.whl','.zip','.json'):
                    continue
                tar.add(path, arcname=target + '/' + path.relative_to(folder).as_posix(),recursive=False)
    encrypted = outgoing / ('macos-' + ARCH + '-review.occenc')
    run(['node',CONTROL / 'envelope.cjs','encrypt',CONTROL / 'diagnostics-public.pem',archive,encrypted],
        'encrypt-diagnostics',cwd=ROOT,timeout=300)
    archive.unlink()
    write(outgoing / ('macos-' + ARCH + '-manifest.json'), {
        'architecture':ARCH,'source_commit':COMMIT,'workflow_commit':os.environ['GITHUB_SHA'],
        'run_id':os.environ['GITHUB_RUN_ID'],'file':encrypted.name,
        'bytes':encrypted.stat().st_size,'sha256':hashlib.file_digest(encrypted.open('rb'),'sha256').hexdigest(),
        'status':json.loads((LOCAL / 'status.json').read_text())})

def main():
    step = sys.argv[1]
    choices = {'checkout':checkout,'tests':tests,'probe':lambda:builder('probe'),
        'native':lambda:builder('native'),'bundle':lambda:builder('bundle'),
        'inference':inference,'package':package}
    try:
        choices[step]()
    except Exception:
        # Never print exception details from private commands on the public runner.
        import traceback
        (LOCAL / ('control-' + step + '.log')).write_text(traceback.format_exc(),encoding='utf-8')
        write(LOCAL / 'status.json', {'last_step':step,'passed':False})
        print('Mac verification stage failed: ' + step, flush=True)
        return 1
    if step != 'package':
        write(LOCAL / 'status.json', {'last_step':step,'passed':True})
    print('Mac verification stage completed: ' + step, flush=True)
    return 0

if __name__ == '__main__':
    sys.exit(main())

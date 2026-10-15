# Maomao Local Live Captions / 猫猫本地实时字幕

[简体中文](README.md) · Author **OCCAT**

Local Windows captions from system audio or a microphone, with optional English/Japanese/Korean to Chinese translation. Reading assistance for videos, courses, games, streams and personal meetings.

## Download and install

**[Open the RC15 public preview](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.0-rc.15)**. **0.1.0 RC15 is published as a public preview.**

Download **one installer**; there is no need to download the whole repository or every archive:

| File | Purpose |
| --- | --- |
| [OCCAT-Live-Caption-0.1.0-windows-x64-setup.exe](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.0-rc.15/OCCAT-Live-Caption-0.1.0-windows-x64-setup.exe) | One installer: 中文 / English / 日本語 / 한국어 |
| `SHA256SUMS.txt` | Optional download integrity verification |
| Corresponding-source and Third-Party-Notices ZIPs | Library sources and notices; not required for ordinary installation |

1. Use **Windows 10/11 x64** with Microsoft Visual C++ x64 Runtime **14.44.35211 or newer**. If missing or outdated, setup asks permission to download it directly from Microsoft, verifies Microsoft's signature, and opens its installer. Confirm the Microsoft license and Windows administrator prompt; caption setup continues after a successful runtime check. Internet access is needed for this download. Setup never restarts Windows automatically; if required, save your work, restart, and rerun caption setup.
2. Download the single EXE, verify its origin and SHA-256, choose Chinese, English, Japanese or Korean, then follow the setup wizard. The installer does not have a commercial code-signing certificate.
3. Launch the application, select the actual output device or microphone, wait for the bundled **Whisper base** model, and start captions. Initial recognition needs no model download.
4. Download/import the compatible **M2M100** model before enabling real-time translation. Leave translation off for original captions only.
5. Customize fonts, smooth outlines, soft shadows, position and backdrop. Interface language and recognition language are separate; the interface can be changed between 中文, English, 日本語 and 한국어 after installation.

**RC13 users must manually download and run the unified EXE for the first upgrade**; the old updater does not recognize the unified asset name. RC14 and RC13 remain available in older Releases. Preview builds are not delivered by the stable latest endpoint. The in-app version remains 0.1.0; use the Release tag to identify candidates. Japanese/Korean setup displays the reviewed original English component terms.

Installation is per user. Existing settings take priority. User data lives under `%LOCALAPPDATA%/OCCATLiveCaption` and is retained on uninstall.

## Features and validation

Model-aware Chinese, English, Japanese, Korean and automatic recognition; optional translation and original text; local model/font import; caption typography, continuous alpha edges, backdrop, positioning and click-through; dark/day/system/custom themes; appearance versions, reset, tray, pause, preview and hide controls.

Input and dropdown controls no longer show lingering white focus borders after mouse editing or while scrolling past; keyboard navigation retains focus feedback.

Settings pages use short smooth wheel movement and direct touchpad pixel input. Top/bottom travel is bounded; reversing, dragging the scrollbar or switching pages takes control immediately.

The update button checks published stable releases. GitHub's latest-release endpoint excludes previews; obtain preview builds manually from Releases.

RC15 passed 56 related tests covering runtime decisions, signature rejection, cancellation and restart handling. The same installer passed isolated installation, offline startup and uninstall checks for Chinese, English, Japanese and Korean on the development computer, including bundled base offline CPU inference and interface switching. **This candidate has not been tested on a fresh Windows system without the runtime and remains a prerelease.** All GPU, monitor and operating-system combinations are not certified.

Recognition and translation run locally. Model downloads and explicit update checks need network access. **Caption text is saved locally by default**; disable logging in advanced settings if preferred. Uninstall retains user data. Important captions need manual verification; obtain permission when capturing others' speech.

## Licenses and publication scope

OCCAT's own code and these documents use [MIT](LICENSE), copyright **OCCAT**. **The development source repository remains private. This is a public binary-download repository, not a claim that all application source has been published.**

The complete installer is not MIT-only. Original font/model/library/vendor licenses remain applicable. Same-version releases provide required corresponding sources, build resources and notices. See [third-party notices](THIRD_PARTY_NOTICE_PUBLIC.md) and the [library modification/replacement guide](LIBRARY_REPLACEMENT.en.md). Rights to modify, replace and debug LGPL libraries remain intact.

Report problems in [Issues](https://github.com/occat666/occat-live-caption-download/issues). Remove private paths, account identifiers, recordings and conversations before submitting evidence.

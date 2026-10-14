# Maomao Local Live Captions / 猫猫本地实时字幕

[简体中文](README.md) · Author **OCCAT**

Local Windows captions from system audio or a microphone, with optional English/Japanese/Korean to Chinese translation. Reading assistance for videos, courses, games, streams and personal meetings.

## Download and install

**[Open Releases](https://github.com/occat666/occat-live-caption-download/releases)**. The prepared release is **0.1.0 RC13, a public preview**. Availability is determined by the actual published release and its assets.

Download **one installer**; there is no need to download the whole repository or every archive:

| File | Purpose |
| --- | --- |
| `OCCAT-Live-Caption-0.1.0-windows-x64-setup-en.exe` | English installer |
| `OCCAT-Live-Caption-0.1.0-windows-x64-setup-zh-CN.exe` | Simplified Chinese installer |
| `SHA256SUMS.txt` | Optional download integrity verification |
| Corresponding-source and Third-Party-Notices ZIPs | Library sources and notices; not required for ordinary installation |

1. Use **Windows 10/11 x64** with Microsoft Visual C++ x64 Runtime **14.44.35211 or newer**. If missing, the installer directs you to [Microsoft's official instructions](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist/). Install that prerequisite and rerun the caption installer.
2. Download either installer, verify its origin and SHA-256, then follow the setup wizard. These installers do not have a commercial code-signing certificate.
3. Launch the application, select the actual output device or microphone, wait for the bundled **Whisper base** model, and start captions. Initial recognition needs no model download.
4. Download/import the compatible **M2M100** model before enabling real-time translation. Leave translation off for original captions only.
5. Customize fonts, smooth outlines, soft shadows, position and backdrop. Interface language and recognition language are separate; the interface can be changed after installation.

Installation is per user. Existing settings take priority. User data lives under `%LOCALAPPDATA%/OCCATLiveCaption` and is retained on uninstall.

## Features and validation

Model-aware Chinese, English, Japanese, Korean and automatic recognition; optional translation and original text; local model/font import; caption typography, continuous alpha edges, backdrop, positioning and click-through; dark/day/system/custom themes; appearance versions, reset, tray, pause, preview and hide controls.

Settings pages use short smooth wheel movement and direct touchpad pixel input. Top/bottom travel is bounded; reversing, dragging the scrollbar or switching pages takes control immediately.

The update button checks published stable releases. GitHub's latest-release endpoint excludes previews; obtain preview builds manually from Releases.

RC13 passed Chinese/English installation, offline startup and uninstall checks on the development computer, plus rendering, opacity, dragging, hiding, size and scaling checks. Of 123 related tests, 122 passed and one secondary-monitor test was skipped. **This build has not completed a fresh independent Windows acceptance run and remains a prerelease candidate.** All GPU, monitor and operating-system combinations are not certified.

Recognition and translation run locally. Model downloads and explicit update checks need network access. **Caption text is saved locally by default**; disable logging in advanced settings if preferred. Uninstall retains user data. Important captions need manual verification; obtain permission when capturing others' speech.

## Licenses and publication scope

OCCAT's own code and these documents use [MIT](LICENSE), copyright **OCCAT**. **The development source repository remains private. This is a public binary-download repository, not a claim that all application source has been published.**

The complete installer is not MIT-only. Original font/model/library/vendor licenses remain applicable. Same-version releases provide required corresponding sources, build resources and notices. See [third-party notices](THIRD_PARTY_NOTICE_PUBLIC.md) and the [library modification/replacement guide](LIBRARY_REPLACEMENT.en.md). Rights to modify, replace and debug LGPL libraries remain intact.

Report problems in [Issues](https://github.com/occat666/occat-live-caption-download/issues). Remove private paths, account identifiers, recordings and conversations before submitting evidence.


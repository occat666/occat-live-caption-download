# 猫猫本地实时字幕 / Maomao Local Live Captions

[简体中文](README.md) · [繁體中文](README.zh-TW.md) · **English** · [日本語](README.ja.md) · [한국어](README.ko.md)

A local live caption tool for system audio or microphone speech, with floating captions, a transcript window, and offline translation.

## Download

Current release: [0.1.29 public preview](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.29). Choose either Windows package, or the Mac package for the appropriate processor.

| Edition | Download |
| --- | --- |
| Windows installer | [OCCAT-Live-Caption-0.1.29-windows-x64-setup.exe](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.29/OCCAT-Live-Caption-0.1.29-windows-x64-setup.exe) |
| Windows portable | [OCCAT-Live-Caption-0.1.29-windows-x64-portable.zip](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.29/OCCAT-Live-Caption-0.1.29-windows-x64-portable.zip) |
| Mac · Apple silicon | [OCCATLiveCaption-0.1.29-macOS-arm64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.29/OCCATLiveCaption-0.1.29-macOS-arm64.dmg) |
| Mac · Intel | [OCCATLiveCaption-0.1.29-macOS-x86_64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.29/OCCATLiveCaption-0.1.29-macOS-x86_64.dmg) |

[Windows SHA-256](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.29/SHA256SUMS.txt) · [macOS SHA-256](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.29/SHA256SUMS-macOS.txt) · [Releases](https://github.com/occat666/occat-live-caption-download/releases)

## Features

- Floating captions or a live transcript with scrollback and copying.
- Chinese (Simplified/Traditional), English, Japanese, and Korean output and translation in either direction. Recognition languages depend on the selected model.
- Separate fonts, colors, outlines, shadows, and backgrounds for original and translated text.
- Recognition and translation run locally. Model downloads and update checks use the network; fully cached models work offline.

## Getting started

1. On Windows, run the installer or fully extract the portable ZIP and open `OCCATLiveCaption.exe`. On Mac, drag the app from the DMG into Applications.
2. Select the active audio device or microphone and download a recognition model. The default Whisper large-v3-turbo is about 1.6 GB; other models are available.
3. For translation, download or import an M2M100 model, choose the target language, and enable translation.

**Windows:** Windows 10/11 x64 and Visual C++ x64 Runtime 14.44.35211 or newer are required. The installer checks the runtime and guides installation.

**macOS:** macOS 14 or newer is required. The preview uses CPU inference and is not Apple-notarized. System audio capture requires a virtual input such as BlackHole. See [Mac audio setup](docs/macos-audio.md).

## Documentation and feedback

[User guide (Chinese)](docs/USER_GUIDE.zh-CN.md) · [Release notes and older versions](https://github.com/occat666/occat-live-caption-download/releases) · [Report an issue](https://github.com/occat666/occat-live-caption-download/issues)

Caption text is saved locally by default; this can be disabled in caption settings. Recognition and translation can be inaccurate; verify important content.

Author: OCCAT. This repository distributes downloads and related materials; application development source remains private. Original repository content uses [MIT](LICENSE). Bundled components and fonts retain their own licenses; see [third-party notices](THIRD_PARTY_NOTICE_PUBLIC.md) and [library replacement instructions](LIBRARY_REPLACEMENT.en.md).

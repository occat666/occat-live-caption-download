# OCCAT Live Caption / OCCAT 实时字幕

[简体中文](README.md)

A Windows desktop application for local captions from system audio or a microphone, with optional English/Japanese/Korean to Chinese translation. It provides reading assistance for videos, courses, games, streams and personal meetings.

**Release preparation only. The installation candidate is GATED. No public Release or approved installer is available yet. OCCAT has confirmed the added CUDA distribution scope, and the current candidate's notices, corresponding sources and actual assets have been reviewed. Independent Windows installation and key-function acceptance remain pending.**

This is the public download page for OCCAT Live Caption, separate from the private development repository. Development history, private configuration, audio and caption logs remain private. Approved releases will include installers, checksums, reviewed source and applicable license materials in this repository's GitHub Releases.

## Features

- Local recognition with a bundled multilingual Whisper base model. Chinese, English, Japanese, Korean and automatic detection are offered according to the selected model's capabilities.
- Optional real-time translation, disabled by default. Download or import a compatible M2M100 model to translate English, Japanese or Korean to Chinese; original text can also be displayed.
- Custom fonts, weight, size, color, position and caption background padding, opacity and corner radius. Import supported model formats and TTF/OTF/TTC fonts.
- Switch between Simplified Chinese and English interfaces. Interface and recognition languages are configured separately.

## Installation after release approval

Use Windows 10/11 x64. The planned installer names are:

| Asset | First-run interface |
| --- | --- |
| `OCCAT-Live-Caption-0.1.0-windows-x64-setup-zh-CN.exe` | Simplified Chinese |
| `OCCAT-Live-Caption-0.1.0-windows-x64-setup-en.exe` | English |

These assets have not been published. Both installers contain the same application; existing preferences take priority, and the interface language can be changed later.

1. Install Microsoft Visual C++ x64 Runtime **14.44.35211 or newer** if required. The caption installer stops when it is missing and offers to open [Microsoft's official instructions](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist/). Install the runtime, then run the caption installer again. Microsoft runtime files are not bundled.
2. Download the desired installer from the approved GitHub Release, check it against the same release's `SHA256SUMS.txt`, then run it.
3. Start the application, select the device actually playing sound or a microphone, wait for the model and start captions.
4. Download or import the compatible translation model before enabling real-time translation. Leave it off for original captions only.

Computers that already meet the runtime prerequisite can run the caption installer directly. CPU speed depends on hardware and the model. GPU support will follow the validation scope listed in the final release notes.

## Privacy and limitations

Recognition and translation run locally. The current application has no audio upload interface; model and dependency downloads require internet access. **Caption text is saved locally by default**; disable saving in advanced settings if preferred. Uninstallation retains user data. User-selected backgrounds and imported models/fonts remain local.

Automatic captions and translation can be inaccurate. Check important content manually and obtain the necessary permission before capturing someone else's speech. This application provides assistance rather than professional accessibility services or an authoritative transcript.

## Licenses and source

OCCAT's own code and these documents use [MIT](LICENSE), copyright OCCAT. Approved binary releases will include the reviewed project source ZIP, original third-party licenses and notices, and required corresponding-source attachments for Qt, FFmpeg/PyAV, Sherpa ASR and other applicable components. The reviewed project source excludes the original development Git history and private configuration.

The complete installer is not labeled MIT-only. Model weights, Source Han Sans fonts (SIL OFL 1.1), LGPL Qt/FFmpeg libraries, Intel/NVIDIA runtime materials and other components retain their own terms. MIT does not replace those terms or recipients' rights to modify, replace and debug LGPL libraries. Consult the complete notices and scoped component terms supplied with the approved release.

The public download repository has been created. Installers and the official version have not been published yet; downloads will appear in GitHub Releases after validation.

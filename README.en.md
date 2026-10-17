# Maomao Local Live Captions / 猫猫本地实时字幕

[简体中文](README.md) · By **OCCAT**

I'm **OCCAT**, and this is my local live caption tool for Windows. It turns audio playing on your computer, or speech from your microphone, into floating captions. You can also translate English, Japanese or Korean into Chinese when you need it. You can use it while watching videos, taking courses, playing games, watching streams or joining personal meetings.

## What you can do

- System-audio and microphone input, with model-dependent Chinese, English, Japanese, Korean and automatic recognition, displayed as floating captions.
- Optional real-time translation with original text; recognition engines, translation and model management share the Recognition and translation page.
- Short model descriptions and recommendations, official and mirror links, one-click downloads, resumable transfers, verification and local model import.
- Caption fonts, weights, size, color, outlines, shadows, placement and backdrop controls, with saved appearance versions.
- HarmonyOS Sans, MiSans, Source Han Sans and Source Han Serif interface fonts with their original weight choices, plus local TTF, OTF and TTC font import.
- Dark, day, system and custom themes. Custom backgrounds share glass opacity, blur and dimming controls; idle navigation icons follow text color and pressed or selected icons use the accent.
- Five icon entries with floating names and one moving indicator, Tab navigation, Ctrl+1–5 page shortcuts and optional interface motion.
- Pause, preview, hide, click-through, standby, tray access, stable-release update checks, mouse-wheel scrolling and direct touchpad input.

Changes and fixes belong in the [RC29 release notes](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.0-rc.29).

## Download and install

**[Open the 0.1.0 RC29 public preview](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.0-rc.29)**. This is a **prerelease**. [RC16](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.0-rc.16) remains available for rollback.

Choose **either the installer or the portable archive**. You do not need the entire repository or every ZIP:

| File | Purpose |
| --- | --- |
| [OCCAT-Live-Caption-0.1.0-windows-x64-setup.exe](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.0-rc.29/OCCAT-Live-Caption-0.1.0-windows-x64-setup.exe) | One installer with 中文 / English / 日本語 / 한국어 |
| [OCCAT-Live-Caption-0.1.0-windows-x64-portable.zip](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.0-rc.29/OCCAT-Live-Caption-0.1.0-windows-x64-portable.zip) | Extract the complete archive and run `OCCATLiveCaption.exe` |
| [SHA256SUMS.txt](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.0-rc.29/SHA256SUMS.txt) | Optional integrity checks for this release's public assets |
| Corresponding-source and Third-Party-Notices ZIPs | Library sources and license materials; not required for ordinary use |

1. Use **Windows 10/11 x64** with Microsoft Visual C++ x64 Runtime **14.44.35211 or newer**. If it is missing or outdated, setup asks before downloading it directly from Microsoft, verifies Microsoft's signature and opens the runtime installer. Confirm the Microsoft license and Windows administrator prompt; caption setup continues after a successful runtime check. This download needs internet access. Setup never restarts Windows automatically: save your work, restart and rerun setup if Microsoft requires a restart. The portable version also needs this runtime.
2. Run the installer and choose Chinese, English, Japanese or Korean, or fully extract the portable ZIP before starting it. Do not copy out the EXE alone. The installer has no commercial code-signing certificate; verify the download source and SHA-256.
3. Select the actual system output device or microphone, wait for the bundled **Whisper base** model, and start captions. Initial recognition requires no model download.
4. For translation, download or import a compatible **M2M100** model from Recognition and translation, then enable real-time translation. Leave it off for original captions only.
5. Adjust caption styling in Caption appearance and positioning, click-through and standby options in Window and standby. The footer language menu supports 中文, English, 日本語 and 한국어; recognition language is a separate setting.

The in-app version remains **0.1.0**; use the Release tag to identify each candidate. **Previews are not delivered through GitHub's stable latest-release endpoint. Download them manually from Releases.** RC13 users need the unified installer for their first upgrade. Japanese and Korean setup retain the reviewed original English component terms.

Installation is per user and preserves existing preferences. Both versions store settings, downloaded models and caption records under `%LOCALAPPDATA%/OCCATLiveCaption`; uninstall retains that data. The portable version does not store preferences alongside the extracted EXE.

## Custom theme example

![Custom theme, shared glass material and navigation](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.0-rc.29/custom-theme-example-2562eb7803b4b4bf.png)

This user-provided screenshot previews a custom theme. Select Custom in Page appearance to choose your own background image; the original wallpaper is not distributed with the installer.

## Validation and use

RC29 passed **121 related regression tests**. Independent Qt checks covered **48 configurations and 528 actual icon-state checks**. The same candidate passed isolated installation, offline startup and uninstall checks in Chinese, English, Japanese and Korean on the development computer, including loading the four interface font families' 30 original weight files.

**It has not been tested on a clean Windows system without the runtime and remains a prerelease.** I do not treat these checks as certification for every GPU, monitor, audio device or Windows configuration.

Recognition and translation run locally. Additional model downloads and update checks use the network. **Caption text is saved locally by default**; disable logging in Advanced settings if preferred. Disabling it does not remove previous records. Personal backgrounds and user-imported models or fonts are not bundled with official downloads.

Captions and translations can be wrong; verify important content yourself. This is a reading aid, not a substitute for professional accessibility services or formal records. Process content you are entitled to use and obtain permission before capturing other people's speech.

## Licenses and publication scope

My own code and these download-repository documents use [MIT](LICENSE), copyright **OCCAT**. **The application development source repository remains Private. This public repository provides downloads and distribution materials; it does not claim that all application source has been published.**

The complete package is not MIT-only. Fonts, Whisper base, Qt, FFmpeg/PyAV, Sherpa ASR and vendor components retain their respective licenses and terms. Original font licenses are included in the same-version notice archive.

Same-version releases provide third-party corresponding sources, build resources, original copyright notices and checksums. See [third-party notices](THIRD_PARTY_NOTICE_PUBLIC.md) and the [library modification/replacement guide](LIBRARY_REPLACEMENT.en.md). Applicable rights to modify, replace and debug LGPL libraries remain intact. Public assets exclude the application's own Source.zip, build reports and user data.

Please report issues in [Issues](https://github.com/occat666/occat-live-caption-download/issues), including the candidate version, system, model and reproduction steps. Remove private paths, account details, recordings and real conversations before submitting evidence.

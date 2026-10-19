# Maomao Local Live Captions / 猫猫本地实时字幕

[简体中文](README.md) · [繁體中文](README.zh-TW.md) · **English** · [日本語](README.ja.md) · [한국어](README.ko.md) · By **OCCAT**

<p align="center">
  <img src="assets/project-cover-eff03bbe0e0a.jpg" alt="Maomao Local Live Captions project cover" width="640">
</p>

I'm **OCCAT**, and this is my local live caption tool for Windows. It turns audio playing on your computer, or speech from your microphone, into floating captions. You can also translate English, Japanese or Korean into Chinese when you need it. You can use it while watching videos, taking courses, playing games, watching streams or joining personal meetings.

## What you can do

- System-audio and microphone input, with model-dependent Chinese, English, Japanese, Korean and automatic recognition, displayed as floating captions.
- Optional real-time translation with original text; recognition engines, translation and model management share the Recognition and translation page.
- Short model descriptions and recommendations, official and mirror links, one-click downloads, resumable transfers, verification and local model import.
- Caption fonts, weights, size, color, outlines, shadows, placement and backdrop controls, with saved appearance versions. Choose Simplified Chinese, Traditional Chinese or the original script for Chinese source captions and translations.
- Five interface and installer languages: 简体中文, 繁體中文, English, 日本語 and 한국어. Interface language, Chinese caption script and recognition language are saved separately.
- HarmonyOS Sans, MiSans, Source Han Sans and Source Han Serif interface fonts with their original weight choices, plus local TTF, OTF and TTC font import.
- Dark, day, system and custom themes. Custom backgrounds share glass opacity, blur and dimming controls; idle navigation icons follow text color and pressed or selected icons use the accent.
- Five Feather vector icon entries with floating names and one moving indicator, Tab navigation, Ctrl+1–5 page shortcuts and optional interface motion.
- Pause, preview, hide, click-through, standby, tray access, stable-release update checks, mouse-wheel scrolling and direct touchpad input.

Changes and fixes belong in the [0.1.5 release notes](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.5).

## What's new in 0.1.5

- The caption overlay shows recognition-model download, loading and warmup stages. It no longer says “Waiting for audio input” before the model is ready.
- Model-loading failures show the corresponding error. When the model is ready, the app automatically connects the selected audio input and then enters the waiting state; initialization can continue without restarting the app.
- Complete cached models still load locally without another download. First-download completion now explains that loading continues automatically. Accent settings remain available only in custom mode.

## Download and install

**[Open the 0.1.5 public preview](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.5)**. This is a **prerelease**. [The previous 0.1.1](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.1) remains available for rollback; other earlier releases are also retained.

Choose **either the installer or the portable archive**. You do not need the entire repository or every ZIP:

| File | Purpose |
| --- | --- |
| [OCCAT-Live-Caption-0.1.5-windows-x64-setup.exe](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.5/OCCAT-Live-Caption-0.1.5-windows-x64-setup.exe) | One installer with 简体中文 / 繁體中文 / English / 日本語 / 한국어 |
| [OCCAT-Live-Caption-0.1.5-windows-x64-portable.zip](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.5/OCCAT-Live-Caption-0.1.5-windows-x64-portable.zip) | Extract the complete archive and run `OCCATLiveCaption.exe` |
| [SHA256SUMS.txt](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.5/SHA256SUMS.txt) | Optional integrity checks for this release's public assets |
| Corresponding-source and Third-Party-Notices ZIPs | Library sources and license materials; not required for ordinary use |

1. Use **Windows 10/11 x64** with Microsoft Visual C++ x64 Runtime **14.44.35211 or newer**. If it is missing or outdated, setup asks before downloading it directly from Microsoft, verifies Microsoft's signature and opens the runtime installer. Confirm the Microsoft license and Windows administrator prompt; caption setup continues after a successful runtime check. This download needs internet access. Setup never restarts Windows automatically: save your work, restart and rerun setup if Microsoft requires a restart. The portable version also needs this runtime.
2. Run the installer and choose Simplified Chinese, Traditional Chinese, English, Japanese or Korean, or fully extract the portable ZIP before starting it. Do not copy out the EXE alone. The installer has no commercial code-signing certificate; verify the download source and SHA-256.
3. Select the actual system output device or microphone. New users default to **Whisper large-v3-turbo**: first use needs internet access to download about **1.6 GB** and verify its files. Downloads support resume and source fallback. Complete cached models are loaded locally and can run offline. Download the other 8 recognition models on demand or import compatible local files; upgrades preserve saved model choices.
4. For translation, download or import a compatible **M2M100** model from Recognition and translation, then enable real-time translation. Leave it off for original captions only.
5. Adjust caption styling in Caption appearance and positioning, click-through and standby options in Window and standby. The footer language menu supports 简体中文, 繁體中文, English, 日本語 and 한국어; recognition language is a separate setting. Choose Chinese caption script under Caption appearance → Text; changing interface language does not change it.

The software version is **0.1.5**, with release tag **`v0.1.5`**. It remains a prerelease. **Previews are not delivered through GitHub's stable latest-release endpoint. Download them manually from Releases.** Users of the older separate-language installers can upgrade manually with the unified installer above. Traditional Chinese, Japanese and Korean setup retain the reviewed original English component terms.

Installation is per user and preserves existing preferences. Both versions store settings, downloaded models and caption records under `%LOCALAPPDATA%/OCCATLiveCaption`; uninstall retains that data. The portable version does not store preferences alongside the extracted EXE.

**Upgrading from an older version:** Saved model choices and other settings are preserved. If Base is still selected, open Speech + translation → Recognition engine → Recognition model, choose `large-v3-turbo`, then click Apply and reload model to download and use Turbo. New users default to Turbo.

## Custom theme example

![Custom theme, shared glass material and navigation](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.5/custom-theme-example-2562eb7803b4b4bf.png)

This user-provided screenshot previews a custom theme. Select Custom in Page appearance to choose your own background image; the original wallpaper is not distributed with the installer.

## Validation and use

This round focuses on first-start status, loading failures, automatic audio connection after readiness, pause and reload behavior, and rejection of stale events.

This release passed **155 relevant unit checks**, frozen-app startup-state checks, and isolated installation, offline interface startup and uninstallation in all five installer languages. Both the source app and frozen app performed **real CPU recognition of a speech test fixture using the complete local cached Turbo model**, and their recognition child processes exited. This did not test a fresh model download. This round did not download the full weights again, capture live speech, test the reporter's hardware or verify a clean Windows system without the runtime; it does not certify every device or network configuration. Windows file version **0.1.5.0** was confirmed in the build report's frozen-app check.

**It has not been tested on a clean Windows system without the runtime and remains a prerelease.** I do not treat these checks as certification for every GPU, monitor, audio device or Windows configuration.

Recognition and translation run locally. First-use recognition model downloads, on-demand translation model downloads and update checks use the network. Complete cached models can run locally offline. **Caption text is saved locally by default**; disable logging in Advanced settings if preferred. Disabling it does not remove previous records. Personal backgrounds and user-imported models or fonts are not bundled with official downloads.

Captions and translations can be wrong; verify important content yourself. This is a reading aid, not a substitute for professional accessibility services or formal records. Process content you are entitled to use and obtain permission before capturing other people's speech.

## Licenses and publication scope

My own code and these download-repository documents use [MIT](LICENSE), copyright **OCCAT**. **The application development source repository remains Private. This public repository provides downloads and distribution materials; it does not claim that all application source has been published.**

The complete package is not MIT-only. Navigation and window controls use [official Feather v4.29.0 icons](https://github.com/feathericons/feather/tree/v4.29.0); the [original MIT license](https://github.com/feathericons/feather/blob/v4.29.0/LICENSE) is included in the installer and same-version notice archive. Fonts, on-demand Whisper models, Qt, FFmpeg/PyAV, Sherpa ASR and vendor components retain their respective licenses and terms. Original font licenses are included in the same-version notice archive.

Same-version releases provide third-party corresponding sources, build resources, original copyright notices and checksums. See [third-party notices](THIRD_PARTY_NOTICE_PUBLIC.md) and the [library modification/replacement guide](LIBRARY_REPLACEMENT.en.md). Applicable rights to modify, replace and debug LGPL libraries remain intact. Public assets exclude the application's own Source.zip, build reports and user data.

Please report issues in [Issues](https://github.com/occat666/occat-live-caption-download/issues), including the candidate version, system, model and reproduction steps. Remove private paths, account details, recordings and real conversations before submitting evidence.

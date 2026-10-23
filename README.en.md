# Maomao Local Live Captions / 猫猫本地实时字幕

[简体中文](README.md) · [繁體中文](README.zh-TW.md) · **English** · [日本語](README.ja.md) · [한국어](README.ko.md) · By **OCCAT**

<p align="center">
  <img src="assets/project-cover-eff03bbe0e0a.jpg" alt="Maomao Local Live Captions project cover" width="640">
</p>

I'm **OCCAT**, and this is my local live caption tool for Windows, with a native macOS preview. It turns audio playing on your computer, or speech from your microphone, into floating captions. You can also translate English, Japanese or Korean into Chinese when you need it. You can use it while watching videos, taking courses, playing games, watching streams or joining personal meetings.

## What you can do

- System-audio and microphone input, with model-dependent Chinese, English, Japanese, Korean and automatic recognition, displayed as floating captions.
- Optional real-time translation with original text; recognition engines, translation and model management share the Recognition and translation page.
- Short model descriptions and recommendations, official and mirror links, one-click downloads, resumable transfers, verification and local model import.
- Caption fonts, weights, size, color, outlines, shadows, placement and backdrop controls, with saved appearance versions. Caption glyphs have five choices: Simplified Chinese, Traditional Chinese, Japanese glyphs, Korean glyphs, or the original text. Simplified/traditional conversion affects Chinese only; Japanese and Korean use the bundled regional Source Han fonts and keep the source text, without translating it into Japanese or Korean.
- Five interface and installer languages: 简体中文, 繁體中文, English, 日本語 and 한국어. Interface language, caption glyphs and recognition language are saved separately.
- HarmonyOS Sans, MiSans, Source Han Sans and Source Han Serif interface fonts with their original weight choices, plus local TTF, OTF and TTC font import.
- Dark, day, system and custom themes. Custom backgrounds share glass opacity, blur and dimming controls; idle navigation icons follow text color and pressed or selected icons use the accent.
- Five Feather vector icon entries with floating names and one moving indicator, Tab navigation, Ctrl+1–5 page shortcuts and optional interface motion.
- Pause, preview, hide, click-through, standby, tray access, in-app public-release update checks including previews, mouse-wheel scrolling and direct touchpad input.

Changes and fixes belong in the [0.1.8 release notes](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.8).

## What's new in 0.1.8

- Verified the existing Windows installed updater: a current copy reports that it is up to date; an older copy downloads and verifies the installer, saves settings, and upgrades in its actual installation directory while retaining settings and models.
- Clarified update behavior for each runtime. Source runs still direct users to an installer; Mac updates still require downloading a new DMG and replacing the app.
- Windows and Mac downloads are both 0.1.8, retaining regional CJK caption glyphs, live translation and first-use large-v3-turbo downloads.

## What's new in 0.1.6 (previous release)

- In-app update checks find the newest public version, including previews, instead of relying only on GitHub's stable latest-release endpoint. After downloading and confirmation, installed copies upgrade in their current installation directory and retain settings, models and language choices.
- Portable copies explain the update path before opening the ordinary installation wizard; the original portable folder is not silently overwritten. **Version 0.1.5 and earlier must first install 0.1.6 or later manually from Releases; subsequent updates can use the new in-app updater.**
- A caption's auto-hide timer starts after its current translation completes. Partial-result translation is throttled and prioritizes the current utterance, reducing premature hiding and stale translations replacing a newer sentence. Pause, switching, clearing and retired jobs keep separate state.
- If the GitHub API is rate-limited or unavailable, update checks fall back to the project's official public update manifest. Installer downloads still require exact size and SHA-256 verification.

## Download and install

**[Open the 0.1.8 public preview](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.8)**. This is a **prerelease**. [The previous 0.1.7](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.7) remains available for rollback; other earlier releases are also retained.

Choose **either the installer or the portable archive**. You do not need the entire repository or every ZIP:

| File | Purpose |
| --- | --- |
| [OCCAT-Live-Caption-0.1.8-windows-x64-setup.exe](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.8/OCCAT-Live-Caption-0.1.8-windows-x64-setup.exe) | One installer with 简体中文 / 繁體中文 / English / 日本語 / 한국어 |
| [OCCAT-Live-Caption-0.1.8-windows-x64-portable.zip](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.8/OCCAT-Live-Caption-0.1.8-windows-x64-portable.zip) | Extract the complete archive and run `OCCATLiveCaption.exe` |
| [SHA256SUMS.txt](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.8/SHA256SUMS.txt) | Optional checksums for the existing Windows release assets |
| Corresponding-source and Third-Party-Notices ZIPs | Library sources and license materials; not required for ordinary use |

1. Use **Windows 10/11 x64** with Microsoft Visual C++ x64 Runtime **14.44.35211 or newer**. If it is missing or outdated, setup asks before downloading it directly from Microsoft, verifies Microsoft's signature and opens the runtime installer. Confirm the Microsoft license and Windows administrator prompt; caption setup continues after a successful runtime check. This download needs internet access. Setup never restarts Windows automatically: save your work, restart and rerun setup if Microsoft requires a restart. The portable version also needs this runtime.
2. Run the installer and choose Simplified Chinese, Traditional Chinese, English, Japanese or Korean, or fully extract the portable ZIP before starting it. Do not copy out the EXE alone. The installer has no commercial code-signing certificate; verify the download source and SHA-256.
3. Select the actual system output device or microphone. New users default to **Whisper large-v3-turbo**: first use needs internet access to download about **1.6 GB** and verify its files. Downloads support resume and source fallback. Complete cached models are loaded locally and can run offline. Download the other 8 recognition models on demand or import compatible local files; upgrades preserve saved model choices.
4. For translation, download or import a compatible **M2M100** model from Recognition and translation, then enable real-time translation. Leave it off for original captions only.
5. Adjust caption styling in Caption appearance and positioning, click-through and standby options in Window and standby. The footer language menu supports 简体中文, 繁體中文, English, 日本語 and 한국어; recognition language is a separate setting. Choose Chinese/Japanese/Korean caption glyphs under Caption appearance → Text; changing interface language does not change them.

The software version is **0.1.8**, with release tag **`v0.1.8`**. It remains a prerelease. **This version supports public preview updates in the app. Version 0.1.5 and earlier still query only the old latest endpoint and need one manual installation of 0.1.6 or later; later checks and updates can then run in the app.** Users of the older separate-language installers can upgrade manually with the unified installer above. Traditional Chinese, Japanese and Korean setup retain the reviewed original English component terms.

Installation is per user and preserves existing preferences. Both versions store settings, downloaded models and caption records under `%LOCALAPPDATA%/OCCATLiveCaption`; uninstall retains that data. The portable version does not store preferences alongside the extracted EXE.

**Upgrading from an older version:** Saved model choices and other settings are preserved. If Base is still selected, open Speech + translation → Recognition engine → Recognition model, choose `large-v3-turbo`, then click Apply and reload model to download and use Turbo. New users default to Turbo.

## macOS preview downloads

**Mac 0.1.8 native previews are available for Apple Silicon and Intel.** Both architectures passed cloud macOS builds, frozen GUI and CPU recognition tests, followed by independent local artifact verification. Physical microphone and playback capture still require user testing on a Mac.

**Requires macOS 14 or newer.** Choose one DMG for your processor:

| Mac processor | Download |
| --- | --- |
| Apple silicon (M1 and later) | [OCCATLiveCaption-0.1.8-macOS-arm64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.8/OCCATLiveCaption-0.1.8-macOS-arm64.dmg) |
| Intel | [OCCATLiveCaption-0.1.8-macOS-x86_64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.8/OCCATLiveCaption-0.1.8-macOS-x86_64.dmg) |

Open the DMG and drag the app to Applications. This preview is **ad-hoc signed and is not Apple-notarized**. After your first attempt to open it, macOS may require Open Anyway for this app in System Settings → Privacy & Security. Verify the Mac assets with [SHA256SUMS-macOS.txt](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.8/SHA256SUMS-macOS.txt) from the same Release. The Mac update entry opens the Releases download page; download a new DMG and replace the app. Settings, models and caption records reside in `~/Library/Application Support/OCCATLiveCaption`.

The Mac preview uses **CPU inference**. New users still download **large-v3-turbo (about 1.6 GB)** on first use; no model is bundled and the app does not automatically switch to Base. Other models remain optional downloads. CPU speed for large models depends on hardware; real-time performance is not guaranteed.

Audio comes from CoreAudio inputs and microphone permission is required when capture starts. Capturing playback audio requires **BlackHole or another virtual input installed and configured by you**; the app includes and installs no audio driver. See [macOS audio setup (Chinese)](docs/macos-audio.md).

Native CI checked both architectures' frozen Cocoa interface, captions/fonts, process cleanup and HTTPS certificate verification. A real CPU recognition check used `tiny.en` and a temporary utterance generated by `say`; it does not measure Turbo performance or accuracy. **Physical-Mac microphone permission/capture, BlackHole playback capture, long sessions, and overlay behavior across Spaces/full-screen apps have not completed acceptance testing.** Component notices and shared-library replacement instructions are inside the app; corresponding third-party sources are attached to the same Release.

The Mac preview bundles Source Han Sans, Source Han Serif, and the Japanese/Korean regional Source Han Sans fonts; additional fonts can be imported locally.

## Custom theme example

![Custom theme, shared glass material and navigation](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.6/custom-theme-example-2562eb7803b4b4bf.png)

This user-provided screenshot previews a custom theme. Select Custom in Page appearance to choose your own background image; the original wallpaper is not distributed with the installer.

## Validation and use

Windows 0.1.8 passed 62 updater unit checks, 2 update-job/interface integration checks, frozen-app offline checks, isolated install/start/uninstall in all five installer languages, and a real 0.1.7 → 0.1.8 upgrade in a custom directory containing spaces. Settings and model verification fixtures remained unchanged; file version is **0.1.8.0**, and regional CJK glyphs, source-text preservation and translation lifecycle checks passed. The lifecycle check uses synthetic translation delivery, not a new native M2M100 inference run. The 414 checks and native M2M100 fixture from 0.1.7 are historical evidence, not new 0.1.8 results. These checks do not constitute clean-Windows, live-audio or all-hardware acceptance.

**It has not been tested on a clean Windows system without the runtime and remains a prerelease.** I do not treat these checks as certification for every GPU, monitor, audio device or Windows configuration.

Recognition and translation run locally. First-use recognition model downloads, on-demand translation model downloads and update checks use the network. Complete cached models can run locally offline. **Caption text is saved locally by default**; disable logging in Advanced settings if preferred. Disabling it does not remove previous records. Personal backgrounds and user-imported models or fonts are not bundled with official downloads.

Captions and translations can be wrong; verify important content yourself. This is a reading aid, not a substitute for professional accessibility services or formal records. Process content you are entitled to use and obtain permission before capturing other people's speech.

## Licenses and publication scope

My own code and these download-repository documents use [MIT](LICENSE), copyright **OCCAT**. **The application development source repository remains Private. This public repository provides downloads and distribution materials; it does not claim that all application source has been published.**

The complete package is not MIT-only. Navigation and window controls use [official Feather v4.29.0 icons](https://github.com/feathericons/feather/tree/v4.29.0); the [original MIT license](https://github.com/feathericons/feather/blob/v4.29.0/LICENSE) is included in the installer and same-version notice archive. Fonts, on-demand Whisper models, Qt, FFmpeg/PyAV, Sherpa ASR and vendor components retain their respective licenses and terms. Original font licenses are included in the same-version notice archive. The added Japanese and Korean regional Source Han Sans fonts are original Adobe files under SIL Open Font License 1.1; their original licenses accompany the same-version materials.

Same-version releases provide third-party corresponding sources, build resources, original copyright notices and checksums. See [third-party notices](THIRD_PARTY_NOTICE_PUBLIC.md) and the [library modification/replacement guide](LIBRARY_REPLACEMENT.en.md). Applicable rights to modify, replace and debug LGPL libraries remain intact. Public assets exclude the application's own Source.zip, build reports and user data.

Please report issues in [Issues](https://github.com/occat666/occat-live-caption-download/issues), including the candidate version, system, model and reproduction steps. Remove private paths, account details, recordings and real conversations before submitting evidence.

# Maomao Local Live Captions / 猫猫本地实时字幕

[简体中文](README.md) · By **OCCAT**

I'm **OCCAT**, and this is my local live caption tool for Windows. It turns audio playing on your computer, or speech from your microphone, into floating captions. You can also translate English, Japanese or Korean into Chinese when you need it. You can use it while watching videos, taking courses, playing games, watching streams or joining personal meetings.

## What you can do

- **Caption system audio or a microphone.** Select the sound device you use and start recognition. Chinese, English, Japanese, Korean and automatic detection are available according to the languages supported by your current caption model.
- **Turn on local translation when needed.** Translate English, Japanese or Korean into Chinese, with the option to keep the original text visible too. Leave translation off for original captions only.
- **Make captions your own.** Adjust the font, weight, size, color, outline, shadow, position and backdrop. You can also import local TTF, OTF and TTC fonts.
- **Choose a page theme.** Use dark, light, system or custom mode. Custom mode lets you choose your own background image and adjust glass transparency and blur.
- **Control the floating captions.** Pause, hide or preview captions, enable click-through, and access the app from the tray. Save appearance presets, switch between them or restore defaults.
- **Choose models and interface languages.** Import compatible local recognition and translation models. The interface supports 中文, English, 日本語 and 한국어; its language is separate from the recognition language.

## Download and get started

**[Download the Windows x64 installer](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.0-rc.16/OCCAT-Live-Caption-0.1.0-windows-x64-setup.exe)**

The current build is **0.1.0 RC16, a public preview**. You only need this one EXE for normal use; there is no need to download the repository or the source archives. The same installer offers Chinese, English, Japanese and Korean.

1. Use **Windows 10/11 x64** and follow the setup wizard. Microsoft Visual C++ x64 Runtime **14.44.35211 or newer** is required. If it is missing or outdated, setup asks to download and install it directly from Microsoft. Confirm Microsoft's license and the Windows administrator prompt, then caption setup continues. If Microsoft requires a restart, save your work, restart Windows and run caption setup again.
2. Open the app, select the actual system output device or microphone, wait for the bundled **Whisper base** model, then start captions. You do not need another model download for initial recognition.
3. To use translation, download or import a compatible **M2M100** translation model, then enable real-time translation.
4. Use Caption appearance for caption styling, Window and standby for positioning and click-through, and Page appearance for themes.

The installer does not currently have a commercial code-signing certificate. Download it from the repository link above; the same Release includes `SHA256SUMS.txt` for checking file integrity.

**[Latest version and release notes](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.0-rc.16)**: each Release lists its additions, changes and fixes. Download preview builds manually from Releases; the in-app update check is for stable releases.

## Custom theme example

![Custom theme with a background image and glass settings](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.0-rc.16/custom-theme-example.png)

Here is one example of a custom theme. Open Page appearance, select Custom, choose your own background image, then adjust blur and transparency. The wallpaper in this example is not bundled with the installer.

## Local data and a few things to know

Recognition and translation run on your computer. Downloading additional models and checking for updates need internet access. **Caption text is saved locally by default.** You can turn this off in Advanced settings; existing records must be deleted separately.

Settings, models and caption records are stored in `%LOCALAPPDATA%/OCCATLiveCaption`. Installation is per user, upgrades keep existing settings, and uninstalling retains user data. Your own background images, models and fonts do not become part of the official installer.

Captions and translations can be wrong, so please check important content yourself. The release notes describe what has been tested for the current preview.

## Licenses and project scope

My own code and these documents use the [MIT license](LICENSE), credited to **OCCAT**. The development source repository remains private; this repository is the public download page.

Fonts, models and third-party components keep their own licenses. I include their notices, corresponding sources and build materials with each Release. You can find the details in the [third-party notices](THIRD_PARTY_NOTICE_PUBLIC.md) and [library modification and replacement guide](LIBRARY_REPLACEMENT.en.md).

If something goes wrong, tell me in [Issues](https://github.com/occat666/occat-live-caption-download/issues), including your version, system, model and steps to reproduce it. Remove private paths, account details, recordings and real conversations from screenshots or logs before posting.

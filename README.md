# 猫猫本地实时字幕 / Maomao Local Live Captions

**简体中文** · [繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

本地实时字幕工具，支持将系统声音或麦克风语音显示为悬浮字幕或实时记录，并提供离线翻译。

## 下载

当前版本为 [0.1.29 公开测试版](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.29)。Windows 安装版和免安装版任选一种；Mac 按芯片类型选择。

| 版本 | 下载文件 |
| --- | --- |
| Windows 安装版 | [OCCAT-Live-Caption-0.1.29-windows-x64-setup.exe](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.29/OCCAT-Live-Caption-0.1.29-windows-x64-setup.exe) |
| Windows 免安装版 | [OCCAT-Live-Caption-0.1.29-windows-x64-portable.zip](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.29/OCCAT-Live-Caption-0.1.29-windows-x64-portable.zip) |
| Mac · Apple 芯片 | [OCCATLiveCaption-0.1.29-macOS-arm64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.29/OCCATLiveCaption-0.1.29-macOS-arm64.dmg) |
| Mac · Intel | [OCCATLiveCaption-0.1.29-macOS-x86_64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.29/OCCATLiveCaption-0.1.29-macOS-x86_64.dmg) |

[Windows SHA-256](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.29/SHA256SUMS.txt) · [macOS SHA-256](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.29/SHA256SUMS-macOS.txt) · [Releases](https://github.com/occat666/occat-live-caption-download/releases)

## 主要功能

- 悬浮字幕与实时记录两种模式，支持回看、复制字幕历史。
- 支持中文（简体／繁体）、英语、日语、韩语的识别显示与互相翻译；可用识别语言取决于所选模型。
- 原文与译文的字体、颜色、描边、阴影及背景分别调节。
- 识别与翻译在本机执行；模型下载和更新检查需要联网，模型缓存完整后可离线使用。

## 开始使用

1. Windows 运行安装器，或完整解压免安装包后运行 `OCCATLiveCaption.exe`；Mac 将 DMG 中的应用拖入“应用程序”。
2. 选择实际播放声音的设备或麦克风，下载识别模型。默认 Whisper large-v3-turbo 约 1.6 GB，其他模型可按需选择。
3. 需要翻译时，下载或导入 M2M100 翻译模型，选择目标语言，再开启翻译。

**Windows:** 支持 Windows 10/11 x64，需要 Visual C++ x64 运行库 14.44.35211 或更新版；安装器会检查并引导安装。

**macOS:** 需要 macOS 14 或更新版。预览版使用 CPU 推理，未经 Apple 公证；系统声音采集需要自行配置 BlackHole 等虚拟输入。详见 [Mac 音频设置](docs/macos-audio.md)。

## 说明与反馈

[使用说明](docs/USER_GUIDE.zh-CN.md) · [更新记录与旧版下载](https://github.com/occat666/occat-live-caption-download/releases) · [问题反馈](https://github.com/occat666/occat-live-caption-download/issues)

默认在本地保存字幕文本，可在字幕设置中关闭。识别和翻译可能有误，重要内容请人工核对。

作者：OCCAT。本仓库提供安装包和分发材料，应用开发源码保持私有。本仓库自有内容采用 [MIT](LICENSE)；安装包中的第三方组件和字体分别遵循其原始许可，详见 [第三方许可](THIRD_PARTY_NOTICE_PUBLIC.md)及[共享库替换说明](LIBRARY_REPLACEMENT.zh-CN.md)。

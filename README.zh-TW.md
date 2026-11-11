# 猫猫本地实时字幕 / Maomao Local Live Captions

[简体中文](README.md) · **繁體中文** · [English](README.en.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

本機即時字幕工具，可將系統聲音或麥克風語音顯示為懸浮字幕或即時記錄，並提供離線翻譯。

## 下載

目前版本為 [0.1.28 公開測試版](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.28)。Windows 安裝版與免安裝版擇一下載；Mac 依晶片類型選擇。

| 版本 | 下載檔案 |
| --- | --- |
| Windows 安裝版 | [OCCAT-Live-Caption-0.1.28-windows-x64-setup.exe](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.28/OCCAT-Live-Caption-0.1.28-windows-x64-setup.exe) |
| Windows 免安裝版 | [OCCAT-Live-Caption-0.1.28-windows-x64-portable.zip](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.28/OCCAT-Live-Caption-0.1.28-windows-x64-portable.zip) |
| Mac · Apple 晶片 | [OCCATLiveCaption-0.1.28-macOS-arm64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.28/OCCATLiveCaption-0.1.28-macOS-arm64.dmg) |
| Mac · Intel | [OCCATLiveCaption-0.1.28-macOS-x86_64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.28/OCCATLiveCaption-0.1.28-macOS-x86_64.dmg) |

[Windows SHA-256](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.28/SHA256SUMS.txt) · [macOS SHA-256](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.28/SHA256SUMS-macOS.txt) · [Releases](https://github.com/occat666/occat-live-caption-download/releases)

## 主要功能

- 懸浮字幕與即時記錄兩種模式，可回看及複製字幕歷史。
- 支援中文（簡體／繁體）、英語、日語、韓語的辨識顯示與互相翻譯；可用辨識語言取決於所選模型。
- 原文與譯文的字型、顏色、描邊、陰影和背景可分別調整。
- 辨識與翻譯在本機執行；模型下載與檢查更新需要連線，完整快取模型後可離線使用。

## 開始使用

1. Windows 執行安裝程式，或完整解壓免安裝包後執行 `OCCATLiveCaption.exe`；Mac 將 DMG 中的應用程式拖入「應用程式」。
2. 選擇實際播放聲音的裝置或麥克風，下載辨識模型。預設 Whisper large-v3-turbo 約 1.6 GB，亦可按需選擇其他模型。
3. 需要翻譯時，下載或匯入 M2M100 翻譯模型，選擇目標語言，再開啟翻譯。

**Windows:** 支援 Windows 10/11 x64，需要 Visual C++ x64 執行階段 14.44.35211 或更新版本；安裝程式會檢查並引導安裝。

**macOS:** 需要 macOS 14 或更新版本。預覽版使用 CPU 推論，尚未通過 Apple 公證；擷取系統聲音須自行設定 BlackHole 等虛擬輸入。詳見 [Mac 音訊設定](docs/macos-audio.md)。

## 說明與回報

[使用說明](docs/USER_GUIDE.zh-CN.md) · [更新記錄與舊版下載](https://github.com/occat666/occat-live-caption-download/releases) · [問題回報](https://github.com/occat666/occat-live-caption-download/issues)

預設在本機儲存字幕文字，可在字幕設定中關閉。辨識與翻譯可能有誤，重要內容請人工核對。

作者：OCCAT。本儲存庫提供安裝包與分發材料，應用程式開發原始碼維持私有。自有內容採用 [MIT](LICENSE)；第三方元件與字型各自遵循原始授權，詳見[第三方授權](THIRD_PARTY_NOTICE_PUBLIC.md)及[共用函式庫替換說明](LIBRARY_REPLACEMENT.zh-CN.md)。

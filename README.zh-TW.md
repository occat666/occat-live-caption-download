# 貓貓本地即時字幕 / Maomao Local Live Captions

[简体中文](README.md) · **繁體中文** · [English](README.en.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · 作者 **OCCAT**

<p align="center">
  <img src="assets/project-cover-eff03bbe0e0a.jpg" alt="貓貓本地即時字幕專案封面" width="640">
</p>

我是 **OCCAT**，這是我做的本機即時字幕工具，提供 Windows 版與 macOS 原生預覽版。你可以把電腦正在播放的聲音，或者麥克風裡的說話聲，顯示成浮動字幕；需要的時候，也可以把英文、日文、韓文翻譯成中文。看影片、聽課、玩遊戲、看直播，或者開個人會議時，都可以用它輔助閱讀。

## 可以怎麼用

- 系統聲音和麥克風輸入；按辨識模型能力選擇中文、英文、日文、韓文或自動判斷，以浮動字幕顯示。
- 獨立的即時翻譯開關，可同時保留原文；辨識引擎、翻譯和模型管理集中在「辨識與翻譯」。
- 模型說明與推薦提示、官方和鏡像下載入口、一鍵下載、斷點續傳、檔案驗證及本地模型匯入。
- 字幕字型、字重、字級、顏色、描邊、陰影、位置與底襯可調；可以儲存外觀版本，按需要恢復。字幕字形可選簡體中文、繁體中文、日語（日本字形）、韓語（韓文字形）或保留原文；簡繁轉換僅影響中文，日語、韓語使用內建地區思源字型並保留來源文字，不會將內容翻譯成日語或韓語。
- 简体中文、繁體中文、English、日本語、한국어 五種頁面語言與安裝語言；介面語言、字幕字形、語音辨識語言分別儲存。
- 介面提供 HarmonyOS Sans、MiSans、思源黑體、思源宋體，按各自原生字重選擇；也支援本地 TTF、OTF、TTC 字型匯入。
- 黑夜、白天、跟隨系統和自訂主題；自訂背景與玻璃透明度、模糊、壓暗設定同步。預設導覽圖示跟隨文字色，按下或選取使用主題色。
- 五個 Feather 向量圖示入口、浮動名稱提示和單一滑動遊標；支援 Tab 鍵盤導覽、Ctrl+1～5 切頁及關閉頁面動效。
- 暫停、預覽、隱藏字幕、視窗穿透、待機、系統匣入口和軟體內公開版本更新檢查（含預覽版）；設定頁支援滑鼠滾輪和觸控板滾動。

這次改動與修正的具體內容放在 [0.1.8 發行說明](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.8)。

## 0.1.8 更新

- 驗證 Windows 安裝版更新流程：已是最新版時顯示提示；有新版時下載並驗證安裝包，儲存設定後覆蓋原安裝目錄，保留設定與模型。
- 更新機制沿用既有實作，本版補齊不同執行方式的說明與版本一致性驗證；原始碼執行仍提示下載安裝版，Mac 仍以新 DMG 手動替換。
- Windows 與 Mac 下載均為 0.1.8，保留中日韓字幕字形、即時翻譯及首次下載 large-v3-turbo。

## 0.1.6 更新（歷史）

- 軟體內檢查最新公開版本，包含預覽版，不再只依賴 GitHub 的 latest 正式版介面。下載安裝程式並確認後，已安裝版在目前安裝目錄覆蓋升級，保留既有設定、模型與語言選擇。
- 免安裝版先說明更新方式，再開啟一般安裝精靈；不會在背景覆蓋原免安裝目錄。**0.1.5 及更早版本需先從 Releases 手動安裝一次 0.1.6 或更新版，之後才能使用新版的軟體內更新。**
- 目前句子的翻譯完成後才開始計算自動隱藏時間；即時中間辨識結果的翻譯經過節流，並優先處理目前句子，減少字幕過早隱藏與舊譯文蓋過新句的情況。暫停、切換、清空與舊任務的狀態互相隔離。
- GitHub API 達到流量限制或連線失敗時，改用專案官方公開更新清單繼續檢查；安裝程式仍依精確檔案大小及 SHA-256 驗證。

## 下載與安裝

**[開啟 0.1.8 公開測試版](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.8)**。這是 **prerelease 預發行版本**；[上一版 0.1.7](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.7) 保留，方便回復舊版，其他舊版也保留在 Releases。

安裝版和免安裝版**選一個即可**，不用下載整個倉庫或所有 ZIP：

| 檔案 | 選擇方式 |
| --- | --- |
| [OCCAT-Live-Caption-0.1.8-windows-x64-setup.exe](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.8/OCCAT-Live-Caption-0.1.8-windows-x64-setup.exe) | 安裝版，統一提供简体中文 / 繁體中文 / English / 日本語 / 한국어 |
| [OCCAT-Live-Caption-0.1.8-windows-x64-portable.zip](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.8/OCCAT-Live-Caption-0.1.8-windows-x64-portable.zip) | 免安裝版，完整解壓縮後執行 `OCCATLiveCaption.exe` |
| [SHA256SUMS.txt](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.8/SHA256SUMS.txt) | 可選，僅用於核對原有 Windows 公開附件 |
| `CorrespondingSources-*.zip`、`Sources-Sherpa-ASR-*.zip`、`OCCAT-Live-Caption-0.1.8-Third-Party-Notices.zip` | 第三方對應原始碼與授權材料，一般使用時不必逐一下載 |

1. 使用 **Windows 10/11 x64**，並具備 Microsoft Visual C++ x64 執行階段程式庫 **14.44.35211 或更新版**。安裝器發現執行階段程式庫缺失或過舊時，會在確認後從微軟官方下載、驗證數位簽章並開啟安裝介面。請按提示確認微軟授權及管理員授權，完成後自動繼續字幕安裝；需要連線至網路，不會自動重新啟動。微軟提示必須重新啟動時，請儲存工作、自行重新啟動，再執行字幕安裝器。免安裝版同樣需要先具備執行階段程式庫。
2. 安裝版按兩下 EXE，選擇簡體中文、繁體中文、英文、日文或韓文並依精靈完成安裝；免安裝版請完整解壓縮後啟動，不要單獨取出 EXE。安裝套件沒有商業程式碼簽章，請核對下載來源與 SHA-256。
3. 啟動「貓貓本地即時字幕」，選擇實際播放聲音的系統裝置或麥克風。新使用者預設使用 **Whisper large-v3-turbo**，首次使用需連線下載約 **1.6 GB** 並完成驗證；下載支援續傳和來源切換，完整快取後優先從本機載入，可離線使用。其他 8 個辨識模型按需下載，也可匯入相容的本地模型；升級不覆蓋已有模型選擇。
4. 需要翻譯時，在「辨識與翻譯」下載或匯入相容的 **M2M100** 模型，再開啟「即時翻譯」；只看原文時保持關閉。
5. 在「字幕外觀」調整字幕樣式，在「視窗與待機」調整位置、穿透和待機方式。底部語言選單支援简体中文、繁體中文、English、日本語、한국어，辨識語言單獨設定。中日韓字幕字形在「字幕外觀 → 文字」設定，不隨介面語言切換。

本版的軟體版本號為 **0.1.8**，發行標籤為 **`v0.1.8`**，仍按預發行版本提供。**本版的軟體內更新支援公開預覽版。0.1.5 及更早版本仍只查詢舊的 latest 介面，需先手動安裝一次 0.1.6 或更新版；之後可在軟體內檢查並更新。** 舊分語言安裝套件使用者可手動升級到上面的統一安裝套件；繁體中文、日文、韓文安裝精靈保留已審閱的英文元件條款原文。

按使用者安裝，已有設定優先。安裝版和免安裝版均把設定、下載模型和字幕記錄儲存到 `%LOCALAPPDATA%/OCCATLiveCaption`，解除安裝保留使用者資料；免安裝版不會把設定放在解壓縮目錄裡。

**從舊版升級：** 已有模型選擇與其他設定會保留。如果升級後仍顯示 Base，請到「辨識與翻譯 → 辨識引擎 → 辨識模型」選擇 `large-v3-turbo`，再點擊重新載入按鈕（介面顯示「應用並過載模型」），即可下載並使用 Turbo；新使用者預設選擇 Turbo。

## macOS 預覽版下載

**Mac 0.1.8 已提供 Apple 晶片與 Intel 原生預覽套件。** 兩種架構均完成雲端 macOS 建置、凍結介面與 CPU 辨識測試，並在本機獨立核驗。實體 Mac 的麥克風與系統收音仍需使用者實測。

**需要 macOS 14 或更新版本。** 依處理器選擇一個 DMG：

| Mac 類型 | 下載 |
| --- | --- |
| Apple 晶片（M1 及更新機型） | [OCCATLiveCaption-0.1.8-macOS-arm64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.8/OCCATLiveCaption-0.1.8-macOS-arm64.dmg) |
| Intel | [OCCATLiveCaption-0.1.8-macOS-x86_64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.8/OCCATLiveCaption-0.1.8-macOS-x86_64.dmg) |

開啟 DMG，將應用程式拖到「應用程式」資料夾。此預覽套件採用 **ad-hoc 簽章，未經 Apple 公證**；首次嘗試開啟後，macOS 可能要求在「系統設定 → 隱私權與安全性」針對此應用程式選擇「強制打開」。請使用同版 Release 的 [SHA256SUMS-macOS.txt](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.8/SHA256SUMS-macOS.txt) 核對 Mac 附件。Mac 版的更新入口會開啟 Releases 下載頁；下載新 DMG 並替換應用程式，設定、模型與字幕記錄保存在 `~/Library/Application Support/OCCATLiveCaption`。

Mac 版使用 **CPU 推論**，新使用者仍預設在首次使用時下載 **large-v3-turbo（約 1.6 GB）**，不內建模型，也不會自動改選 Base；其他模型按需下載。大型模型的 CPU 速度取決於硬體，預覽套件不保證即時效能。

音訊來源採用 CoreAudio 輸入，開始擷取時需要允許麥克風權限。播放中的系統聲音需要自行安裝並設定 **BlackHole 等虛擬輸入**，軟體不隨附或安裝音訊驅動程式。步驟見 [macOS 聲音來源設定（簡體中文）](docs/macos-audio.md)。

兩種架構已在原生 CI 中檢查凍結應用程式的 Cocoa 介面、字幕與字型、程序回收及 HTTPS 憑證驗證；另以執行時暫時產生的 `say` 語音與 `tiny.en` 完成真實 CPU 辨識。此測試資料不代表 Turbo 的效能或準確率。**實體 Mac 的麥克風授權與擷取、BlackHole 系統聲音、長時間執行，以及多桌面 Spaces／全螢幕置頂仍未完成驗收。** 元件授權與共享程式庫替換說明位於應用程式套件內，對應第三方原始碼附件見同版 Release。

Mac 預覽套件內建思源黑體、思源宋體及日語／韓語地區思源字型，其他字型可從本機匯入。

## 自訂主題範例

![自訂主題、玻璃材質與導覽預覽](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.6/custom-theme-example-2562eb7803b4b4bf.png)

這是使用者提供的自訂主題截圖預覽。在「頁面外觀」選擇「自訂」後，可以自行設定背景圖片；原始桌布不隨安裝套件分發。

## 驗證範圍與使用說明

Windows 0.1.8 已通過 62 項更新單元檢查、2 項更新工作與介面聯通檢查、凍結程式離線檢查、五種安裝語言的隔離安裝／啟動／解除安裝，以及實際 0.1.7 → 0.1.8 含空格自訂目錄覆蓋升級。升級後設定與模型校驗樣本保持不變；檔案版本為 **0.1.8.0**，中日韓地區字形、原始文字保留與翻譯生命週期檢查通過。翻譯生命週期使用合成譯文交付，並非本輪實際 M2M100 推理；0.1.7 的 414 項檢查與原生 M2M100 測試為歷史證據，不計作本版新執行。這些檢查不等同於乾淨 Windows、現場音訊或所有硬體實測。

**尚未在缺少執行階段程式庫的乾淨 Windows 環境實測，仍屬於預發行版本。** 我沒有把這些檢查當作所有 GPU、多螢幕、音訊裝置和系統組合的保證。

辨識和翻譯在本機執行；首次辨識模型下載、按需翻譯模型下載和更新檢查會連線至網路，模型完整快取後可在本機離線使用。**預設儲存本地字幕文字**，可在進階設定關閉，關閉不會刪除舊記錄。個人背景圖片、自行匯入的模型和字型不隨官方安裝套件釋出。

字幕和翻譯可能有誤，重要內容請人工核對；這是輔助閱讀工具，不替代專業無障礙服務或正式記錄。請只處理有權使用的內容，採集他人發言前取得必要授權。

## 授權與公開範圍

本下載倉庫文件及我自己的程式碼採用 [MIT](LICENSE)，署名 **OCCAT**。**應用開發原始碼倉庫保持 Private；這個公共倉庫提供軟體下載與分發材料，不表示全部應用原始碼已經公開。**

安裝套件並非整套 MIT。導覽與視窗控制元件使用 [Feather v4.29.0 官方圖示](https://github.com/feathericons/feather/tree/v4.29.0)，其 [MIT 原始授權](https://github.com/feathericons/feather/blob/v4.29.0/LICENSE) 隨安裝套件和同版通知歸檔提供。四種介面字型、Whisper 模型（按需下載）、Qt、FFmpeg/PyAV、Sherpa ASR、Intel/NVIDIA 等保留各自適用的授權和元件條款；字型的原始授權也隨本版通知歸檔提供。 新增的日語、韓語地區思源黑體保持 Adobe 官方原版，採用 SIL Open Font License 1.1，原始授權隨同版材料提供。

同版 Release 附第三方對應原始碼、建置材料、原始版權通知和校驗清單。入口見[第三方授權說明](THIRD_PARTY_NOTICE_PUBLIC.md)與[共用程式庫修改/替換指引](LIBRARY_REPLACEMENT.zh-CN.md)；適用的 LGPL 修改、替換及必要偵錯權利保持不變。公開附件不包含自有應用 Source.zip、建置報告或使用者資料。

歡迎在 [Issues](https://github.com/occat666/occat-live-caption-download/issues) 回報問題，附候選版本、系統、模型和重現步驟，提交前請刪除私人目錄、帳號、錄音與真實對話內容。

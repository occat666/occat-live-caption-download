# 猫猫本地实时字幕 / Maomao Local Live Captions

**简体中文** · [繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · 作者 **OCCAT**

<p align="center">
  <img src="assets/project-cover-eff03bbe0e0a.jpg" alt="猫猫本地实时字幕项目封面" width="640">
</p>

我是 **OCCAT**，这是我做的本地实时字幕工具，提供 Windows 版和 macOS 原生预览版。你可以把电脑正在播放的声音，或者麦克风里的说话声，显示成悬浮字幕；需要的时候，也可以把英文、日文、韩文翻译成中文。看视频、听课、玩游戏、看直播，或者开个人会议时，都可以用它辅助阅读。

## 可以怎么用

- 系统声音和麦克风输入；按识别模型能力选择中文、英文、日文、韩文或自动判断，字幕悬浮显示。
- 独立的实时翻译开关，可同时保留原文；识别引擎、翻译和模型管理集中在“识别与翻译”。
- 模型说明与推荐提示、官方和镜像入口、一键下载、断点续传、文件校验及本地模型导入。
- 字幕字体、字重、字号、颜色、描边、阴影、位置与底衬可调；可以保存外观版本，按需要恢复。字幕字形可选简体中文、繁體中文、日语（日本字形）、韩语（韩文字形）或保留原文；简繁转换仅作用于中文，日语、韩语使用内置地区思源字体并保留源文本，不会把内容翻译成日语或韩语。
- 简体中文、繁體中文、English、日本語、한국어 五种页面语言与安装语言；界面语言、字幕字形、语音识别语言分别保存。
- 界面提供 HarmonyOS Sans、MiSans、思源黑体、思源宋体，按各自原生字重选择；也支持本地 TTF、OTF、TTC 字体导入。
- 黑夜、白天、跟随系统和自定义主题；自定义背景与玻璃透明度、模糊、压暗设置同步。默认导航图标跟随文字色，按下或选中使用主题色。
- 五个 Feather 矢量图标入口、悬浮名称提示和单一滑动游标；支持 Tab 键盘导航、Ctrl+1～5 切页及关闭页面动效。
- 暂停、预览、隐藏字幕、窗口穿透、待机、托盘入口和软件内公开版本更新检查（含预览版）；设置页支持鼠标滚轮和触控板滚动。

这次改动与修正的具体内容放在 [0.1.9 发布说明](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.9)。

## 0.1.9 更新

- 识别原文与翻译字幕的格式独立设置：字体、字号、字重、颜色、不透明度、描边和阴影均可分别调节。
- 打开“字幕外观”，分别调整“识别原文”和“翻译字幕”；翻译关闭时也能预览译文样式。位置、背景、行间距和最多行数共用。
- 旧设置会自动复制为译文的初始样式，此后两组设置独立保存。支持五种界面语言，保留实时翻译、中日韩字形和首次下载 large-v3-turbo。

## 0.1.6 更新（历史）

- 软件内检查最新公开版本，包含预览版，不再只依赖 GitHub 的 latest 正式版接口。下载安装包并确认后，已安装版在当前安装目录覆盖升级，保留已有设置、模型和语言选择。
- 便携版先说明更新方式，再打开普通安装向导；不会静默覆盖原便携目录。**0.1.5 及更早版本需先从 Releases 手动安装一次 0.1.6 或更新版，之后可使用新版的软件内更新。**
- 当前句翻译完成后才开始计算自动隐藏时间；实时中间识别结果的翻译经过节流，并优先处理当前句，减少字幕被过早隐藏及旧译文覆盖新句的情况。暂停、切换、清空及旧任务的状态相互隔离。
- GitHub API 限流或连接失败时，改用项目官方公开更新清单继续检查；安装包仍按精确文件大小及 SHA-256 校验。

## 下载与安装

**[打开 0.1.9 公开测试版](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.9)**。这是 **prerelease 预发布版本**；[上一版 0.1.8](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.8) 保留供回退，其他旧版也保留在 Releases。

安装版和免安装版**选一个即可**，不用下载整个仓库或所有 ZIP：

| 文件 | 选择方式 |
| --- | --- |
| [OCCAT-Live-Caption-0.1.9-windows-x64-setup.exe](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.9/OCCAT-Live-Caption-0.1.9-windows-x64-setup.exe) | 安装版，统一提供简体中文 / 繁體中文 / English / 日本語 / 한국어 |
| [OCCAT-Live-Caption-0.1.9-windows-x64-portable.zip](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.9/OCCAT-Live-Caption-0.1.9-windows-x64-portable.zip) | 免安装版，完整解压后运行 `OCCATLiveCaption.exe` |
| [SHA256SUMS.txt](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.9/SHA256SUMS.txt) | 可选，用于核对本版 Windows 附件 |
| `CorrespondingSources-*.zip`、`Sources-Sherpa-ASR-*.zip`、`OCCAT-Live-Caption-0.1.9-Third-Party-Notices.zip` | 第三方对应源码与许可材料，普通运行无需逐个下载 |

1. 使用 **Windows 10/11 x64**，并具备 Microsoft Visual C++ x64 运行库 **14.44.35211 或更新版**。安装器发现运行库缺失或过旧时，会在确认后从微软官方下载、校验签名并打开安装界面。请按提示确认微软许可及管理员授权，完成后自动继续字幕安装；需要联网，不会自动重启。微软提示必须重启时，请保存工作、自行重启，再运行字幕安装器。免安装版同样需要先具备运行库。
2. 安装版双击 EXE，选择简体中文、繁體中文、英文、日文或韩文并按向导完成；免安装版请完整解压后启动，不要单独取出 EXE。安装包没有商业代码签名，请核对下载来源与 SHA-256。
3. 启动“猫猫本地实时字幕”，选择实际播放声音的系统设备或麦克风。新用户默认使用 **Whisper large-v3-turbo**，首次使用需联网下载约 **1.6 GB** 并完成校验；下载支持续传和下载源回退，完整缓存后优先本地加载，可断网使用。其他 8 个识别模型按需下载，也可导入兼容本地模型；升级不覆盖已有模型选择。
4. 需要翻译时，在“识别与翻译”下载或导入兼容的 **M2M100** 模型，再开启“实时翻译”；只看原文时保持关闭。
5. 在“字幕外观”调整字幕样式，在“窗口与待机”调整位置、穿透和待机方式。底部语言菜单支持简体中文、繁體中文、English、日本語、한국어，识别语言单独设置。中日韩字幕字形在“字幕外观 → 识别原文 · 文字”设置，不随界面语言切换。

本版的软件版本号为 **0.1.9**，发布标签为 **`v0.1.9`**，仍按预发布版本提供。**本版的软件内更新支持公开预览版。0.1.5 及更早版本仍只查询旧的 latest 接口，需先手动安装一次 0.1.6 或更新版；之后可在软件内检查并更新。** 旧分语言安装包用户可手动升级到上面的统一安装包；繁體中文、日文、韩文安装向导保留已审阅的英文组件条款原文。

按用户安装，已有设置优先。安装版和免安装版均把设置、下载模型和字幕记录保存到 `%LOCALAPPDATA%/OCCATLiveCaption`，卸载保留用户数据；免安装版不会把设置放在解压目录里。

**从旧版升级：** 已有模型选择与其他设置会保留。如果升级后仍显示 Base，请到“识别与翻译 → 识别引擎 → 识别模型”选择 `large-v3-turbo`，再点击“应用并重载模型”，即可下载并使用 Turbo；新用户默认选择 Turbo。

## macOS 预览版下载

**Mac 0.1.9 已提供 Apple 芯片与 Intel 原生预览包。** 两种架构均完成云端 macOS 构建、冻结界面与 CPU 识别测试，并在本机独立核验。实体 Mac 的麦克风与系统收音仍需用户实测。

**需要 macOS 14 或更新版本。** 按处理器选择一个 DMG：

| Mac 类型 | 下载 |
| --- | --- |
| Apple 芯片（M1 及更新机型） | [OCCATLiveCaption-0.1.9-macOS-arm64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.9/OCCATLiveCaption-0.1.9-macOS-arm64.dmg) |
| Intel | [OCCATLiveCaption-0.1.9-macOS-x86_64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.9/OCCATLiveCaption-0.1.9-macOS-x86_64.dmg) |

打开 DMG，将应用拖到“应用程序”。此预览包采用 **ad-hoc 签名，未经 Apple 公证**；首次尝试打开后，macOS 可能要求在“系统设置 → 隐私与安全性”对该应用选择“仍要打开”。请使用同版 Release 的 [SHA256SUMS-macOS.txt](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.9/SHA256SUMS-macOS.txt) 核对 Mac 附件。后续更新在 Mac 版中打开 Releases 下载页，下载新 DMG 并替换应用；设置、模型和字幕记录保存在 `~/Library/Application Support/OCCATLiveCaption`。

Mac 版使用 **CPU 推理**，新用户仍默认首次下载 **large-v3-turbo（约 1.6 GB）**，不内置模型，也不会自动改选 Base；其他模型按需下载。大模型在 CPU 上的速度取决于硬件，预览包不保证实时性能。

声音来源使用 CoreAudio 输入，开始采集时需允许麦克风权限。播放中的系统声音需要自行安装并配置 **BlackHole 等虚拟输入**，软件不捆绑或安装音频驱动。步骤见 [macOS 声音来源设置](docs/macos-audio.md)。

两种架构在原生 CI 中检查了冻结应用的 Cocoa 界面、字幕与字体、进程回收和 HTTPS 证书验证；另以运行时临时生成的 `say` 语音和 `tiny.en` 完成真实 CPU 识别。该夹具不代表 Turbo 的性能或准确率。**实体 Mac 的麦克风授权与采集、BlackHole 系统声音、长期运行，以及多桌面 Spaces／全屏置顶仍未完成验收。** 组件许可和共享库替换说明在应用包内，对应第三方源码附件见同版 Release。

Mac 预览包内置思源黑体、思源宋体及日语／韩语地区思源字体，其他字体可从本地导入。

## 自定义主题示例

![自定义主题、玻璃材质与导航预览](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.6/custom-theme-example-2562eb7803b4b4bf.png)

这是用户提供的自定义主题截图预览。在“页面外观”选择“自定义”后，可以自行设置背景图片；原始壁纸不随安装包分发。

## 验证范围与使用说明

Windows 0.1.9 已通过原文与译文独立样式、配置迁移、界面语言及字幕渲染回归检查，冻结程序检查、五种安装语言的隔离安装／启动／卸载，以及真实 0.1.8 → 0.1.9 含空格自定义目录覆盖升级。升级保留配置与模型校验样本，文件版本为 **0.1.9.0**。翻译生命周期检查使用合成译文交付，并非本轮真实 M2M100 推理。以上不等同于干净 Windows、现场音频或全部硬件实测。

**尚未在缺少运行库的干净 Windows 环境实测，仍属于预发布版本。** 我没有把这些检查当作所有 GPU、多屏、音频设备和系统组合的保证。

识别和翻译在本机执行；首次识别模型下载、按需翻译模型下载和更新检查会联网，模型完整缓存后可在本地使用。**默认保存本地字幕文本**，可在高级设置关闭，关闭不会删除旧记录。个人背景图片、自行导入的模型和字体不随官方安装包发布。

字幕和翻译可能有误，重要内容请人工核对；这是辅助阅读工具，不替代专业无障碍服务或正式记录。请只处理有权使用的内容，采集他人发言前取得必要授权。

## 许可与公开范围

本下载仓库文档及我自己的代码采用 [MIT](LICENSE)，署名 **OCCAT**。**应用开发源码仓库保持 Private；这个公共仓库提供软件下载与分发材料，不表示全部应用源码已经公开。**

安装包并非整套 MIT。导航与窗口控件使用 [Feather v4.29.0 官方图标](https://github.com/feathericons/feather/tree/v4.29.0)，其 [MIT 原始许可](https://github.com/feathericons/feather/blob/v4.29.0/LICENSE) 随安装包和同版通知归档提供。四种界面字体、Whisper 模型（按需下载）、Qt、FFmpeg/PyAV、Sherpa ASR、Intel/NVIDIA 等保留各自适用的许可和组件条款；字体的原始许可也随本版通知归档提供。 新增的日语、韩语地区思源黑体保持 Adobe 官方原版，采用 SIL Open Font License 1.1，原始许可随同版材料提供。

同版 Release 附第三方对应源码、构建材料、原始版权通知和校验清单。入口见[第三方许可说明](THIRD_PARTY_NOTICE_PUBLIC.md)与[共享库修改/替换指引](LIBRARY_REPLACEMENT.zh-CN.md)；适用的 LGPL 修改、替换及必要调试权利保持不变。公开附件不包含自有应用 Source.zip、构建报告或用户数据。

欢迎在 [Issues](https://github.com/occat666/occat-live-caption-download/issues) 反馈，附候选版本、系统、模型和复现步骤，提交前请删除私人目录、账号、录音与真实对话内容。

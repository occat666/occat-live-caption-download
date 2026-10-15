# 同版 Qt、FFmpeg 与 PyAV 库的修改与替换

适用版本：猫猫本地实时字幕 0.1.0 RC15 对应二进制。本说明是该发行版本的公开补充说明，纠正旧候选文档中资源与路径描述；原始第三方许可、源码归档与二进制字节保持原样。

本发行采用可替换共享库方式。Qt 采用 LGPLv3；本版实际重建 FFmpeg 采用 LGPL-2.1-or-later。项目 MIT 与指定 Intel/NVIDIA 组件条款不限制接收者修改、替换这些开源库，以及为调试这些修改进行必要逆向工程的权利。自有应用源码仓库保持 Private，取得 Private 应用源码不是就地替换库的前提；Public 仓库是软件下载仓库，不宣称已经公开全部应用源码。

## 准确资源与通知

在同一 Release 下载 `CorrespondingSources-Qt-6.11.2.zip` 和 `CorrespondingSources-FFmpeg-PyAV.zip`。它们提供准确版本源码、原通知、构建材料和现有 DLL 名称映射。不能用上游主页链接或另一版源码代替。

安装器与 portable 内的实际许可位置是 `_internal/licenses/qt/upstream/`、`_internal/licenses/ffmpeg-8.1.3/` 和 `_internal/licenses/pyav-18.1.0/`。本版安装目录 `docs/QT_RUNTIME_REPLACEMENT.md` 已修正 `_internal/` 路径。本版安装说明明确自有应用源码保持 Private；本次公开提供第三方对应源码和共享库替换材料，自有应用源码仍在 Private 仓库。

## Qt 运行库

1. 完全退出应用，备份整个安装目录或 portable 目录。
2. Qt/PySide6 运行文件位于 `_internal/PySide6/`；Shiboken 位于 `_internal/shiboken6/`。它们是 onedir 中的独立 DLL/PYD，替换不要求修改主 EXE、维护者签名或激活。
3. 以 Qt 对应源码归档内 `BUILDING-Qt-6.11.2.md` 和上游脚本为准，使用 Windows x64 Release、兼容 Qt 6.11/PySide6 6.11 与本发行 Python ABI 的一整组构建文件。Core/Gui/Widgets、平台/图片插件以及受影响的 PySide6/Shiboken 绑定应保持一致，避免不同架构和 Debug/Release 混用。
4. 将相应 DLL/PYD、插件及绑定作为一致组替换，启动后检查窗口、文字、图片与交互。发生问题时退出并恢复备份。Qt Base、Image Formats、Translations、PySide6/Shiboken 的准确源码及未修改说明均在对应归档内。

## FFmpeg / PyAV 运行库

1. 完全退出并备份应用目录。实际位置为 `_internal/av.libs/` 的七个 FFmpeg DLL，以及 `_internal/av/` 中引用它们的 PyAV `.pyd` 扩展。
2. 使用对应源码归档中的原始 FFmpeg 8.1.3 与 PyAV 18.1.0 源码、`build/` 构建配置、工具和无补丁说明。`build/tools/build_lgpl_native.py` 可以重建共享库和相关 PyAV 构建，并生成可选 native SDK；“SDK”是重建输出，不是本次另行上传的现成发行附件。
3. 查看 `build/library-name-map.json`。冻结的 PyAV 扩展与 FFmpeg DLL 导入表引用修复后的 DLL 名称。不能只把新 wheel 的新哈希文件名复制进去；须保持映射的名称、Windows x64 架构、发行 Python ABI、FFmpeg ABI 和所有库间导入一致。必要时同时重建并处理 PyAV 扩展及完整 FFmpeg DLL 组。单纯重命名文件不自动修改依赖导入表。
4. 就地替换一整组兼容库和受影响的扩展，不要求重建完整应用或取得 Private Python 源码。归档两份旧 `LIBRARY_REPLACEMENT.md` 对“supplied MIT application source”“separately supplied native SDK”的描述，以本说明所列实际 Public 资源和可选重建输出为准。
5. 启动后检查音频解码、重采样、实际音源识别、暂停恢复及退出。遇到兼容性问题，退出后恢复备份；不要复制 Windows 系统 DLL 来代替用户库。

发行核对中的哈希用于确认原始产物，不阻止用户合法修改 LGPL 库后运行。自行使用与对外再分发修改版的义务不同；再分发修改后的库时，需要提供该修改版准确源码、补丁、所需构建材料和适用通知。此指南不是“修改后的库替换运行已通过”的测试记录；该操作未在本次材料审阅中实际执行。

依据：[GNU LGPLv3 §4d1](https://www.gnu.org/licenses/lgpl-3.0.html)、[FFmpeg 官方发行检查](https://ffmpeg.org/legal.html)。

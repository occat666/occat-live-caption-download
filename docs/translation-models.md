# 本地翻译模型

本版本保留 Whisper / faster-whisper 的语音识别，文字翻译改用 **M2M100 418M INT8 + CTranslate2 + SentencePiece**。识别模型负责把声音变成原文，翻译模型负责把原文译成所选目标语言；它们有各自的模型选择入口，不互相替代。

## 用户操作

1. 打开“识别与翻译”，在“实时翻译”区域点击“下载推荐翻译模型”。下载的是已经转换的 INT8 模型，用户不需要安装 Python 转换工具、PyTorch 或 Transformers。
2. 等待下载、文件校验完成。下载与校验在后台执行；失败会显示原因，原文识别和已有有效模型不应被失败的结果覆盖。
3. 打开“实时翻译”。在“翻译目标”选择 **中文（简体）、中文（繁体）、英文、日文或韩文**。中、英、日、韩可相互翻译，一个模型即可；同语种直接显示，中文简繁由本地 OpenCC 转换，不重复运行模型。
4. 希望保留原文时打开“同时显示原文”，并将字幕设为两行。关闭翻译后，该原文选项暂不可操作，但保留显示偏好。

下载需要联网，可在“模型下载与管理…”选择自动、官方源或镜像源，并使用系统代理、直接连接或自定义 HTTP/HTTPS 代理。自动模式会在连接失败后切换来源和连接方式；部分文件会保留供下次继续下载。模型完整保存在本机后，翻译不依赖远程接口；下载或校验失败时，原文字幕仍可使用。初次下载需约 496 MB 模型文件，加上许可和清单等小文件；下载临时文件、模型加载所需内存与这一磁盘大小不同。推理速度取决于硬件、句子长度和识别/翻译同时运行的负载，不能由 INT8 或模型文件大小推导固定延迟。

## 导入已准备好的离线包

在同一区域点击“导入本地翻译模型”，选择已解压的完整模型目录。需要选择模型目录本身，不是单独的 `model.bin`。成功校验后，选择保存到 `config.json` 的 `translation_model_path`；权重仍需保留在所选目录，移动或删除后会提示模型不可用。

本入口只支持本程序定义的 **M2M100 CTranslate2 完整包**。目录应包含：

| 文件 | 用途 |
| --- | --- |
| `model.bin` | CTranslate2 INT8 权重 |
| `config.json` | CTranslate2 模型配置 |
| `shared_vocabulary.json` | 共享词表 |
| `sentencepiece.bpe.model` | 对应的 SentencePiece 分词器 |
| `LICENSE.txt` | 模型 MIT 许可全文与版权声明 |
| `README.upstream.md` | 上游来源和转换说明 |
| `translation-model.json` | 架构、源/目标语言、来源版本和上述六个文件的 SHA-256 |

缺少文件、哈希不符、语言或架构不匹配会拒绝导入。清单校验提供格式与完整性检查，不是对任意来源模型的安全或授权保证；仅导入可信来源的模型。推荐下载保存到 `models/translation/m2m100-418m-int8`；命令行等效入口为 `download_models.py translation`，`m2m100` 是别名。

下列文件不能直接作为翻译模型导入：

- Whisper 识别模型，即使同样带有 `model.bin`。
- 原始 PyTorch `.bin` / `.pt` / `.pth` / `.safetensors` 权重。
- NLLB、Marian/OPUS、GGUF 大语言模型或其他架构的 ONNX 模型。
- 旧 `.argosmodel` 语言包或 Stanza 分句模型。

其他开源模型须先确认许可，再由开发者实现对应后端、分词与校验逻辑；“开源”不意味着文件格式和推理接口通用。

## 推荐包来源与版本

| 项目 | 来源与状态 |
| --- | --- |
| 原始模型 | [facebook/m2m100_418M](https://huggingface.co/facebook/m2m100_418M)，官方模型卡为 MIT，包含 en、ja、ko、zh |
| 预转换模型 | [gn64/M2M100_418M_CTranslate2](https://huggingface.co/gn64/M2M100_418M_CTranslate2)，发布者模型卡明示 M2M100 418M INT8 与 MIT |
| 预转换包固定版本 | `18e406c615ef2991fa74d53734bf66b0a6b10cb4`，下载后逐文件核对 SHA-256 |
| 开发者重新转换的原模型固定版本 | `55c2e61bbf05dfb8d7abccdc3fae6fc8512fd636`；这是本项目选择的可复现来源，不等于预转换发布者证明使用了同一版本 |
| Runtime | [CTranslate2](https://github.com/OpenNMT/CTranslate2/blob/v4.8.2/LICENSE) 为 MIT；[SentencePiece](https://github.com/google/sentencepiece/blob/v0.2.2/LICENSE) 为 Apache-2.0。按最终安装版本保留许可和内含组件声明 |

预转换发布者未明确记录当时转换所用的原模型提交、转换器版本和完整命令。本项目固定下载包的版本与文件内容，记录这一来源限制；不能将本次原模型固定版本反向写成上游转换事实。正式发行时，随模型保留来源、原许可及转换说明，项目自身 MIT 声明不能代替这些材料。

2026-10-10 已使用上述原模型固定版本独立重新转换：CTranslate2 4.8.2、Transformers 4.57.6、Torch 2.14.0 CPU，隔离环境为 `_dev/conversion-deps`。生成的 `model.bin` 与推荐包逐字节一致，SHA-256 都为 `a1826980fc5c037e69c7ac94fcb56c03001a66f380eb71863cc0a3879e71421b`；SentencePiece 分词模型的哈希也一致。这支持独立复现权重与分词器，不证明发布者当时使用的提交或命令。配置与词表 JSON 的内容也已比对一致，仅序列化格式不同。最终发行附件仍需单独核验。

## 开发者转换

终端用户使用准备好的包。开发者若需重新生成包，可在项目根目录创建隔离环境并运行：

```powershell
python -m venv _dev/m2m-converter
.\_dev\m2m-converter\Scripts\python.exe -m pip install -r requirements-conversion.txt
.\_dev\m2m-converter\Scripts\python.exe -m pip check
.\_dev\m2m-converter\Scripts\python.exe -X utf8 tools/convert_translation_model.py --output models/translation/custom-pack
```

`--output` 必须是尚不存在的新目录；工具会拒绝覆盖已有目录，避免损坏当前模型。重新转换会下载原始权重并创建缓存和临时目录，所需磁盘空间大于最终 INT8 包。转换器固定原模型提交并校验源文件，生成权重、分词器、语言与来源清单、许可和 SHA-256，不执行远程自定义模型代码。完成后先验证真实加载、源语言标记及各目标前缀，再用软件的翻译模型导入入口选择新目录。

PyTorch 与 Transformers 是转换工具依赖，不应因此进入软件的翻译运行时或默认安装环境。本次另建的 `_dev/m2m100-runtime` 安装验证中，未安装 Argos、MiniSBD、Stanza、PyTorch 或 Transformers，`pip check` 通过；这与保留作回退的旧 `.venv` 是两个不同环境。

[CTranslate2 的 M2M100 指引](https://opennmt.net/CTranslate2/guides/transformers.html#m2m-100)要求正确的源语言标记和目标语言前缀；不使用 Hugging Face tokenizer 时，必须显式处理所需特殊标记。只把目录换成 M2M100 权重并不足以实现可靠翻译。

## 多语言目标与旧包兼容

0.1.19 的翻译目标独立保存为 `translation_target`；缺失时默认中文（简体），旧配置明确选择中文（繁体）时保留该显示偏好。切换目标不重新下载或加载模型，缓存与待处理结果按目标隔离。

推荐包的旧清单虽然仅声明英、日、韩译中，其共享词表已包含 `__zh__`、`__en__`、`__ja__`、`__ko__`，程序核验后复用。导入包按实际词表与模型格式判断能力，缺少语言标记的方向不会被报告为可用。中文简繁共用 `__zh__`，通过目标显示转换区分；日、韩目标使用对应字形，不受原文简繁设置影响。

## 已执行的推理检查

2026-10-10 使用 18 条人工编写的短句，英文、日文、韩文各 6 条，每条清空缓存后运行 2 次，最终运行参数为 `beam_size=4`；未使用真人对话或用户字幕。测试对象是已准备的推荐模型与本机翻译后端，不包含录音、Whisper 识别或同时进行游戏/识别的完整负载。

| 环境 | 加载时间 | 首次预热 | 36 次翻译耗时中位数 | 单次最大耗时 |
| --- | --- | --- | --- | --- |
| Ryzen 5 9600X，CPU INT8 | 0.707 秒 | 0.104 秒 | 0.137 秒 | 0.229 秒 |
| RTX 5070，CUDA `int8_float16` | 0.859 秒 | 0.235 秒 | 0.099 秒 | 0.153 秒 |

两条测试路径均加载成功，CUDA 测试未发生 CPU 回退。运行脚本为 `tools/benchmark_translation.py`；本机原始结果保存在内部交付目录，不作为公开用户资料上传。本表复测前显卡已有内核缓存；初次冷启动测得 GPU 预热约 2.816 秒，明显长于后续短句翻译。模型加载和推理都由后台线程处理。

三种语言的普通短句可以生成可读中文，但这不是专业质量评测或所有硬件的实时承诺：英文 “space bar” 仍出现“空间栏”，日文对应词出现“空间键”。初测韩文“村庄”被译成“城”，调整解码参数后改善；真实测试音频中的 “live caption” 仍可能被译成“直播标签”。游戏术语、专有名词、长句和识别错误仍会影响译文；重要内容应核对原文。另在全新运行环境通过了本地英语语音文件 → Whisper 识别 → M2M100 中文翻译测试，Tk、Qt 和字体检查通过。该测试跳过系统声音捕获；尚未证明低配电脑、完整实时采集到浮层的时延或连续高负载性能。

## 升级与回退

安装版可在软件内检查并安装更新；升级前先退出字幕程序，安装后保留已有用户配置与本地模型。macOS 下载对应芯片的新版，替换“应用程序”中的旧应用。

如新版不适用于当前设备，可从 [0.1.19 发布页面](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.19) 下载上一版。回退前退出程序并备份用户配置；旧版可能不识别新版新增设置。保留原有模型目录，不要在回退过程中删除权重。

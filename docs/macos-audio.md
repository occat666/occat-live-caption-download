# macOS 声音来源设置（预览版）

Mac 预览版要求 macOS 14 或更新版本，Apple 芯片与 Intel 分别下载对应 DMG。
下载入口与已完成的验证范围见[项目主页](../README.md#macos-预览版下载)。
此包采用 ad-hoc 签名，未经 Apple 公证。实体 Mac 的首次麦克风授权、设备采集、
BlackHole 路由、长期运行及 Spaces／全屏应用置顶仍未完成验收。

## 麦克风及其他输入

Mac 版读取 CoreAudio 输入。选择内置麦克风、耳机麦克风、USB 音频接口或已安装的
虚拟输入。开始字幕时需要允许麦克风权限；如果曾拒绝，请在「系统设置 → 隐私与
安全性 → 麦克风」允许本应用，再重新开始字幕。虚拟输入也需要该权限。

「系统默认输入（自动跟随）」跟随 macOS 的默认输入，通常是麦克风。它不会直接
读取普通扬声器正在播放的声音。

## 读取播放中的系统声音

需要用户自行安装并设置 BlackHole 等虚拟输入。字幕软件不捆绑或自动安装音频
驱动；请从 [BlackHole 官方项目](https://github.com/ExistentialAudio/BlackHole)取得与系统兼容的版本。

1. 安装 BlackHole 2ch 后，打开 macOS「音频 MIDI 设置」。
2. 创建「多输出设备」，同时勾选实际使用的耳机／扬声器与 BlackHole 2ch。
3. 按设备要求设置一致的采样率；对非主时钟设备启用漂移校正，设备顺序等要求见
   [BlackHole 官方多输出设置](https://github.com/ExistentialAudio/BlackHole/wiki/Multi-Output-Device)。
4. 在「系统设置 → 声音 → 输出」选择该多输出设备。
5. 在字幕软件选择实际列出的 BlackHole 2ch 输入，然后播放需要识别的内容。

只把输出设为 BlackHole，可能导致你听不到播放声音；多输出设备用于同时送到
真实耳机／扬声器和虚拟输入。不同设备的实际兼容性仍需在你的 Mac 上检查。

## 模型、设置与验证范围

Mac 使用 CPU 推理，新用户默认仍是 large-v3-turbo，首次需联网下载约 1.6 GB，
其他模型按需下载。已有 CUDA 或自动 GPU 首选项按 CPU 运行，同时保留模型选择。
大型模型的 CPU 速度取决于硬件，预览版不保证实时性能。

设置、模型和字幕记录保存在 `~/Library/Application Support/OCCATLiveCaption`。
更新入口打开 Releases 下载页；下载新 DMG 并替换应用，不需删除该用户目录。

原生 CI 的冻结应用检查覆盖 Cocoa 界面、字幕和字体、进程回收、HTTPS 证书验证，
另以临时生成的 `say` 语音和 tiny.en 做一次真实 CPU 识别。这个测试不代表 Turbo
的性能或准确率，也没有完成实体 Mac 的麦克风、系统声音与长期使用验收。

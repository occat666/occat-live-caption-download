# macOS 声音来源设置（适配验证草稿）

**macOS 适配正在验证，目前没有可下载的 Mac 安装包。** 原生构建尚待工作流运行授权并完成后续验证，以下流程用于说明已准备的音频适配方案，不代表 Mac 端已经完成安装、权限或真实设备验收。将来如发布经过验证的安装包，应以对应 Release 的系统要求、下载链接和验证范围为准。

[简体中文](../README.md) · [繁體中文](../README.zh-TW.md) · [English](../README.en.md) · [日本語](../README.ja.md) · [한국어](../README.ko.md)

适配方案使用 CoreAudio 音频输入。内置麦克风、耳机麦克风、USB 音频接口及虚拟输入的实际兼容情况仍需真机验证。首次开始字幕时需要允许软件访问麦克风；若曾拒绝，可在“系统设置 → 隐私与安全性 → 麦克风”中调整后重新开始。BlackHole 等虚拟输入也需要此权限。

“系统默认输入（自动跟随）”拟跟随 macOS 的输入设置，通常是麦克风。它不能直接获取普通扬声器正在播放的声音。SoundCard 的 CoreAudio 后端只提供实际输入，不能沿用 Windows 扬声器环回方式。

## 系统声音的拟用设置流程

以下步骤适用于将来获得并完成验证的 Mac 应用，也可用于理解虚拟音频路由。BlackHole 由用户自行决定是否安装；字幕软件不捆绑或自动安装该驱动。

1. 从 [BlackHole 官方项目](https://github.com/ExistentialAudio/BlackHole)了解并安装 BlackHole 2ch，重新打开音频应用。
2. 打开“应用程序 → 实用工具 → 音频 MIDI 设置”，点击左下角 `+`，选择“创建多输出设备”。
3. 同时勾选 BlackHole 2ch 和实际使用的耳机或扬声器，将耳机或扬声器设为时钟源，对 BlackHole 开启漂移校正，并保持各设备采样率一致。
4. 在 macOS“系统设置 → 声音 → 输出”中选择该多输出设备。
5. 在完成适配验证的字幕软件中，将声音来源选为 **BlackHole 2ch（系统声音输入）**，再播放需要识别的内容。

多输出设备会同时把声音送到实际耳机或扬声器和 BlackHole。若仅将 BlackHole 设为系统输出，声音只会进入虚拟设备，你可能听不到播放内容。完成后可将系统输出切回原耳机或扬声器。更换耳机时，也要调整多输出设备。详见 [BlackHole 官方多输出设备指南](https://github.com/ExistentialAudio/BlackHole/wiki/Getting-Started%3A-Creating-a-Multi-Output-Device)。

## 模型、设置与待验证项目

已准备的 Mac 运行配置使用 CPU，默认模型仍为 large-v3-turbo，已有 CUDA 或自动 GPU 首选项按 CPU 处理并保留模型选择。计划将设置、下载模型与字幕记录保存在 `~/Library/Application Support/OCCATLiveCaption`，应用更新不应覆盖该用户目录。最终行为需以真实安装包验证为准。

待完成的 Mac 验收包括：两种架构的原生构建与应用启动、模型推理、首次麦克风授权与拒绝后恢复、内置及外接输入、BlackHole 路由、真实系统声音采集和长时间运行。Windows 版的历史验证不覆盖这些项目。

开发依据：[SoundCard 0.4.6 CoreAudio 实现](https://github.com/bastibe/SoundCard/blob/0.4.6/soundcard/coreaudio.py#L30-L41)、[Qt 权限说明](https://doc.qt.io/qt-6/permissions.html)、[Apple 麦克风用途声明](https://developer.apple.com/documentation/bundleresources/information-property-list/nsmicrophoneusagedescription)。应用包需要麦克风用途说明，启用 hardened runtime 签名时也需音频输入 entitlement。

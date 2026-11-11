# 猫猫本地实时字幕 / Maomao Local Live Captions

[简体中文](README.md) · [繁體中文](README.zh-TW.md) · [English](README.en.md) · **日本語** · [한국어](README.ko.md)

システム音声やマイクの音声をローカルで認識し、フローティング字幕やリアルタイム履歴として表示するツールです。オフライン翻訳にも対応しています。

## ダウンロード

現在のバージョンは [0.1.28 公開テスト版](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.28)です。Windows はどちらか一方、Mac はプロセッサに対応するファイルを選択してください。

| 種類 | ファイル |
| --- | --- |
| Windows インストーラー | [OCCAT-Live-Caption-0.1.28-windows-x64-setup.exe](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.28/OCCAT-Live-Caption-0.1.28-windows-x64-setup.exe) |
| Windows ポータブル版 | [OCCAT-Live-Caption-0.1.28-windows-x64-portable.zip](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.28/OCCAT-Live-Caption-0.1.28-windows-x64-portable.zip) |
| Mac · Apple シリコン | [OCCATLiveCaption-0.1.28-macOS-arm64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.28/OCCATLiveCaption-0.1.28-macOS-arm64.dmg) |
| Mac · Intel | [OCCATLiveCaption-0.1.28-macOS-x86_64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.28/OCCATLiveCaption-0.1.28-macOS-x86_64.dmg) |

[Windows SHA-256](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.28/SHA256SUMS.txt) · [macOS SHA-256](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.28/SHA256SUMS-macOS.txt) · [Releases](https://github.com/occat666/occat-live-caption-download/releases)

## 主な機能

- フローティング字幕とリアルタイム履歴を切り替え、過去の字幕の確認やコピーが可能。
- 中国語（簡体字／繁体字）、英語、日本語、韓国語の表示と相互翻訳に対応。認識可能な言語はモデルによって異なります。
- 原文と訳文のフォント、色、縁取り、影、背景を個別に調整。
- 認識と翻訳は端末内で実行。モデルのダウンロードと更新確認には通信が必要で、モデルの取得完了後はオフラインで使用可能。

## 使い方

1. Windows はインストーラーを実行するか、ZIP を完全に展開して `OCCATLiveCaption.exe` を起動します。Mac は DMG 内のアプリを「アプリケーション」に移動します。
2. 再生中の音声デバイスまたはマイクを選び、認識モデルをダウンロードします。既定の Whisper large-v3-turbo は約 1.6 GB です。別のモデルも選択できます。
3. 翻訳を使う場合は M2M100 モデルをダウンロードまたはインポートし、翻訳先言語を選択して翻訳を有効にします。

**Windows:** Windows 10/11 x64、Visual C++ x64 ランタイム 14.44.35211 以降が必要です。インストーラーが確認し、導入を案内します。

**macOS:** macOS 14 以降が必要です。プレビュー版は CPU 推論を使用し、Apple の公証は未取得です。システム音声の取得には BlackHole などの仮想入力が必要です。[Mac 音声設定](docs/macos-audio.md)を参照してください。

## 説明とフィードバック

[使い方（中国語）](docs/USER_GUIDE.zh-CN.md) · [更新履歴・旧バージョン](https://github.com/occat666/occat-live-caption-download/releases) · [不具合報告](https://github.com/occat666/occat-live-caption-download/issues)

字幕テキストは既定でローカル保存され、字幕設定で無効にできます。認識や翻訳には誤りが生じるため、重要な内容は確認してください。

作者：OCCAT。このリポジトリは配布物を提供し、アプリの開発ソースは非公開です。独自のコンテンツは [MIT](LICENSE)、同梱コンポーネントやフォントは各ライセンスに従います。[第三者ライセンス](THIRD_PARTY_NOTICE_PUBLIC.md)と[共有ライブラリの差し替え手順](LIBRARY_REPLACEMENT.en.md)を参照してください。

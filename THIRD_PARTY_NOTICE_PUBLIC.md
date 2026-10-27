# Public download license notice / 公开下载许可说明

Maomao Local Live Captions uses Qt under LGPLv3 and the exact rebuilt FFmpeg under LGPL-2.1-or-later, with PyAV under its own BSD terms. Corresponding source/build resources and original notices are separate same-version Release assets. See `LIBRARY_REPLACEMENT.zh-CN.md` or `LIBRARY_REPLACEMENT.en.md` for the replaceable shared-library route and corrected installed paths.

OCCAT 自有代码使用 MIT，保持 Private 源码仓库；Public 仓库仅提供软件下载和分发材料。第三方运行库、识别模型、字体与厂商材料保持其原有许可，不能将整个安装包统称为 MIT。适用的修改、替换和必要调试权利不受指定厂商组件条款限制。

Same-version source assets / 同版第三方源码附件：

- `CorrespondingSources-Qt-6.11.2.zip`
- `CorrespondingSources-FFmpeg-PyAV.zip`
- `CorrespondingSources-Rust-MPL.zip`
- `CorrespondingSources-tqdm-4.70.1.zip`
- `Sources-Sherpa-ASR-1.13.8.zip`

For Windows, original notices are retained in the application's `_internal/licenses/` and this notice bundle. Qt notices are under `_internal/licenses/qt/upstream/`; FFmpeg/PyAV notices are under `_internal/licenses/ffmpeg-8.1.3/` and `_internal/licenses/pyav-18.1.0/`. Upstream authors' copyright names and license contact information remain intact.

Microsoft Visual C++ x64 Redistributable is obtained directly from Microsoft and is not bundled with these 0.1.9 installers or these public materials. Windows repair images, Microsoft installation media, testing fixtures, personal audio, private configuration and the application's own main Source.zip are excluded.

0.1.9 uses one installer with Simplified Chinese, Traditional Chinese, English, Japanese and Korean UI. The Qt 6.11.2 corresponding-source archive includes qttranslations sources for the bundled Chinese/Japanese/Korean translation resources; the Traditional Chinese page copy ships with the application itself. Traditional Chinese, Japanese and Korean setup use the reviewed original English component terms.

Windows 0.1.9 provides HarmonyOS Sans, MiSans, Source Han Sans and Source Han Serif with 30 original weight files, plus the original Japanese and Korean regional Source Han Sans variable files under SIL Open Font License 1.1. Their original font licenses are included under _internal/bundled_assets/ in the notice archive and application. Other fonts are downloaded and imported by the user.

0.1.9 draws navigation and window-control glyphs from the unmodified official Feather v4.29.0 SVG set. The 13 original SVG files, their source manifest and SHA-256 values, and the original MIT license are included under _internal/licenses/feather/ in the notice archive and the installed application. Feather icons are rendered as Qt vector paths at runtime; no network icon loading or additional icon runtime is added.

0.1.9 does not bundle an ASR model by default. New users download and verify Whisper large-v3-turbo on first use; the other eight recognition models are optional. Downloaded models retain their own model licenses and notices. Upgrades preserve existing model selections and cached files. / 0.1.9 安装包默认不附带识别模型；新用户首次使用下载并校验 Whisper large-v3-turbo，其他八个识别模型按需下载。下载模型保留各自许可与通知，升级保留已有选择与缓存。

## macOS preview components

These Mac materials apply to the published **0.1.9** native previews. Both Apple Silicon and Intel artifacts were built and tested on native cloud macOS runners and independently reviewed; the links below are the matching corresponding sources. The application source repository remains private.

The native macOS previews use Qt/PySide6/Shiboken6 6.9.3, including the QtDBus framework required by QtGui. Their original Qt notices come from the matching verified 6.9.3 source archives; the Windows Qt 6.11.2 materials remain separate. The bundled PyAV 18.1.0 uses rebuilt LGPL FFmpeg 8.1.3 shared libraries, and sherpa-onnx is the ASR-only 1.13.8+asr.1 build.

Original installed-wheel licenses, pinned Adobe SC/Serif/JP/KR font licenses, and the Mac shared-library replacement instructions are retained inside OCCATLiveCaption.app/Contents/Resources; package layouts also contain PyInstaller resource links. Mac fonts supplied with this preview are Source Han Sans SC, Source Han Serif SC, and the original Japanese/Korean regional Source Han Sans variable fonts.

Matching same-version Mac corresponding-source assets:

- [CorrespondingSources-Qt-6.9.3-macOS.zip](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.9/CorrespondingSources-Qt-6.9.3-macOS.zip)
- [CorrespondingSources-macOS-arm64.zip](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.9/CorrespondingSources-macOS-arm64.zip)
- [CorrespondingSources-macOS-x86_64.zip](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.9/CorrespondingSources-macOS-x86_64.zip)

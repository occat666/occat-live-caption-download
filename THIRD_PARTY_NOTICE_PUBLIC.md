# Public download license notice / 公开下载许可说明

Maomao Local Live Captions uses Qt under LGPLv3 and the exact rebuilt FFmpeg under LGPL-2.1-or-later, with PyAV under its own BSD terms. Corresponding source/build resources and original notices are separate same-version Release assets. See `LIBRARY_REPLACEMENT.zh-CN.md` or `LIBRARY_REPLACEMENT.en.md` for the replaceable shared-library route and corrected installed paths.

OCCAT 自有代码使用 MIT，保持 Private 源码仓库；Public 仓库仅提供软件下载和分发材料。第三方运行库、识别模型、字体与厂商材料保持其原有许可，不能将整个安装包统称为 MIT。适用的修改、替换和必要调试权利不受指定厂商组件条款限制。

Same-version source assets / 同版第三方源码附件：

- `CorrespondingSources-Qt-6.11.2.zip`
- `CorrespondingSources-FFmpeg-PyAV.zip`
- `CorrespondingSources-Rust-MPL.zip`
- `CorrespondingSources-tqdm-4.70.1.zip`
- `Sources-Sherpa-ASR-1.13.8.zip`

Original notices are retained in the application's `_internal/licenses/` and this notice bundle. Qt notices are under `_internal/licenses/qt/upstream/`; FFmpeg/PyAV notices are under `_internal/licenses/ffmpeg-8.1.3/` and `_internal/licenses/pyav-18.1.0/`. Upstream authors' copyright names and license contact information remain intact.

Microsoft Visual C++ x64 Redistributable is obtained directly from Microsoft and is not bundled with these 0.1.1 installers or these public materials. Windows repair images, Microsoft installation media, testing fixtures, personal audio, private configuration and the application's own main Source.zip are excluded.

0.1.1 uses one installer with Simplified Chinese, Traditional Chinese, English, Japanese and Korean UI. The Qt 6.11.2 corresponding-source archive includes qttranslations sources for the bundled Chinese/Japanese/Korean translation resources; the Traditional Chinese page copy ships with the application itself. Traditional Chinese, Japanese and Korean setup use the reviewed original English component terms.

0.1.1 provides HarmonyOS Sans, MiSans, Source Han Sans and Source Han Serif with 30 original weight files. Their original font licenses are included under _internal/bundled_assets/ in the notice archive and application. Other fonts are downloaded and imported by the user.

0.1.1 draws navigation and window-control glyphs from the unmodified official Feather v4.29.0 SVG set. The 13 original SVG files, their source manifest and SHA-256 values, and the original MIT license are included under _internal/licenses/feather/ in the notice archive and the installed application. Feather icons are rendered as Qt vector paths at runtime; no network icon loading or additional icon runtime is added.

# Modifying and replacing Qt, FFmpeg and PyAV libraries

Scope: the Maomao Local Live Captions 0.1.3 binary artifacts. This supplemental guide corrects resource and path descriptions in the earlier candidate documentation. It does not change the original third-party licenses, source archives or binaries.

This distribution uses replaceable shared libraries. Qt is distributed under LGPLv3; the rebuilt FFmpeg in these artifacts uses LGPL-2.1-or-later. The project's MIT license and identified Intel/NVIDIA component terms do not restrict the applicable rights to modify or replace these open-source libraries, or perform reverse engineering necessary to debug such modifications. The application's own source repository remains Private. Access to that Private source is not a prerequisite for replacing installed shared libraries. The Public repository is a software download repository, not a claim that all application source has been published.

Download `CorrespondingSources-Qt-6.11.2.zip` and `CorrespondingSources-FFmpeg-PyAV.zip` from the same Release. They include the exact library versions, original notices, build materials and the existing DLL filename map. An upstream homepage or a different source version is not a substitute.

The installed license locations are `_internal/licenses/qt/upstream/`, `_internal/licenses/ffmpeg-8.1.3/` and `_internal/licenses/pyav-18.1.0/`. This corrects the omitted `_internal/` prefix in the installed `docs/QT_RUNTIME_REPLACEMENT.md`. The old statement in `docs/RELEASE_0.1.0_RC.md` about supplying the application source with the installer does not describe this Public download channel: the third-party corresponding sources and shared-library replacement materials are public; the application's own source remains Private.

## Qt

Exit the application and back up the installation or portable directory. Qt/PySide6 files are independent DLLs/PYDs under `_internal/PySide6/`; Shiboken files are under `_internal/shiboken6/`. The onedir layout allows replacement without modifying the main EXE, obtaining a publisher signature or activating modified libraries.

Use `BUILDING-Qt-6.11.2.md` and the upstream scripts in the Qt source archive. Build a consistent Windows x64 Release set compatible with Qt 6.11, PySide6 6.11 and the distribution's Python ABI. Replace affected Core/Gui/Widgets libraries, platform/image plugins and PySide6/Shiboken bindings together. Do not mix incompatible architectures, ABI versions or Debug/Release files. Check windows, text, images and interaction after replacement; exit and restore the backup if compatibility fails.

## FFmpeg and PyAV

Exit and back up the application. The seven FFmpeg DLLs are under `_internal/av.libs/`; the PyAV `.pyd` extensions referring to them are under `_internal/av/`.

Use the archive's original FFmpeg 8.1.3 and PyAV 18.1.0 sources, `build/` configuration, tools and no-patch statement. `build/tools/build_lgpl_native.py` can rebuild shared libraries and the related PyAV build and produce an optional native SDK. The SDK is a build output, not an extra prebuilt asset already supplied in this Release.

Follow `build/library-name-map.json`. Frozen PyAV extensions and the FFmpeg import tables refer to repaired DLL names. Copying a new wheel's differently hashed DLL filenames alone is insufficient. Preserve consistent mapped filenames, Windows x64 architecture, Python ABI, FFmpeg ABI and imports between all affected libraries. Rebuild and process the affected PyAV extensions and the complete FFmpeg DLL set when needed. Renaming a file alone does not rewrite an import table.

Replace a compatible library/extension set in place; rebuilding the complete application or obtaining its Private Python source is not required for this route. The two older `LIBRARY_REPLACEMENT.md` copies' references to “supplied MIT application source” and “separately supplied native SDK” are superseded by the actual Public resources and optional build output described here. Check decoding, resampling, real audio recognition, pause/resume and exit; restore the backup if needed. Do not copy Windows system DLLs as replacement user libraries.

Distribution hashes record the original artifacts and must not prevent legitimate modified LGPL libraries from running. Redistributing modified libraries requires the applicable exact modified source, patches, build materials and notices. This guide is not evidence that running a modified-library replacement was tested during the current materials review; it was not.

References: [GNU LGPLv3 §4d1](https://www.gnu.org/licenses/lgpl-3.0.html), [FFmpeg's official distribution checklist](https://ffmpeg.org/legal.html).

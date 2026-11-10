# 猫猫本地实时字幕 / Maomao Local Live Captions

[简体中文](README.md) · [繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · **한국어**

시스템 소리나 마이크 음성을 로컬에서 인식해 화면 자막 또는 실시간 기록으로 표시하는 도구입니다. 오프라인 번역도 지원합니다.

## 다운로드

현재 버전은 [0.1.27 공개 테스트 버전](https://github.com/occat666/occat-live-caption-download/releases/tag/v0.1.27)입니다. Windows는 두 패키지 중 하나를, Mac은 프로세서에 맞는 패키지를 선택하세요.

| 종류 | 파일 |
| --- | --- |
| Windows 설치형 | [OCCAT-Live-Caption-0.1.27-windows-x64-setup.exe](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.27/OCCAT-Live-Caption-0.1.27-windows-x64-setup.exe) |
| Windows 무설치형 | [OCCAT-Live-Caption-0.1.27-windows-x64-portable.zip](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.27/OCCAT-Live-Caption-0.1.27-windows-x64-portable.zip) |
| Mac · Apple Silicon | [OCCATLiveCaption-0.1.27-macOS-arm64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.27/OCCATLiveCaption-0.1.27-macOS-arm64.dmg) |
| Mac · Intel | [OCCATLiveCaption-0.1.27-macOS-x86_64.dmg](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.27/OCCATLiveCaption-0.1.27-macOS-x86_64.dmg) |

[Windows SHA-256](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.27/SHA256SUMS.txt) · [macOS SHA-256](https://github.com/occat666/occat-live-caption-download/releases/download/v0.1.27/SHA256SUMS-macOS.txt) · [Releases](https://github.com/occat666/occat-live-caption-download/releases)

## 주요 기능

- 화면 자막과 실시간 기록을 전환하고 이전 자막을 확인하거나 복사할 수 있습니다.
- 중국어(간체/번체), 영어, 일본어, 한국어 표시 및 상호 번역을 지원합니다. 인식 가능한 언어는 선택한 모델에 따라 다릅니다.
- 원문과 번역문의 글꼴, 색상, 외곽선, 그림자, 배경을 각각 조절할 수 있습니다.
- 인식과 번역은 기기 내에서 실행됩니다. 모델 다운로드와 업데이트 확인에는 인터넷이 필요하며, 모델이 완전히 저장되면 오프라인으로 사용할 수 있습니다.

## 시작하기

1. Windows는 설치 프로그램을 실행하거나 ZIP을 완전히 풀고 `OCCATLiveCaption.exe`를 실행합니다. Mac은 DMG의 앱을 응용 프로그램 폴더로 옮깁니다.
2. 소리가 재생되는 장치 또는 마이크를 선택하고 인식 모델을 다운로드합니다. 기본 Whisper large-v3-turbo는 약 1.6 GB이며 다른 모델도 선택할 수 있습니다.
3. 번역이 필요하면 M2M100 모델을 다운로드하거나 가져온 후 대상 언어를 선택하고 번역을 켭니다.

**Windows:** Windows 10/11 x64와 Visual C++ x64 런타임 14.44.35211 이상이 필요합니다. 설치 프로그램이 확인하고 설치를 안내합니다.

**macOS:** macOS 14 이상이 필요합니다. 미리 보기 버전은 CPU 추론을 사용하며 Apple 공증을 받지 않았습니다. 시스템 소리를 캡처하려면 BlackHole 등의 가상 입력을 설정해야 합니다. [Mac 오디오 설정](docs/macos-audio.md)을 참고하세요.

## 설명 및 의견

[사용 설명서 (중국어)](docs/USER_GUIDE.zh-CN.md) · [변경 기록 및 이전 버전](https://github.com/occat666/occat-live-caption-download/releases) · [문제 보고](https://github.com/occat666/occat-live-caption-download/issues)

자막 텍스트는 기본적으로 로컬에 저장되며 자막 설정에서 끌 수 있습니다. 인식과 번역에는 오류가 있을 수 있으므로 중요한 내용은 직접 확인하세요.

제작자: OCCAT. 이 저장소는 설치 파일과 배포 자료를 제공하며 앱 개발 소스는 비공개입니다. 자체 콘텐츠에는 [MIT](LICENSE)가 적용되며, 포함된 구성 요소와 글꼴은 각각의 라이선스를 따릅니다. [제3자 라이선스](THIRD_PARTY_NOTICE_PUBLIC.md)와 [공유 라이브러리 교체 안내](LIBRARY_REPLACEMENT.en.md)를 참고하세요.

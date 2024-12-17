# GreDot  
**2024-2 한양대학교 ERICA 인간컴퓨터 상호작용**  

## 개요  
**GreDot**은 촉각 그래픽 장치 닷패드에 청각 피드백을 추가해 시각장애인의 글자 학습을 돕는 앱입니다. 자음과 모음의 정확한 배치, 글자 간의 간격 및 기울기와 같은 주요 요소를 평가하고 직관적이면서도 효율적인 학습 경험을 제공하고자 합니다.  

---

## 목차  
1. [설치 방법](#%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95)  
2. [프로젝트 구조](#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B5%AC%EC%A1%B0)  
3. [주요 기능](#%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5)  
4. [실행 방법](#%EC%8B%A4%ED%96%89-%EB%B0%A9%EB%B2%95)  
5. [사용된 도구 및 라이브러리](#%EC%82%AC%EC%9A%A9%EB%90%9C-%EB%8F%84%EA%B5%AC-%EB%B0%8F-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC)  
6. [요구사항](#%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD)  
7. [기여자](#%EA%B8%B0%EC%97%AC%EC%9E%90)  
8. [라이센스](#%EB%9D%BC%EC%9D%B4%EC%84%BC%EC%8A%A4)  

---

## 설치 방법  
1. **Python** 설치 (버전 3.12 이상 권장).  
2. 프로젝트를 클론하거나 다운로드합니다.  
   ```bash
   git clone <repository-url>
   cd GreDot
   ```  
3. 필수 패키지를 설치합니다.  
   ```bash
   pip install -r requirements.txt
   ```  

---

## 프로젝트 구조  
```
.
├── README.md                     # 프로젝트 설명 문서
├── build
│   └── build_qrc.py              # 이미지 리소스 빌드 스크립트
├── requirements.txt              # 필요한 Python 패키지 목록
└── src
    ├── SDK.py                    # 닷패드 SDK 연동 코드
    ├── data                      # 데이터 및 리소스 폴더
    │   ├── images                # 이미지 리소스
    │   ├── py                    # 이미지 및 사운드 처리 코드
    │   │   └── sound             # 사전 사운드 관련 리소스 폴더
    │   │   └── image_process.py  # 이미지 프로세싱 코드
    │   │   └── libs.py           # 라이브러리 및 통합 함수 관리 코드
    │   │   └── sound_live.py     # 실시간 사운드 피드백 코드
    │   └── ui                    # UI 인터페이스
    └── main.py                   # 메인 실행 파일
```

---

## 주요 기능  
1. **닷패드와의 통합**  
   - 닷패드 장치와 상호작용하여 촉각 그래픽을 출력합니다.  

2. **이미지 및 글자 처리**  
   - 이미지 데이터로부터 글자의 간격, 기울기 및 배치를 분석합니다.  

3. **청각 피드백 시스템**  
   - 학습 시 자음과 모음에 대한 청각적 피드백을 제공하여 직관적 학습을 돕습니다.  

4. **사용자 인터페이스 (UI)**  
   - 학습 인터페이스를 통해 사용자의 학습 진행도를 시각화합니다.  

---

## 사용된 도구 및 라이브러리  

### **프로그래밍 언어 및 프레임워크**  
- **Python 3.12**  
- **PySide6**: GUI 개발 및 사용자 인터페이스 구현  
- **Qt for Python**: UI 화면 디자인  

### **데이터 분석 및 처리**  
- **NumPy**: 수치 계산 및 데이터 처리  
- **OpenCV**: 이미지 분석 및 처리  

### **청각 피드백**  
- **gTTS**: 텍스트-음성 변환  
- **Sounddevice** & **Soundfile**: 실시간 오디오 재생 및 저장  

### **하드웨어 통신**  
- **Bleak**: 블루투스를 통해 닷패드와 통신  

### **기타 유틸리티**  
- **Qasync**: PySide와 비동기 코드 통합  

---

## 요구사항  
- **Python 3.12 이상**  
- 필수 라이브러리 설치: `requirements.txt` 참조  

---

## 기여자  
| 이름     | 역할 및 기여                          |  
|----------|--------------------------------------|  
| 김도훈   | 닷패드 SDK 연동 및 프로젝트 전반 개발     |  
| 우나림   | 사전 사운드 개발 및 이미지 처리 기여  |  
| 박지민   | 이미지 처리 시도             |   

---

## 라이센스  
**GreDot** 프로젝트는 [MIT 라이센스](https://opensource.org/licenses/MIT)를 따릅니다.  

```
MIT License  

Copyright (c) 2024 GreDot Development Team  

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.
```  

---

# debugger1

## 프로젝트 구조

```
debugger1/
├── my_debugger.py           # 디버거 클래스 구현 (프로세스 생성, attach, detach, run 등)
├── my_debugger_defines.py   # Windows API 구조체 및 상수 정의
├── my_test.py               # 디버거 테스트 및 실행 예제
└── README.md                # 프로젝트 설명 파일
```

## 각 파일 설명

- **my_debugger.py**: 실제 디버거의 핵심 로직이 구현되어 있습니다. 프로세스 생성, attach/detach, 디버깅 이벤트 루프 등 Windows API를 ctypes로 래핑하여 사용합니다.
- **my_debugger_defines.py**: Windows API와 연동하기 위한 구조체(STARTUPINFO, PROCESS_INFORMATION)와 상수(DEBUG_PROCESS 등)를 정의합니다.
- **my_test.py**: 디버거 클래스를 실제로 사용해보는 테스트 코드입니다. 실행할 exe 경로를 입력받아 프로세스를 생성하고, 디버깅 루프를 돌린 뒤 detach합니다.

## 실행 방법

1. Python 3.x가 설치된 Windows 환경에서 사용하세요.
2. 프로젝트 폴더에서 `my_test.py`를 실행합니다.

```bash
python my_test.py
```

3. 실행할 exe 파일의 전체 경로를 입력합니다. (예: `C:/Windows/System32/notepad.exe`)

## 예시

```
실행할 exe 경로를 입력하세요: C:/Windows/System32/notepad.exe
[*] 프로세스 생성 성공! PID: 1234
[*] 디버깅 루프 시작
[*] 디버깅 이벤트 발생!
[*] 디버깅 루프 종료
[*] 프로세스 detach 완료! PID: 1234
```

## 참고
- Windows API와 ctypes를 활용한 기본 디버거 예제입니다.
- 실제 디버깅 이벤트 파싱 및 고급 기능은 추가 구현이 필요합니다.
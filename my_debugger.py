from ctypes import *
from my_debugger_defines import *

class MyDebugger(object):
    def __init__(self):
        self.h_process = None
        self.pid = None
        self.debugger_active = False

    def load(self, path_to_exe):
        # 프로세스 생성 구조체 준비
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()
        startupinfo.cb = sizeof(startupinfo)

        # CreateProcessA 함수 정의
        creation_flags = DEBUG_PROCESS | CREATE_NEW_CONSOLE
        kernel32 = windll.kernel32
        success = kernel32.CreateProcessA(
            c_char_p(path_to_exe.encode('utf-8')),
            None,
            None,
            None,
            False,
            creation_flags,
            None,
            None,
            byref(startupinfo),
            byref(process_information)
        )

        if not success:
            raise Exception('CreateProcessA 실패')
        else:
            self.h_process = process_information.hProcess
            self.pid = process_information.dwProcessId
            self.debugger_active = True
            print(f"[*] 프로세스 생성 성공! PID: {self.pid}")

    def attach(self, pid):
        # 이미 실행 중인 프로세스에 디버거를 붙임
        self.pid = int(pid)
        kernel32 = windll.kernel32
        self.h_process = kernel32.OpenProcess(0x1F0FFF, False, self.pid)
        if not self.h_process:
            raise Exception('프로세스 핸들 열기 실패')
        attach_result = kernel32.DebugActiveProcess(self.pid)
        if not attach_result:
            raise Exception('DebugActiveProcess 실패')
        self.debugger_active = True
        print(f"[*] 프로세스 attach 성공! PID: {self.pid}")

    def detach(self):
        # 디버거 분리
        if self.debugger_active and self.pid:
            kernel32 = windll.kernel32
            kernel32.DebugActiveProcessStop(self.pid)
            kernel32.CloseHandle(self.h_process)
            self.debugger_active = False
            print(f"[*] 프로세스 detach 완료! PID: {self.pid}")

    def run(self):
        # 디버깅 이벤트 루프 실행
        print("[*] 디버깅 루프 시작")
        kernel32 = windll.kernel32
        debug_event = (c_byte * 1024)()  # 충분히 큰 버퍼
        while self.debugger_active:
            debug_event_struct = create_string_buffer(1024)
            if kernel32.WaitForDebugEvent(byref(debug_event_struct), 100):
                print("[*] 디버깅 이벤트 발생!")
                # 간단한 이벤트 정보 출력
                # 실제로는 DEBUG_EVENT 구조체를 파싱해야 함
                kernel32.ContinueDebugEvent(0, 0, 0x00010002)  # DBG_CONTINUE
            else:
                break
        print("[*] 디버깅 루프 종료")
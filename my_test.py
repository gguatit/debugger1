from my_debugger import MyDebugger
import time

if __name__ == "__main__":
    dbg = MyDebugger()
    # 테스트할 실행 파일 경로를 입력하세요 (예: 'C:/Windows/System32/notepad.exe')
    exe_path = input("실행할 exe 경로를 입력하세요: ")
    try:
        dbg.load(exe_path)
        time.sleep(1)
        dbg.run()
        dbg.detach()
    except Exception as e:
        print(f"오류 발생: {e}")

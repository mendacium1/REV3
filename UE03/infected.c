#include <windows.h>

LONG WINAPI MyUnhandledExceptionFilter(struct _EXCEPTION_POINTERS *ExceptionInfo) {
    MessageBoxW(NULL, L"Infected", L"Infected", MB_ICONWARNING);
   
    //ExitProcess(0);

    return EXCEPTION_EXECUTE_HANDLER;
}

int main() {

    if (IsDebuggerPresent()){
	MessageBoxW(0, (LPCWSTR)L"Hello", (LPCWSTR)L"Hello", MB_OK);
	return 0;
    }
    SetUnhandledExceptionFilter(MyUnhandledExceptionFilter);
    DebugBreak();
    MessageBoxW(NULL, L"Hello", L"Hello", MB_OK);

    return 0;
}

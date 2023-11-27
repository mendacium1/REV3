#include <windows.h>

/**
* This function is a custom unhandled exception filter.
*
* @param ExceptionInfo A pointer to an EXCEPTION_POINTERS structure that
*                      contains information about the exception.
* @return A constant that determines how the exception is handled.
*
* The function displays a message box with the text "Infected" and
* an icon indicating a warning. It's meant to be invoked when an
* unhandled exception occurs. The function then returns a constant
* indicating that the exception handler (EXCEPTION_EXECUTE_HANDLER)
* should be executed.
*/
LONG WINAPI MyUnhandledExceptionFilter(struct _EXCEPTION_POINTERS* ExceptionInfo) {
	MessageBoxW(NULL, L"Infected", L"Infected", MB_ICONWARNING);

	//ExitProcess(0);

	return EXCEPTION_EXECUTE_HANDLER;
}

/**
* The main entry point for the application.
*
* @return An integer indicating the success or failure of the program.
*
* The function first checks if a debugger is present using IsDebuggerPresent().
* If a debugger is detected, it displays a message box with "Hello" and then
* terminates. If no debugger is detected, it sets a custom unhandled
* exception filter and then deliberately triggers a breakpoint exception
* using DebugBreak(). If the breakpoint is unhandled, it will invoke the
* custom unhandled exception filter. After handling the exception,
* or if the breakpoint is handled by a debugger, it displays a "Hello" message
* box and then exits.
*
* NOTE: It might happen, that when executing this code on a system where a
* debugger is just installed but not running, "DebugBreak()" or "INT 3" might
* start the debugger automatically.
*/
int main() {

	if (IsDebuggerPresent()) {
		MessageBoxW(0, (LPCWSTR)L"Hello", (LPCWSTR)L"Hello", MB_OK);
		return 0;
	}
	SetUnhandledExceptionFilter(MyUnhandledExceptionFilter);
	DebugBreak();
	MessageBoxW(NULL, L"Hello", L"Hello", MB_OK);

	return 0;
}
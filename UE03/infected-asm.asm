.386
.model flat,stdcall
option casemap :none

include \masm32\include\windows.inc
include \masm32\include\kernel32.inc
include \masm32\include\user32.inc
includelib \masm32\lib\kernel32.lib
includelib \masm32\lib\user32.lib

.data
HelloWorld dw 'H','e','l','l','o',0
Infected dw 'I','n','f','e','c','t','e','d',0

.code
start:
	jmp begin

NoDebugger:
	; If no debugger is found, display "Infected" message
	push MB_ICONWARNING
	push offset Infected
	push offset Infected
	push 0
	call MessageBoxW
	jmp ExitProcessCall

begin:
	; Check if debugger is present with IsDebuggerPresent-function
	call IsDebuggerPresent
	test eax, eax
	jnz DebuggerFound ; Jump if debugger is detected

	; If no debugger is found with IsDebuggerPresent, try with unhandlet exception
	invoke SetUnhandledExceptionFilter, NoDebugger
	int 3
	;if Debugger is Found:
	jmp DebuggerFound

DebuggerFound:
	; If a debugger is detected, display "Hello" message
	push MB_OK
	push offset HelloWorld
	push offset HelloWorld
	push 0
	call MessageBoxW

ExitProcessCall:
	push 0
	call ExitProcess
	end start

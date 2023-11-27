.386
.model flat,stdcall
option casemap :none

include \masm32\include\windows.inc
include \masm32\include\kernel32.inc
include \masm32\include\user32.inc
includelib \masm32\lib\kernel32.lib
includelib \masm32\lib\user32.lib

.data
; Define strings to be used in the message boxes.
HelloWorld dw 'H','e','l','l','o',0
Infected dw 'I','n','f','e','c','t','e','d',0

.code
start:
	; Entry point of the program. Jumps to the 'begin' label.
	jmp begin

NoDebugger:
	; This section executes if no debugger is detected.
	; Displays a message box with the text "Infected" and a warning icon.
	push MB_ICONWARNING
	push offset Infected
	push offset Infected
	push 0
	call MessageBoxW
	jmp ExitProcessCall

begin:
	; Checks if a debugger is present.
	; Calls IsDebuggerPresent and examines the return value.
	call IsDebuggerPresent
	test eax, eax
	jnz DebuggerFound ; If EAX is non-zero, a debugger is detected, jump to DebuggerFound.
	
	; If no debugger is detected, set up an exception filter and trigger a breakpoint.
	invoke SetUnhandledExceptionFilter, NoDebugger
	int 3 ; Software breakpoint - triggers an exception if no debugger is present.
	; Continue to DebuggerFound if execution reaches here.
	jmp DebuggerFound

DebuggerFound:
	; This section executes if a debugger is detected.
	; Displays a message box with the text "Hello".
	push MB_OK
	push offset HelloWorld
	push offset HelloWorld
	push 0
	call MessageBoxW

ExitProcessCall:
	; Terminates the process.
	push 0
	call ExitProcess
	end start
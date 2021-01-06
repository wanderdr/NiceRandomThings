' Turn off the capslock if its turned on

Set objWord = CreateObject("Word.Application")
If objWord.CapsLock Then
	Set objShell = CreateObject("WScript.Shell")
	objShell.SendKeys "{CAPSLOCK}"
End If
objWord.Quit
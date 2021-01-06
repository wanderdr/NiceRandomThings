#!/usr/bin/env python
"""

Turn CapsLock on/off on Windows

"""
import ctypes
import sys

# Based on https://stackoverflow.com/questions/854393/change-keyboard-locks-in-python/854442
def capslock(flag_on):
	# Load windows dll
	dll = ctypes.WinDLL('User32.dll')
	VK_CAPITAL = 0X14
	# Check if need to change
	if (flag_on and not dll.GetKeyState(VK_CAPITAL)) or (not flag_on and dll.GetKeyState(VK_CAPITAL)):
		# Send the keystroke command
		dll.keybd_event(VK_CAPITAL, 0X3a, 0X1, 0)
		dll.keybd_event(VK_CAPITAL, 0X3a, 0X3, 0)

if __name__ == '__main__':
    turn_capslock(sys.argv[1])

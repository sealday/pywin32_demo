import ctypes
from _ctypes import byref
from win32gui import FindWindow, SetWindowPos

import logging
from win32con import SWP_SHOWWINDOW, SWP_HIDEWINDOW

from win32 import ABM_SETSTATE
from win32.shell32 import APPBARDATA, SHAppBarMessage


class TaskBar:
    """
    当第一个参数为 ABM_SETSTATE 时 lParam 几个参数好像和描述不太一样
    至少当他为 0 的时候，并不会隐藏任务栏
    https://msdn.microsoft.com/en-us/library/windows/desktop/bb787961(v=vs.85).aspx
    """
    def __init__(self):
        self.hwnd = FindWindow("Shell_TrayWnd", None)

    def show(self):
        SetWindowPos(self.hwnd, 0, 0, 0, 0, 0, SWP_SHOWWINDOW)
        data = APPBARDATA()
        data.cbSize = ctypes.sizeof(APPBARDATA)
        data.lParam = 0
        SHAppBarMessage(ABM_SETSTATE, byref(data))
        logging.info('Show task bar.')

    def hide(self):
        SetWindowPos(self.hwnd, 0, 0, 0, 0, 0, SWP_HIDEWINDOW)
        data = APPBARDATA()
        data.cbSize = ctypes.sizeof(APPBARDATA)
        data.lParam = 1
        SHAppBarMessage(ABM_SETSTATE, byref(data))
        logging.info('Hide task bar.')

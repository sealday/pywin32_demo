from ctypes import WINFUNCTYPE, windll, Structure, POINTER
from ctypes.wintypes import PUINT, DWORD, HWND, UINT, RECT, LPARAM


class APPBARDATA(Structure):
    _fields_ = [
        ('cbSize', DWORD),
        ('hWnd', HWND),
        ('uCallbackMessage', UINT),
        ('uEdge', UINT),
        ('rc', RECT),
        ('lParam', LPARAM),
    ]

PAPPBARDATA = POINTER(APPBARDATA)
SHAppBarMessage = WINFUNCTYPE(PUINT, DWORD, PAPPBARDATA)(('SHAppBarMessage', windll.shell32))

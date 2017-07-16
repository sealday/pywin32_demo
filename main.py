import logging
import win32gui
import winxpgui

import win32con
from flask import Flask

from TaskBar import TaskBar

count = 0
app = Flask(__name__)


def enum_windows_func(hWnd, lParam):
    global count
    if not win32gui.GetWindow(hWnd, win32con.GW_OWNER) and win32gui.IsWindowVisible(hWnd):
        name: str = win32gui.GetClassName(hWnd)
        if name == 'Shell_TrayWnd' or name == 'Progman':
            return
        title = win32gui.GetWindowText(hWnd)
        rect = win32gui.GetWindowRect(hWnd)
        # 排除一些 dummy 的窗口
        if rect == (0, 0, 0, 0):
            return
        count = count + 1
        if '迷糊' in title:
            icon_handle = win32gui.SendMessage(hWnd, win32con.WM_GETICON, win32con.ICON_BIG, 0)
            print(name, hWnd, title, icon_handle)
            # result = win32gui.ShowWindow(hWnd, win32con.SW_SHOWNORMAL)
            # print('迷糊', result)
            print(hWnd, win32gui.GetParent(hWnd))
            # win32gui.SetWindowPos(hWnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
            #                       win32con.SWP_NOSIZE | win32con.SWP_NOMOVE | win32con.SWP_DRAWFRAME)
            # 对于多桌面这一点也是有效果的
            win32gui.SetForegroundWindow(hWnd)
            # re = win32gui.SetActiveWindow(hWnd)
            # print(re)
        # icon_handle = win32gui.SendMessage(hWnd, win32con.WM_GETICON, win32con.ICON_BIG, 0)
        print('列举', count, name, rect, hex(hWnd), title)


@app.route('/')
def hello():
    return 'hello world'


@app.route('/show')
def show():
    win32gui.EnumWindows(enum_windows_func, None)
    return 'show'


@app.route('/hide')
def hide():
    return 'hide'


# http://blog.csdn.net/liaomin416100569/article/details/38457129
if __name__ == '__main__':
    # win32api.MessageBox(None, 'hello world', 'title', win32con.MB_OK)
    # ctypes.windll.user32.MessageBoxW(None, '你好世界', '标题', win32con.MB_OK)
    # win32gui.EnumWindows(enum_windows_func, None)
    # print('数量', count)
    # import _thread
    # _thread.start_new(lambda: app.run('0.0.0.0', 5000), ())
    # # 为什么不需要自己找这个函数？
    logging.basicConfig(level=logging.INFO)
    taskBar = TaskBar()
    taskBar.show()

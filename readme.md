当 class 是 Windows.UI.Core.CoreWindow 的时候，并没有打开这个应用程序
当 class 是 ApplicationFrameWindow 的时候才是打开这个应用程序的状态

很神奇，如果打开一下对应的程序，再关掉之后，那个 Core.CoreWindow 就消失了

虽然可以被彻底隐藏起来，但是按开始菜单键的时候，还是会让他出现，并且取消隐藏状态（任务栏）

如果要支持高清屏幕还得处理一下
ctypes.windll.shcore.SetProcessDpiAwareness(1) 使用这个 api 可以告诉系统不要自动处理
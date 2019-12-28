import random


class Tools(object):

    @classmethod
    def qt_screenshot(cls, app):
        import win32gui
        name = str(random.randint(10000, 99999))
        hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
        screen = app.primaryScreen()
        img = screen.grabWindow(hwnd).toImage()
        img.save(name + ".jpg")

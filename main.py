import pystray
from PIL import Image
from pystray import MenuItem 
import pywintypes
import win32api
import win32con


def set_resolution(width:int,height:int):
    try: 
        print("Called set_resolution")
        devmode = pywintypes.DEVMODEType()
        devmode.PelsWidth = width
        devmode.PelsHeight = height
        devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
        win32api.ChangeDisplaySettings(devmode, 0)
    except Exception as e:
        print(e)

image = Image.open('icon.png')
icon = pystray.Icon('Resolution Agent')
icon.icon=image
icon.title = 'Resolution Agent'


def on_exit():
    try: 
        icon.visible = False
        icon.stop()
    except Exception as e:
        print(e)



if __name__=="__main__":
    
    
    menu = (
    MenuItem('4096 x 2160', lambda: set_resolution(4096,2160)),
    MenuItem('3840 x 2160', lambda: set_resolution(3840,2160)),
    MenuItem('2560 x 1600', lambda: set_resolution(2560,1600)),
    MenuItem('2560 x 1440', lambda: set_resolution(2560,1440)),
    MenuItem('1920 x 1200', lambda: set_resolution(1920,1200)),
    MenuItem('1920 x 1080', lambda: set_resolution(1920,1080)),
    MenuItem('1680 x 1050', lambda: set_resolution(1680,1050)),
    MenuItem('1600 x 900', lambda: set_resolution(1600,900)),
    MenuItem('1440 x 900', lambda: set_resolution(1440,900)),
    MenuItem('1366 x 768', lambda: set_resolution(1366,768)),
    MenuItem('1280 x 1024', lambda: set_resolution(1280,1024)),
    MenuItem('1280 x 800', lambda: set_resolution(1280,800)),
    MenuItem('1280 x 720', lambda: set_resolution(1280,720)),
    MenuItem('1024 x 768', lambda: set_resolution(1024,768)),
    MenuItem('800 x 600', lambda: set_resolution(800,600)),
    MenuItem('640 x 480', lambda: set_resolution(640,480)),
    # MenuItem('Exit',on_exit()),
    )
    # icon = pystray.Icon('Resolution Agent', image, 'Resolution Agent', menu)
    icon.menu=menu
    try:
        icon.run()
    except KeyboardInterrupt:
        icon.visible =False
        icon.stop()
        
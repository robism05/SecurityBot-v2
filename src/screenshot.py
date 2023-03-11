import platform
from subprocess import call
from time import gmtime, strftime
from pathlib import Path
import PIL.ImageGrab

path = Path().parent.absolute()
print(path)


def take_screenshot():
    # taking screenshot on macOS
    if platform.system() == "Darwin":
        call(["screencapture", strftime("%H:%M:%S")+".jpg"]) 
    # taking screenshot on Windows
    elif platform.system() == "Windows":
        screenshot = PIL.ImageGrab.grab()
        screenshot.save(path+"image.jpg")
    # taking screenshot on Linux
    elif platform.system() == "Linux":
        call(["scrot", strftime("%H:%M:%S", gmtime()) + ".jpg"])

take_screenshot()

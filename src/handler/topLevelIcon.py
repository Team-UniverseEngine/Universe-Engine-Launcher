import src.handler.path as path
import sys
import os

def I(topLevel):
    baseDirectory = path.imagePath()
    if sys.platform == "win32":
        iconPath = os.path.join(baseDirectory, 'icon64.ico')
        if os.path.exists(iconPath):
            topLevel.after(200, lambda: topLevel.iconbitmap(iconPath))
    else:
        iconPath = os.path.join(baseDirectory, 'icon64.png')
        if os.path.exists(iconPath):
            photo = tk.PhotoImage(file=iconPath)
            topLevel.iconphoto(False, photo)
import os
import sys

import tkinter as tk
import src.handler.path as path
from PIL import Image, ImageColor
import customtkinter as ctk
import src.main.settingsMenu as settings

import src.main.otherInterface.version as ver
import src.main.otherInterface.instance as inst

def initialize():
    root = ctk.CTk()
    root.title("Universe Launcher")
    root.geometry("640x400")

    if sys.platform == "win32":
        iconPath = os.path.join(path.imagePath(), 'icon64.ico')
        if os.path.exists(iconPath):
            root.iconbitmap(iconPath)
    else:
        iconPath = os.path.join(path.imagePath(), 'icon64.png')
        if os.path.exists(iconPath):
            root.iconphoto(False, tk.PhotoImage(file=iconPath))
    
    mainButton(root)
    funnyInterface(root)
    instanceInterface(root)
    
    root.mainloop()
    
def mainButton(root):
    mainFrame = ctk.CTkFrame(root, fg_color="transparent")
    mainFrame.pack(pady=10, padx=10, fill="y", side="left")
    
    # ==================== BUTTONS ====================
    mainButtons = [
        {
            "buttonName": "Folder",
            "imageIcon": "folder",
            "execCommand": startFolder,
            "padY": (10, 5),
            "side": "top"
        },
        {
            "buttonName": "Start",
            "imageIcon": "play",
            "execCommand": startUniverse,
            "padY": (5, 5),
            "side": "top"
        },
        {
            "buttonName": "Options",
            "imageIcon": "settings",
            "execCommand": startOptions,
            "padY": (5, 10),
            "side": "bottom"
        }
    ]
    
    buttonFrame = ctk.CTkFrame(mainFrame, fg_color="#1E1E1E")
    buttonFrame.pack(fill="y", expand=True)
    
    for buttons in mainButtons:
        nameButton = buttons["buttonName"]
        buttonImage = buttons["imageIcon"]
        commandExecute = buttons["execCommand"]
        paddingY = buttons["padY"]
        buttonSide = buttons["side"]
    
        iconPath = os.path.join(path.iconPath(), buttonImage + ".png")
        if os.path.exists(iconPath):
            buttonIcon = ctk.CTkImage(Image.open(iconPath), size=(20, 20))
            itemButton = ctk.CTkButton(buttonFrame, image=buttonIcon, fg_color="#1B1B1B", text="", command=commandExecute, width=20)
        else:
            itemButton = ctk.CTkButton(buttonFrame, fg_color="#1B1B1B", text=nameButton, command=commandExecute, width=20)
        itemButton.pack(padx=10, pady=paddingY, fill="y", expand=True, side=buttonSide)


def funnyInterface(root):
    container = ctk.CTkFrame(root, fg_color="transparent")
    container.pack(pady=20, padx=10)

    imagePath = os.path.join(path.imagePath(), 'universe.png')
    if os.path.exists(imagePath):
        image = Image.open(imagePath)
        ctkImage = ctk.CTkImage(image, size=(100, 100))
        imageLabel = ctk.CTkLabel(container, image=ctkImage, text="")
        imageLabel.image = image #type: ignore
        imageLabel.pack(pady=10)
    
def instanceInterface(root):
    container = ctk.CTkFrame(root, fg_color="#1E1E1E")
    container.pack(pady=10, padx=10, side="bottom", fill="x", expand=True)
    
    iconPath = os.path.join(path.iconPath(), "folder.png")
    if os.path.exists(iconPath):
        buttonIcon = ctk.CTkImage(Image.open(iconPath), size=(20, 20))
        itemButton = ctk.CTkButton(container, image=buttonIcon, fg_color="#1B1B1B", text="", command=inst.init, width=10)
    else:
        itemButton = ctk.CTkButton(container, fg_color="#1B1B1B", text="Create Instance", command=inst.init, width=10)
    itemButton.pack(padx=10, pady=10, side="left")
    
    instanceText = ctk.CTkLabel(container, text="Current instance selected: ", text_color="#FFFFFF")
    instanceText.pack(side="left")
    
def startUniverse():
    print("paws at u")
    
def startOptions():
    print("barks at u")
    settings.init()

def startFolder():
    print("idk ;m;")
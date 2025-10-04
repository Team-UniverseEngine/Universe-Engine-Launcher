import os
import sys

import tkinter as tk
import src.handler.path as path
from PIL import Image, ImageColor
import customtkinter as ctk
import src.main.settingsMenu as settings
import src.backend.fetchVersions as FV

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
    
    imageInterface(root)
    labelText(root)
    instanceInterface(root)
    mainButton(root)
    
    FV.init()
    
    root.mainloop()
    
def mainButton(root):
    mainFrame = ctk.CTkFrame(root, fg_color="transparent")
    mainFrame.pack(pady=10, padx=10)
    
    # ==================== BUTTONS ====================
    mainButtons = [
        {
            "buttonName": "Start",
            "execCommand": startUniverse,
            "padX": (10, 5),
            "side": "left"
        },
        {
            "buttonName": "Options",
            "execCommand": startOptions,
            "padX": (5, 10),
            "side": "left"
        },
        {
            "buttonName": "Folder",
            "execCommand": startFolder,
            "padX": (5, 10),
            "side": "right"
        }
    ]
    
    buttonFrame = ctk.CTkFrame(mainFrame, fg_color="#1E1E1E")
    buttonFrame.pack(side="bottom", fill="x", expand=True)
    
    for buttons in mainButtons:
        nameButton = buttons["buttonName"]
        commandExecute = buttons["execCommand"]
        paddingX = buttons["padX"]
        buttonSide = buttons["side"]
    
        itemButton = ctk.CTkButton(buttonFrame, fg_color="#1B1B1B", text=nameButton, command=commandExecute)
        itemButton.pack(padx=paddingX, pady=10, fill="x", expand=True, side=buttonSide)


def imageInterface(root):
    container = ctk.CTkFrame(root, fg_color="transparent")
    container.pack(pady=20, padx=10)

    imagePath = os.path.join(path.imagePath(), 'universe.png')
    if os.path.exists(imagePath):
        image = Image.open(imagePath)
        ctkImage = ctk.CTkImage(image, size=(100, 100))
        imageLabel = ctk.CTkLabel(container, image=ctkImage, text="")
        imageLabel.image = image #type: ignore
        imageLabel.pack(pady=10)
        
def labelText(root):
    textLabel = ctk.CTkFrame(root, fg_color="transparent")
    textLabel.pack(pady=10, padx=10)
    
    instanceText = ctk.CTkLabel(textLabel, text="Current instance selected: ", text_color="#FFFFFF")
    instanceText.pack()
    
def instanceInterface(root):
    container = ctk.CTkFrame(root, fg_color="#1E1E1E")
    container.pack(pady=10, padx=10)
    
    instanceButton = ctk.CTkButton(container, text="Select Instance", command=inst.init, fg_color="#1B1B1B")
    instanceButton.pack(pady=10, padx=10, expand=True, fill="x", side="right")
    
def startUniverse():
    print("paws at u")
    
def startOptions():
    print("barks at u")
    settings.init()

def startFolder():
    print("idk ;m;")
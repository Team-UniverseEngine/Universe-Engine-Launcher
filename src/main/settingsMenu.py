import os
import sys

import tkinter as tk
import src.handler.path as path
import customtkinter as ctk

def init():
    root = ctk.CTk()
    root.title("Settings")
    root.geometry("360x240")

    if sys.platform == "win32":
        iconPath = os.path.join(path.imagePath(), 'icon64.ico')
        if os.path.exists(iconPath):
            root.iconbitmap(iconPath)
    else:
        iconPath = os.path.join(path.imagePath(), 'icon64.png')
        if os.path.exists(iconPath):
            root.iconphoto(False, tk.PhotoImage(file=iconPath))
    
    ui(root)
    
    root.mainloop()

def ui(root):
    mainFrame = ctk.CTkFrame(root, fg_color="transparent")
    mainFrame.pack(pady=10, padx=10)

    settingsButtons = [
        {
            "buttonName": "TestButton",
            "execCommand": root.destroy,
            "padY": (5, 10),
            "side": "top"
        },
        {
            "buttonName": "Another1",
            "execCommand": saySmthElse,
            "padY": (5, 10),
            "side": "bottom"
        }
    ]

    buttonFrame = ctk.CTkFrame(mainFrame, fg_color="#1E1E1E")
    buttonFrame.pack(side="bottom", fill="y", expand=True)
    
    for buttons in settingsButtons:
        nameButton = buttons["buttonName"]
        commandExecute = buttons["execCommand"]
        paddingX = buttons["padY"]
        buttonSide = buttons["side"]
    
        itemButton = ctk.CTkButton(buttonFrame, fg_color="#1B1B1B", text=nameButton, command=commandExecute)
        itemButton.pack(padx=paddingX, pady=10, fill="y", expand=True, side=buttonSide)

def saySmthElse():
    print("does it look like i care?")

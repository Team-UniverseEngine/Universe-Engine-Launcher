# code taken from noteted!!!
# foss app by daveberry blueson

import os
import sys
import json

import customtkinter as ctk
import tkinter as tk

def getAppConfigDirectory():
    if sys.platform == 'win32':
        return os.path.join(os.getenv('APPDATA'), 'Universe Engine Launcher') # type: ignore
    elif sys.platform == 'linux': # Linux
        return os.path.join(os.getenv('XDG_CONFIG_HOME', os.path.join(os.path.expanduser('~'), '.config')), 'Universe Engine Launcher')
    elif sys.platform == 'darwin': # macOS
        return os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', 'Universe Engine Launcher')
    # fallback for other systems or if APPDATA is not set
    return os.path.join(os.path.expanduser('~'), '.Universe Engine Launcher')

appDirectory = getAppConfigDirectory()
if not os.path.exists(appDirectory):
    os.makedirs(appDirectory)

settingsFile = os.path.join(appDirectory, 'settings.json')

def loadSettings():
    try:
        with open(settingsFile, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def saveSettings(settingsData):
    print(f"Attempting to save settings to: {settingsFile}")
    with open(settingsFile, 'w') as f:
        json.dump(settingsData, f, indent=4)
        
def getSettingsDef():
    settingsDef = [
        {
            "name": "Automatically check for updates?",
            "type": "bool",
            "default": True,
            "id": "automaticUpdate"
        }
    ]
    
    return settingsDef

def listAllSettings(parent):
    settingsDef = getSettingsDef()
    for settings in settingsDef:
        settingName = settings["name"]
        settingType = settings["type"]
        settingDefault = settings["default"]
        settingID = settings["id"]
        
        settingFrame = ctk.CTkFrame(parent, fg_color="transparent")
        settingFrame.pack(pady=5, padx=10, fill="x")

        settingLabel = ctk.CTkLabel(settingFrame, text=settingName)
        settingLabel.pack(side="left", padx=(0, 5))
        
        if settingType == "bool":
            settingCheckbox = ctk.CTkCheckBox(settingFrame)
            settingCheckbox.pack(side="right", padx=10)
# code taken from noteted!!!
# foss app by daveberry blueson


import os
import sys
import json

def getAppConfigDirectory():
    if sys.platform == 'win32':
        return os.path.join(os.getenv('APPDATA'), 'Noteted')
    elif sys.platform == 'linux': # Linux
        return os.path.join(os.getenv('XDG_CONFIG_HOME', os.path.join(os.path.expanduser('~'), '.config')), 'Noteted')
    elif sys.platform == 'darwin': # macOS
        return os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', 'Noteted')
    # fallback for other systems or if APPDATA is not set
    return os.path.join(os.path.expanduser('~'), '.noteted')

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
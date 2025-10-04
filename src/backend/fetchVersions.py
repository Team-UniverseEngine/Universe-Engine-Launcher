import os
import requests

def init():
    internet = requests.get("https://raw.githubusercontent.com/Team-UniverseEngine/Universe-Engine/refs/heads/main/versionList.txt")
    print("Fetching if the user has internet...")
    if internet.status_code == 200:
        print("User has internet! Continuing fetching versions...")
        fetchVersions()
    elif internet.status_code == 404:
        print("Not found! Is it the correct link?")
    else:
        print("Is your internet running? Can't fetch!")
        
def fetchVersions():
    response = requests.get("https://raw.githubusercontent.com/Team-UniverseEngine/Universe-Engine/refs/heads/main/versionList.txt")
    versionList = response.text.split()
    
    for version in versionList:
        print(version)
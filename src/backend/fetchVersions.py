import os
import requests

URL = requests.get("https://raw.githubusercontent.com/Team-UniverseEngine/Universe-Engine/refs/heads/main/versionList.txt")

def init():
    print("Fetching if the user has internet...")
    if URL.status_code == 200:
        print("User has internet!")
    elif URL.status_code == 404:
        print("Not found! Is it the correct link?")
    else:
        print("Is your internet running? Can't fetch!")
        
def fetchVersions():
    versionList = URL.text.split()
    return versionList
import os

def mainpath():
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def assetsPath():
    return os.path.join(mainpath(), 'assets')

def imagePath():
    return os.path.join(assetsPath(), 'images')
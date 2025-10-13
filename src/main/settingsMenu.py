import customtkinter as ctk
import src.handler.topLevelIcon as TLI
import src.backend.settings as settings

curSettings = settings.loadSettings()

def init():
    settingsWindow = ctk.CTkToplevel()
    settingsWindow.title("Settings")
    settingsWindow.geometry("360x240")
    settingsWindow.resizable(False, True)
    
    settingsWindow.transient()
    settingsWindow.after(10, settingsWindow.grab_set)
    
    TLI.I(settingsWindow)
    ui(settingsWindow)
    saveUI(settingsWindow)

def ui(parent):
    settings.loadSettings()
    settings.listAllSettings(parent)


def saveUI(parent):
    mainFrame = ctk.CTkFrame(parent, fg_color="transparent")
    mainFrame.pack(pady=10, padx=10)

    settingsButtons = [
        {
            "buttonName": "save",
            "execCommand": save,
            "padX": (5, 10),
            "side": "left"
        },
        {
            "buttonName": "cancel",
            "execCommand": parent.destroy,
            "padX": (5, 10),
            "side": "right"
        }
    ]

    buttonFrame = ctk.CTkFrame(mainFrame, fg_color="#1E1E1E")
    buttonFrame.pack(side="bottom", fill="x", expand=True)
    
    for buttons in settingsButtons:
        nameButton = buttons["buttonName"]
        commandExecute = buttons["execCommand"]
        paddingX = buttons["padX"]
        buttonSide = buttons["side"]
    
        itemButton = ctk.CTkButton(buttonFrame, fg_color="#1B1B1B", text=nameButton, command=commandExecute)
        itemButton.pack(padx=paddingX, pady=10, fill="x", expand=True, side=buttonSide)

def save():
    settings.saveSettings(curSettings)
    
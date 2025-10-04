import customtkinter as ctk
import src.handler.topLevelIcon as TLI

def init():
    instanceWindow = ctk.CTkToplevel()
    instanceWindow.title("New Instance")
    instanceWindow.geometry("640x480")
    
    instanceWindow.transient()
    instanceWindow.after(10, instanceWindow.grab_set)
    
    TLI.I(instanceWindow)
    ui(instanceWindow)

def ui(parent):
    mainFrame = ctk.CTkFrame(parent, fg_color="transparent")
    mainFrame.pack(pady=10, padx=10)

    instanceButtons = [
        {
            "buttonName": "Select Version",
            "execCommand": parent.destroy,
            "padY": (5, 10),
            "side": "top"
        }
    ]

    buttonFrame = ctk.CTkFrame(mainFrame, fg_color="#1E1E1E")
    buttonFrame.pack(side="bottom", fill="y", expand=True)
    
    for buttons in instanceButtons:
        nameButton = buttons["buttonName"]
        commandExecute = buttons["execCommand"]
        paddingX = buttons["padY"]
        buttonSide = buttons["side"]
    
        itemButton = ctk.CTkButton(buttonFrame, fg_color="#1B1B1B", text=nameButton, command=commandExecute)
        itemButton.pack(padx=paddingX, pady=10, fill="y", expand=True, side=buttonSide)

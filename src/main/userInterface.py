import customtkinter as ctk

def initialize():
    root = ctk.CTk()
    root.title("Universe Launcher")
    root.geometry("600x400")
    
    userInterface(root)
    
    root.mainloop()
    
def userInterface(root):
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
    
def startUniverse():
    print("paws at u")
    
def startOptions():
    print("barks at u")
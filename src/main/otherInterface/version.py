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

    buttonFrame = ctk.CTkFrame(mainFrame, fg_color="#1E1E1E")
    buttonFrame.pack(side="bottom", fill="y", expand=True)

    versionSelect = ctk.CTkButton(buttonFrame, fg_color="#1B1B1B", text="Select Version", command=parent.destroy)
    versionSelect.pack(padx=10, pady=10, fill="y", expand=True, side="left")
    
    cancelSelect = ctk.CTkButton(buttonFrame, fg_color="#1B1B1B", text="Cancel", command=parent.destroy)
    cancelSelect.pack(padx=10, pady=10, fill="y", expand=True, side="right")
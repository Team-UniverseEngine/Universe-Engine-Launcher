import customtkinter as ctk
import src.handler.topLevelIcon as TLI
import src.backend.fetchVersions as fV

def init():
    instanceWindow = ctk.CTkToplevel()
    instanceWindow.title("Install a new version")
    instanceWindow.geometry("300x480")
    instanceWindow.resizable(False, False)
    
    instanceWindow.transient()
    instanceWindow.after(10, instanceWindow.grab_set)
    
    TLI.I(instanceWindow)
    ui(instanceWindow)

def ui(parent):
    mainFrame = ctk.CTkFrame(parent, fg_color="transparent")
    mainFrame.pack(pady=10, padx=10, fill="both", expand=True)

    versionFrame = ctk.CTkScrollableFrame(mainFrame, fg_color="#1E1E1E")
    versionFrame.pack(pady=10, padx=10, fill="both", expand=True)

    versions = fV.fetchVersions()
    if versions:
        for version in versions:
            versionButton = ctk.CTkButton(versionFrame, text=version, command=lambda v=version: print(v))
            versionButton.pack(side="top", padx=5, pady=5, fill="x")

    buttonFrame = ctk.CTkFrame(mainFrame, fg_color="transparent")
    buttonFrame.pack(side="bottom", fill="x", pady=10, padx=10)
    
    cancelButton = ctk.CTkButton(buttonFrame, text="Cancel", command=parent.destroy)
    cancelButton.pack(side="top")
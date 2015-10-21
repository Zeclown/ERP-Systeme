__author__ = 'Drago'
from tkinter import *


class View():
    def __init__(self, parent):
        self.root = Tk()
        self.parent = parent
        self.currentFrame = None
        self.frameLogin = FrameLogin(self, self.root, "Connexion", width=400, height=150)
        self.frameAcceuil = FrameAcceuil(self, self.root, "Acceuil", width=900, height=500)
        self.frameSwapper(self.frameLogin)
        
    def show(self):
        self.root.mainloop()

    def frameSwapper(self, frame):
        if self.currentFrame:
            self.currentFrame.pack_forget()
        frame.pack(fill=BOTH, expand=True)
        self.currentFrame = frame
        self.root.title(frame.titleFrame)

class GFrame(Frame):
    BACKGROUND_COLOR = "gray20"
    FORGROUND_COLOR = "white"

    def __init__(self, parentController, parentWindow, title, **args):
        Frame.__init__(self, parentWindow, **args)
        self.parentWindow = parentWindow
        self.parentController = parentController
        self.titleFrame = title
        self.grid_propagate(0)
        self.config(bg=GFrame.BACKGROUND_COLOR)

class FrameLogin(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)

        self.label = Label(self, bg=GFrame.BACKGROUND_COLOR)
        self.label.grid(row=0, column=0, sticky=W)

        self.labelName = Label(self, text="Usager : ", bg=GFrame.BACKGROUND_COLOR, fg=GFrame.FORGROUND_COLOR, width=25, anchor=E)
        self.labelName.grid(row=1, column=0, sticky=E)
        self.entryName = Entry(self)
        self.entryName.focus_set()
        self.entryName.grid(row=1, column=1, sticky=E)

        self.labelPass = Label(self, text="Mot de passe : ", bg=GFrame.BACKGROUND_COLOR, fg=GFrame.FORGROUND_COLOR, width=25, anchor=E)
        self.labelPass.grid(row=2, column=0, sticky=E)
        self.entryPass = Entry(self, show="*")
        self.entryPass.grid(row=2, column=1, sticky=E)

        self.ButtonLogin = Button(self, text="Se connecter", width=10, command=self.parentController.parent.userLogin)
        self.ButtonLogin.grid(row=3, column=1, sticky=E)
    
    def resetEntries(self):
        self.entryName.delete(0, END)
        self.entryPass.delete(0, END)

class FrameAcceuil(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
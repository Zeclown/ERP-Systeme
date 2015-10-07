__author__ = 'Drago'
from tkinter import *


class View():
    def __init__(self, parent):
        self.root = Tk()
        self.parent = parent
        self.currentFrame = None
        self.frameLogin = FrameLogin(self, self.root, width=400, height=150)
        self.frameAcceuil = FrameAcceuil(self, self.root, width=600, height=400)
        self.frameSwapper(self.frameLogin)

    def frameSwapper(self, frame):
        if self.currentFrame:
            self.currentFrame.pack_forget()
        frame.pack(fill=BOTH, expand=True)
        self.currentFrame = frame
        self.root.title(frame.titleFrame)

class FrameLogin(Frame):
    def __init__(self, view, parent, **args):
        Frame.__init__(self, parent, **args)
        self.grid_propagate(False)
        self.parent = parent
        self.view = view
        self.titleFrame = "Login"
        #self.parent.wm_overrideredirect(True)

        BACKGROUND_COLOR = "gray20"
        self.config(bg=BACKGROUND_COLOR)

        self.label = Label(self, bg=BACKGROUND_COLOR)
        self.label.grid(row=0, column=0, sticky=W)

        self.labelName = Label(self, text="User : ", bg=BACKGROUND_COLOR, fg="white", width=25, anchor=E)
        self.labelName.grid(row=1, column=0, sticky=E)
        self.entryName = Entry(self)
        self.entryName.focus_set()
        self.entryName.grid(row=1, column=1, sticky=E)

        self.labelPass = Label(self, text="Password : ", bg=BACKGROUND_COLOR, fg="white", width=25, anchor=E)
        self.labelPass.grid(row=2, column=0, sticky=E)
        self.entryPass = Entry(self, show="*")
        self.entryPass.grid(row=2, column=1, sticky=E)

        self.ButtonLogin = Button(self, text="Login", width=10, command=self.view.parent.userLogin)
        self.ButtonLogin.grid(row=3, column=1, sticky=E)
    
    def resetEntries(self):
        self.entryName.delete(0, END)
        self.entryPass.delete(0, END)

class FrameAcceuil(Frame):
    def __init__(self, view, parent, **args):
        Frame.__init__(self, parent, **args)
        self.grid_propagate(False)
        self.parent = parent
        self.view = view
        self.titleFrame = "Acceuil"
        
        BACKGROUND_COLOR = "gray20"
        self.config(bg=BACKGROUND_COLOR)
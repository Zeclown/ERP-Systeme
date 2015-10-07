__author__ = 'Drago'

from tkinter import *

class View():
    def __init__(self,parent):
        self.root = Tk()
        self.parent = parent
        self.currentFrame = None
        self.frameLogin = FrameLogin(self, self.root, width=400, height=100)
        self.frameSwapper(self.frameLogin)
    
    def frameSwapper(self, frame):
        if (self.currentFrame):
            self.currentFrame.pack_forget()
        frame.pack()
        self.currentFrame = frame
        self.root.title(frame.titleFrame)
      
          
class FrameLogin(Frame):
    def __init__ (self, view, parent, **args):
        Frame.__init__(self, parent, **args)
        self.pack_propagate(False)
        self.parent = parent
        self.view = view
        self.titleFrame="Login"
        
        BACKGROUND_COLOR = "gray70"
        self.config(bg=BACKGROUND_COLOR) 
        
        self.labelName = Label(self, text="User : ", bg=BACKGROUND_COLOR, fg="white")
        self.labelName.pack(side=LEFT)
        self.entryName = Entry(self)
        self.entryName.focus_set()
        self.entryName.pack(side=LEFT)
        
        self.labelPass = Label(self, text="Password : ", bg=BACKGROUND_COLOR, fg="white")
        self.labelPass.pack(side=LEFT)
        self.entryPass = Entry(self, show="*")
        self.entryPass.pack(side=LEFT)
        
        self.ButtonLogin = Button(self, text="Login", command=self.parent.userLogin())
        self.ButtonLogin.pack(side=BOTTOM)
        
    def buttonLogin(self):
        self.view.parent.userLogin(self.entryName.get(), self.entryPass.get())

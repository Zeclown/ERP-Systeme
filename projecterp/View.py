__author__ = 'Drago'
from tkinter import *


class View():
    def __init__(self, parent):
        self.root = Tk()
        self.parent = parent
        self.currentFrame = None
        self.frameLogin = FrameLogin(self, self.root, width=400, height=150)
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
<<<<<<< HEAD:projecterp/View.py
        self.entryPass.pack(side=LEFT)
        
        self.ButtonLogin = Button(self, text="Login", command=self.parent.userLogin())
        self.ButtonLogin.pack(side=BOTTOM)
        
    def buttonLogin(self):
        self.view.parent.userLogin(self.entryName.get(), self.entryPass.get())
=======
        self.entryPass.grid(row=2, column=1, sticky=E)

        self.ButtonLogin = Button(self, text="Login", width=10, command=self.buttonLogin)
        self.ButtonLogin.grid(row=3, column=1, sticky=E)



    def buttonLogin(self):
        self.view.parent.userLogin(self.entryName.get(), self.entryPass.get())

class Controller():
    def __init__(self):
        self.view = View(self)

    def userLogin(self, user, password):
        print(user, password)


c = Controller()
c.view.root.mainloop()
>>>>>>> 0f6531b3e48f04258f99debfe0410a66feaa5e8f:projecterp/View.py

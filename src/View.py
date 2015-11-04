# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import *


class View():
    def __init__(self, parent):
        self.root = Tk()
        self.parent = parent
        self.currentFrame = None
        self.styleCreation()
        self.frameLogin = FrameLogin(self, self.root, "Connexion", width=400, height=150)
        self.frameAcceuil = FrameAcceuil(self, self.root, "Acceuil", width=900, height=500)
        self.frameUsersList=FrameUsersList(self, self.root, "Usagers", width=900, height=500)
        self.frameFormulaire=FrameFormulaire(self, self.root, "Formulaire", width=900, height=500)
        self.frameSwapper(self.frameLogin)
        #self.frameSwapper(self.frameUsersList)
        
    def show(self):
        self.root.mainloop()
    def styleCreation(self):
        self.style=Style()
        self.style.configure("TButton", background="black",foreground="white")
        
    def frameSwapper(self, frame):
        if self.currentFrame:
            self.currentFrame.pack_forget()
        frame.pack(fill=BOTH, expand=True)
        self.currentFrame = frame
        self.root.title(frame.titleFrame)
        self.currentFrame.updateFrame()

class GFrame(Frame):
    BACKGROUND_COLOR = "gray20"
    FORGROUND_COLOR = "white"
    def __init__(self, parentController, parentWindow, title, **args):
        Frame.__init__(self, parentWindow, **args)
        self.parentWindow = parentWindow
        self.parentController = parentController
        self.titleFrame = title
        self.grid_propagate(0)
        self.config()
    def updateFrame(self):
        pass
        
class FrameUsersList(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
        self.label=Label(self,text="Usagers",relief=GROOVE)
        self.label.grid(row=0, column=0, sticky=W,columnspan=2)
        self.listboxUsers = Listbox(self)
        self.listboxUsers.grid(row=1,column=0,columnspan=2,sticky=W+E+N+S)
        self.buttonModify = Button(self,text="Modifier utilisateur")
        self.buttonModify.grid(row=2,column=0,padx=0,sticky=W+E+N+S)
        self.buttonAdd = Button(self,text="Créer utilisateur")
        self.buttonAdd.grid(row=3,column=0,padx=0,sticky=W+E+N+S)
        self.buttonDelete = Button(self,text="Supprimer utilisateur")
        self.buttonDelete.grid(row=4,column=0,padx=0,sticky=W+E+N+S)
        self.frameCreation=Frame(self)
        self.frameCreation.labelTitle=Label(self.frameCreation,text="Nouvel Utilisateur")
        self.frameCreation.labelName=Label(self.frameCreation,text="Nom : ")
        self.frameCreation.labelPassword=Label(self.frameCreation,text="Password : ")
        self.frameCreation.nameVariable=StringVar()
        self.frameCreation.nameVariable.trace("w", lambda name, index, mode,sv=self.frameCreation.nameVariable: self.verifyUserName(sv))
        self.frameCreation.entryName=Label(self.frameCreation,)
    def verifyUserName(self):
        pass
    def newUser(self):
        pass
        
class FrameLogin(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
        
        
        self.label = Label(self)
        self.label.grid(row=0, column=0, sticky=W)


        self.labelName = Label(self, text="Usager : ", width=25, anchor=E)

        self.labelName.grid(row=1, column=0, sticky=E)
        self.entryName = Entry(self)
        self.entryName.focus_set()
        self.entryName.grid(row=1, column=1, sticky=E)

        self.labelPass = Label(self, text="Mot de passe : ",  width=25, anchor=E)
        self.labelPass.grid(row=2, column=0, sticky=E)
        self.entryPass = Entry(self, show="*")
        self.entryPass.grid(row=2, column=1, sticky=E)

        self.ButtonLogin = Button(self, text="Se connecter", width=10,command=self.parentController.parent.userLogin)
        self.ButtonLogin.grid(row=3, column=1, sticky=E)
        
        self.labelWrongPassword = Label(self, text="Le nom d'usager et ou le mot de passe sont invalides")
        self.labelWrongPassword = None
    
    def resetEntries(self):
        self.entryName.delete(0, END)
        self.entryPass.delete(0, END)

class FrameAcceuil(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)    
class FrameFormulaire(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
        
        self.labelTitle = Label(self, text = "Formulaires")
        self.formsListBox = Listbox(self)
        
        for i in self.parentController.parent.getFormsNameList():
            self.formsListBox.insert(END,i)
            
        self.labelTitle.pack()
        self.formsListBox.pack()
   


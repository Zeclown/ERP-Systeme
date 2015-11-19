# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo, askyesno, askquestion, askretrycancel


class View():
    def __init__(self, parent):
        self.root = Tk()
        self.parent = parent
        self.currentFrame = None
        self.styleCreation()
        self.frameLogin = FrameLogin(self, self.root, "Connexion", width=400, height=150)
        self.frameAcceuil = FrameAcceuil(self, self.root, "Acceuil", width=900, height=500)
        self.frameCreateTable=FrameCreateTable(self, self.root, "Create Table", width=900, height=500)
        self.frameLogin.addMenuBar(0)
        self.frameUsersList=FrameUsersList(self, self.root, "Usagers", width=900, height=500)
        self.frameFormulaire=FrameFormulaire(self, self.root, "Formulaire", width=900, height=500)
        self.frameSwapper(self.frameLogin)

    def show(self):
        self.root.mainloop()

    def styleCreation(self):
        self.style=Style()


    
    def showError(self):
        return askretrycancel('Connection au serveur impossible', 'Veuillez vous assure que le serveur est actif')
        

    def frameSwapper(self, frame):
        if self.currentFrame:
            self.currentFrame.pack_forget()
        frame.pack(fill=BOTH, expand=True)
        self.currentFrame = frame
        self.root.title(frame.titleFrame)
        self.currentFrame.updateFrame()

class Styles(Style):
    def __init__(self):
        Style.__init__(self)
    
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
    def addMenuBar(self, showMenuBar):
        self.menuBar = Menu(self.parentWindow, tearoff=0)
        optionMenu = Menu(self.menuBar, tearoff=0)
        optionMenu.add_command(label="Gestion d'usager", command=self.showFrameUsersList)
        optionMenu.add_command(label="Gestion de groupe", command=self.addGroupToDB)
        optionMenu.add_command(label="Gestion de table", command=self.showFrameCreateTable)
        optionMenu.add_command(label="Gestion de formulaire", command=self.showFrameFormulaire)
        optionMenu.add_separator()
        optionMenu.add_command(label="Se deconnecter", command=self.logOutUser)
        optionMenu.add_command(label="Quitter", command = self.parentController.root.destroy)
        self.menuBar.add_cascade(label="Options", menu=optionMenu)
        if showMenuBar:
            self.parentWindow.config(menu=self.menuBar)
    def updateFrame(self):
        pass
            
    def showFrameUsersList(self):
        self.parentController.frameSwapper(self.parentController.frameUsersList)
        
    def showFrameCreateTable(self):
        self.parentController.frameSwapper(self.parentController.frameCreateTable)
    
    def showFrameFormulaire(self):
        self.parentController.frameSwapper(self.parentController.frameFormulaire)
        
    def addGroupToDB(self):
        print("addGroupToDB")
        
    def logOutUser(self):
        self.parentController.frameSwapper( self.parentController.frameLogin )
        self.parentController.frameLogin.entryName.focus()
        self.parentController.frameLogin.resetEntries()

class FrameUsersList(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
        self.frameCreateUser = FrameCreateUser(parentController,self, "Cree un usager", width=400, height=300)
        self.label=Label(self,text="Usagers",relief=GROOVE)
        self.label.grid(row=0, column=0, sticky=W,columnspan=2)
        self.listboxUsers = Listbox(self)
        self.listboxUsers.grid(row=1,column=0,columnspan=2,sticky=W+E+N+S)
        self.buttonModify = Button(self,text="Modifier utilisateur")
        self.buttonModify.grid(row=2,column=0,padx=0,sticky=W+E+N+S)
        self.buttonAdd = Button(self,text="Créer utilisateur", command=lambda: self.frameCreateUser.setUserCreationTextFieldState('normal'))
        self.buttonAdd.grid(row=3,column=0,padx=0,sticky=W+E+N+S)
        self.buttonDelete = Button(self,text="Supprimer utilisateur")
        self.buttonDelete.grid(row=4,column=0,padx=0,sticky=W+E+N+S)

        self.frameCreation=Frame(self)
        self.frameCreateUser.grid(column=2,row=1)

        self.refreshUserListe()




        #print(self.parentController.parent.getUsers())

    def refreshUserListe(self):
        listofUsers = self.parentController.parent.getUsers()
        nameOfUsers = []

        for i in range (len(listofUsers)):
            nameOfUsers.append(listofUsers[i][1])

        print("NOM D'USAGER: ", nameOfUsers)

        for i in nameOfUsers:
            self.listboxUsers.insert(END,i)


    def verifyUserName(self):
        pass

    def newUser(self):
        pass

class FrameCreateUser(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
        
        self.label = Label(self)
        self.label.grid(row=0, column=0, sticky=W)
        
        self.labelNameAccount = Label(self, text="Nom de compte : ", width=25, anchor=E)
        self.labelNameAccount.grid(row=1, column=0, sticky=E)
        self.entryNameAccount = Entry(self, state='disable')
        self.entryNameAccount.focus_set()
        self.entryNameAccount.grid(row=1, column=1, sticky=E)
        
        self.labelPass = Label(self, text="Mot de passe : ",  width=25, anchor=E)
        self.labelPass.grid(row=2, column=0, sticky=E)
        self.entryPass = Entry(self, show="*", state='disable')
        self.entryPass.grid(row=2, column=1, sticky=E)
        
        self.labelPassConfirm = Label(self, text="Confirmer le mot de passe : ",  width=25, anchor=E)
        self.labelPassConfirm.grid(row=3, column=0, sticky=E)
        self.entryPassConfirm = Entry(self, show="*", state='disable')
        self.entryPassConfirm.grid(row=3, column=1, sticky=E)
        
        self.labelGroup = Label(self, text="Groupe d'usagers : ", width=25, anchor=E)
        self.labelGroup.grid(row=4, column=0, sticky=E)
        self.comboBoxGroup = Combobox(self, text="Admin", state='disable')
        self.comboBoxGroup.grid(row=4, column=1, sticky=E)
        
        self.labelSurname = Label(self, text="Nom : ", width=25, anchor=E)
        self.labelSurname.grid(row=5, column=0, sticky=E)
        self.entrySurname = Entry(self, state='disable')
        self.entrySurname.grid(row=5, column=1, sticky=E)
        
        self.labelName = Label(self, text="Prenom : ", width=25, anchor=E)
        self.labelName.grid(row=6, column=0, sticky=E)
        self.entryName = Entry(self, state='disable')
        self.entryName.grid(row=6, column=1, sticky=E)

        self.ButtonCreate = Button(self, text="Crée", width=10,state='disable', command=self.parentController.parent.createUser)
        self.ButtonCreate.grid(row=7, column=0, sticky=E,ipady = 5, pady = 15)
        
        self.ButtonCancel = Button(self, text="Annuler", width=10, state='disable', command=lambda: self.setUserCreationTextFieldState('disable'))
        self.ButtonCancel.grid(row=7, column=1, sticky=E, ipady = 5, pady = 15)
        


    def setUserCreationTextFieldState(self,widgetState): #normal or disable

        self.entryNameAccount.configure(state = widgetState)
        self.entryPass.configure(state = widgetState)
        self.entryPassConfirm.configure(state = widgetState)
        self.comboBoxGroup.configure(state = widgetState)
        self.entrySurname.configure(state = widgetState)
        self.entryName.configure(state = widgetState)
        self.ButtonCreate.configure(state = widgetState)
        self.ButtonCancel.configure(state = widgetState)

        
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
        self.entryPass.bind("<Return>", self.callBackLogIn)

        self.ButtonLogin = Button(self, text="Se connecter", width=13,command=self.parentController.parent.userLogin)
        self.ButtonLogin.grid(row=3, column=1, sticky=E, ipady = 5, pady = 10)
        
        self.labelWrongPassword = Label(self, text="Le nom d'usager et ou le mot de passe sont invalides")
        self.labelWrongPassword = None
    
    def showErrorMsg(self, msg):
        labelErrorMsg = Label(self, text= msg)
        labelErrorMsg.grid(row=4, columnspan=2, sticky=E)

    def callBackLogIn(self,evt):
        self.parentController.parent.userLogin()
    
    def resetEntries(self):
        self.entryName.delete(0, END)
        self.entryPass.delete(0, END)

class FrameAcceuil(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
        GFrame.addMenuBar(self, 1)
    
        
class FrameFormulaire(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
        
        self.labelForms = Label(self, text = "Formulaires de la base de donnee")
        self.labelForms.grid(row=0, column=0)
        self.formsListBox = Listbox(self)

        for i in self.parentController.parent.getFormsNameList():
            self.formsListBox.insert(END,i)

        self.formsListBox.grid(row=1, column=0)
        self.showAllFormsInListView()
            
        self.labelTable = Label(self, text="Tables de la base de donnee")
        self.labelTable.grid(row=0, column=1)
        self.tablesTreeView = Treeview(self)
        self.tablesTreeView.grid(row=1, column=1)
        self.showAllTablesInTreeView()

    def showAllTablesInTreeView(self):
        count = 0;
        for i in self.parentController.parent.getAllTables():
            self.tablesTreeView.insert("", count, i, text=i)
            self.tablesTreeView.insert(i, count, text="Sub Item Table")
            count+=1
           
    def showAllFormsInListView(self):
        for i in self.parentController.parent.getFormsNameList():
            self.formsListBox.insert(END,i)
        
                
class FrameCreateTable(GFrame):
    def __init__(self,parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
        GFrame.addMenuBar(self, 1)
        self.types=["number","string"]
        self.createButton=Button(self, text="Ajouter Table", width=15,command=self.createTable)  
        self.addColumnButton=Button(self, text="Ajouter Colonne", width=15,command=self.addColumn)      
        self.listboxColumns=Treeview(self, selectmode="extended",columns=("Type"))        
        self.entryColumnName=Entry(self)
        self.labelColumnName=Label(self, text="Nouvelle Colonne : ",  width=25, anchor=W);
        self.comboBoxType=Combobox(self,values=self.types);
        self.labelTableName=Label(self, text="Nom de la table : ",  width=25, anchor=W);
        self.entryTableName=Entry(self)
        
        self.listboxColumns.heading("#0", text="Nom de colonne",anchor=W)
        self.listboxColumns.heading("Type", text="Type",anchor=W)
        self.labelType=Label(self, text="Type de la colonne : ",  width=25, anchor=W);
        self.comboBoxType.config(state="readonly")
        self.currentTable={}
        
        self.labelTableName.grid(column=0,row=0)
        self.entryTableName.grid(column=1,row=0)
        self.labelColumnName.grid(column=0,row=1)
        self.entryColumnName.grid(column=1,row=1)
        self.labelType.grid(column=2,row=1)
        self.comboBoxType.grid(column=3,row=1)
        self.addColumnButton.grid(column=4,row=1)
        self.listboxColumns.grid(column=0,row=2,columnspan=2) 
        self.createButton.grid(column=0,row=4)
        
        
        
    def addColumn(self):
        self.listboxColumns.insert("", END,    text=self.entryColumnName.get(), values=(self.comboBoxType.get()))
        
        self.currentTable[self.entryColumnName.get()]=self.comboBoxType.get()
        self.entryColumnName.config(text="")
        self.comboBoxType.index(0)
    def createTable(self):
        self.parentController.parent.model.createTable(self.entryTableName.get(),self.currentTable)
        self.entryColumnName.delete(0, END)
        self.entryTableName.delete(0,END)
        self.listboxColumns.delete(0, END)
        self.listboxTypes.delete(0, END)


# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.tix import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo, askyesno, askquestion, askretrycancel




class View():
    def __init__(self, parent):
        self.root = Tk()
        self.parent = parent
        self.currentFrame = None
        self.styleCreation()
        self.frameLogin = FrameLogin(self, self.root, "Connexion", width=400, height=150)
        #self.frameAcceuil = FrameAcceuil(self, self.root, "Acceuil", width=900, height=500)
        #self.frameCreateTable=FrameCreateTable(self, self.root, "Tables", width=900, height=500)
        self.frameLogin.addMenuBar(0)
        #self.frameGroups=FrameGroups(self, self.root, "Groupes", width=900, height=500)
        #self.frameUsersList=FrameUsersList(self, self.root, "Usagers", width=900, height=500)
        #self.frameFormulaire=FrameFormulaire(self, self.root, "Formulaire", width=900, height=500)
        self.frameSwapper(self.frameLogin)


    def initFrames(self):
        self.frameLogin = FrameLogin(self, self.root, "Connexion", width=400, height=150)
        self.frameAcceuil = FrameAcceuil(self, self.root, "Acceuil", width=900, height=500)
        self.frameCreateTable=FrameCreateTable(self, self.root, "Tables", width=900, height=500)
        self.frameGroups=FrameGroups(self, self.root, "Groupes", width=900, height=500)
        self.frameUsersList=FrameUsersList(self, self.root, "Usagers", width=900, height=500)
        self.frameFormulaire=FrameFormulaire(self, self.root, "Formulaire", width=900, height=500)
    def show(self):
        self.root.mainloop()

    def styleCreation(self):
        self.style=Style()



    def showError(self,titre,message):
        return askretrycancel(titre, message)


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
        self.menuBar.add_cascade(label="Modules", menu=optionMenu)
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
        self.parentController.frameSwapper(self.parentController.frameGroups)
        
    def logOutUser(self):
        self.parentController.frameSwapper( self.parentController.frameLogin )
        self.parentController.frameLogin.entryName.focus()
        self.parentController.frameLogin.resetEntries()

class FrameUsersList(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
        self.frameCreateUser = FrameCreateUser(parentController,self, "Cree un usager", width=400, height=300)
        self.label=Label(self,text="Usagers", width = 10, font = ("Bell Gothic Std Black", 18))
        self.label.grid(row=0, column=0, sticky=W,columnspan=2, pady = 5, padx = 5)
        self.listboxUsers = Listbox(self)
        self.listboxUsers.bind('<<ListboxSelect>>', self.selectListBoxItem)
        self.listboxUsers.grid(row=1,column=0,columnspan=2,sticky=W+E+N+S)
        self.buttonModify = Button(self,text="Modifier utilisateur", command=lambda: self.frameCreateUser.setUserCreationTextFieldState('normal'))
        self.buttonModify.grid(row=2,column=0,padx=0,sticky=W+E+N+S)
        self.buttonAdd = Button(self,text="Créer utilisateur", 
        command=lambda: self.combine_funcs(self.frameCreateUser.setUserCreationTextFieldState('normal'),
                                           self.frameCreateUser.clearUserCreationTextFields()))
        self.buttonAdd.grid(row=3,column=0,padx=0,sticky=W+E+N+S)
        
        self.buttonDelete = Button(self,text="Supprimer utilisateur", command=lambda:
                                   self.combine_funcs(self.parentController.parent.deleteUser(self.listboxUsers.get(self.listboxUsers.curselection())),
                                                      self.refreshUsersInList() ))

        self.buttonDelete.grid(row=4,column=0,padx=0,sticky=W+E+N+S)

        self.frameCreation=Frame(self)
        self.frameCreateUser.grid(column=2,row=1)

        self.refreshUsersInList()


    def refreshCurrentlySelectedUser(self,index):
        listofUsers = self.parentController.parent.getUsers()
        nameOfUserToRefresh = listofUsers[index][1]
        self.frameCreateUser.stringVarEntryName.set(nameOfUserToRefresh)
        self.frameCreateUser.stringVarEntryPass.set(listofUsers[index][2])
        self.frameCreateUser.stringVarGroupeUsager.set("Test comboBox StringVar()")
        self.frameCreateUser.stringVarEntrySurname.set(listofUsers[index][4])
        self.frameCreateUser.stringVarEntryNameOfUser.set(listofUsers[index][5])




        print("USER TO REFRESH" , listofUsers[index])


    def selectListBoxItem(self,evt):
        selectedListBox = evt.widget
        index = int(selectedListBox.curselection()[0])
        value = selectedListBox.get(index)
        self.refreshCurrentlySelectedUser(index)
        print("INDEX: ", index, "VALEUR:", value)

    def refreshUsersInList(self):
        self.listboxUsers.delete(0,END)
        listofUsers = self.parentController.parent.getUsers()
        nameOfUsers = []

        for i in range (len(listofUsers)):
            nameOfUsers.append(listofUsers[i][1])

        print("NOM D'USAGER: ", nameOfUsers)

        for i in nameOfUsers:
            self.listboxUsers.insert(END,i)
            
    def combine_funcs(self,*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func

    def verifyUserName(self):
        pass

    def newUser(self):
        pass

class FrameCreateUser(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
       
        self.labelNameAccount = Label(self, text="Nom de compte : ", width=25, anchor=E)
        self.labelNameAccount.grid(row=1, column=0, sticky=E)
        self.stringVarEntryName = StringVar()
        self.entryNameAccount = Entry(self, state='disable', textvariable = self.stringVarEntryName)
        self.entryNameAccount.focus_set()
        self.entryNameAccount.grid(row=1, column=1, sticky=E)
        
        self.labelPass = Label(self, text="Mot de passe : ",  width=25, anchor=E)
        self.labelPass.grid(row=2, column=0, sticky=E)
        self.stringVarEntryPass = StringVar()
        self.entryPass = Entry(self, show="*", state='disable', textvariable = self.stringVarEntryPass)
        self.entryPass.grid(row=2, column=1, sticky=E)
        
        self.labelPassConfirm = Label(self, text="Confirmer le mot de passe : ",  width=25, anchor=E)
        self.labelPassConfirm.grid(row=3, column=0, sticky=E)
        self.entryPassConfirm = Entry(self, show="*", state='disable', textvariable = self.stringVarEntryPass)
        self.entryPassConfirm.grid(row=3, column=1, sticky=E)
        
        self.labelGroup = Label(self, text="Groupe d'usagers : ", width=25, anchor=E)
        self.labelGroup.grid(row=4, column=0, sticky=E)
        self.stringVarGroupeUsager = StringVar()
        self.comboBoxGroup = Combobox(self, text="Admin", state='disable', textvariable = self.stringVarGroupeUsager)

        self.comboBoxGroup.grid(row=4, column=1, sticky=E)
        
        self.labelSurname = Label(self, text="Nom : ", width=25, anchor=E)
        self.labelSurname.grid(row=5, column=0, sticky=E)
        self.stringVarEntrySurname = StringVar()
        self.entrySurname = Entry(self, state='disable', textvariable = self.stringVarEntrySurname)
        self.entrySurname.grid(row=5, column=1, sticky=E)
        
        self.labelName = Label(self, text="Prenom : ", width=25, anchor=E)
        self.labelName.grid(row=6, column=0, sticky=E)
        self.stringVarEntryNameOfUser = StringVar()
        self.entryName = Entry(self, state='disable', textvariable = self.stringVarEntryNameOfUser)
        self.entryName.grid(row=6, column=1, sticky=E)

        self.ButtonCreate = Button(self, text="Crée", width=10,state='disable', command=lambda:
                                   self.combine_funcs(self.parentController.parent.createUser(),
                                                      self.parentWindow.refreshUsersInList()))
        self.ButtonCreate.grid(row=7, column=0, sticky=E,ipady = 5, pady = 15)
        
        self.ButtonCancel = Button(self, text="Annuler", width=10, state='disable', command=lambda: 
                                   self.setUserCreationTextFieldState('disable'))
        
        self.ButtonCancel.grid(row=7, column=1, sticky=E, ipady = 5, pady = 15)

        self.widgetUserCreation = [
            self.entryNameAccount,
            self.entryPass,
            self.entryPassConfirm,
            self.comboBoxGroup,
            self.entrySurname,
            self.entryName,
            self.ButtonCreate,
            self.ButtonCancel,
        ]

    def addItemsToComboBox(self):
        pass
    
    def combine_funcs(self,*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func

    def clearUserCreationTextFields(self):
        self.stringVarEntryName.set("")
        self.stringVarEntryPass.set("")
        self.stringVarGroupeUsager.set("")
        self.stringVarEntrySurname.set("")
        self.stringVarEntryNameOfUser.set("")

    def setUserCreationTextFieldState(self,widgetState): #'normal' or 'disable'

        for i in self.widgetUserCreation:
            i.configure(state = widgetState)

        
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
        self.formsListBox.grid(row=1, column=0)
        self.showAllFormsInListView()
            
        self.labelTable = Label(self, text="Tables de la base de donnee")
        self.labelTable.grid(row=0, column=1)
        self.tablesTreeView = Treeview(self)
        self.tablesTreeView.grid(row=1, column=1)
        self.showAllTablesInTreeView()

        self.buttonAdd = Button(self, text=">", width=3)
        self.buttonAdd.grid(rowspan=1, column=2)
        self.buttonRemove = Button(self, text="<", width=3)
        self.buttonRemove.grid(rowspan=1, column=2)

        self.labelNameForm = Label(self, text="Nom du formulaire : ")
        self.labelNameForm.grid(row=0, column=3)
        self.entryNameForm = Entry(self)
        self.entryNameForm.grid(row=0, column=4)



    def showAllTablesInTreeView(self):
        count = 0
        for i in self.parentController.parent.getAllTables():
            self.tablesTreeView.insert("", count, i, text=i)
            for j in self.parentController.parent.getTableColumnName(i):
                self.tablesTreeView.insert(i, count, text=j)
                count+=1
           
    def showAllFormsInListView(self):
        for i in self.parentController.parent.getFormsNameList():
            self.formsListBox.insert(END,i)

class FrameGroups(GFrame):
    def __init__(self,parentController,parentWindow,title,**args):

        GFrame.__init__(self, parentController, parentWindow, title, **args)
        self.labelNameGroup = Label(self, text="Nom de groupe  ", width=25, anchor=W)
        self.labelNameGroup.grid(row=0, column=2, sticky=W)
        self.stringVarEntryName = StringVar()
        self.entryNameAccount = Entry(self, state='disable', textvariable = self.stringVarEntryName)
        self.entryNameAccount.focus_set()
        self.entryNameAccount.grid(row=0, column=3, sticky=W)
        self.labelNiveau = Label(self, text="Niveau de sécurité  ", width=25, anchor=W)
        self.labelNiveau.grid(row=1, column=2, sticky=W)
        self.stringVarLevel = StringVar()
        self.comboBoxLevel = Combobox(self, text="0", state='disable', textvariable = self.stringVarLevel)
        self.comboBoxLevel.grid(row=1, column=3, sticky=W)
        self.buttonModif = Button(self, text="Sauvegarder", width=10,state='disable', command=self.saveGroup)
        self.buttonModif.grid(row=4, column=2, sticky=N,ipady = 5, pady = 15)
        self.buttonCancel = Button(self, text="Annuler", width=10, state='disable', command=self.cancel)
        self.buttonCancel.grid(row=4, column=3, sticky=N, ipady = 5, pady = 15)
        self.listboxGroups=Listbox(self)
        self.listboxGroups.grid(column=0,row=1,rowspan=2,columnspan=2)
        self.buttonCreate=Button(self,text="Create", width=10, state='enable', command=self.createGroup)
        self.buttonCreate.grid(column=0,row=4,sticky=N, ipady = 5, pady = 15)
        self.labelGroups=Label(self,text="Groupes")
        self.labelGroups.grid(column=0,row=0)
        self.permissionCheckList=CheckList(self)
        self.permissionCheckList.grid(row=2,column=2,columnspan=2,sticky=E+W+S+N)
        self.permissionCheckList.hlist.add("CL1", text="Modification d'usagers")
        self.permissionCheckList.hlist.add("CL2", text="Lecture d'usagers")
        self.permissionCheckList.hlist.add("CL3", text="Modification de groupes")
        self.permissionCheckList.setstatus("CL1", "off")
        self.permissionCheckList.setstatus("CL2", "off")
        self.permissionCheckList.setstatus("CL3", "off")
        self.permissionCheckList.autosetmode()
        
        self.widgetActivate=[self.permissionCheckList,self.buttonCancel,self.buttonCreate]#liste des widget a activer a la modification
        self.widgetDeactivate=[self.buttonModif]
        #configure(state = widgetState)

    def activateModifs(self):
        for widg in self.widgetActivate:
            widg.config(state="enable")
        for widg in self.widgetDeactivate:
            widg.config(state="disable")   
    def deactivateModifs(self):
        for widg in self.widgetActivate:
            widg.config(state="disable")
        for widg in self.widgetDeactivate:
            widg.config(state="enable")
    def updateFrame(self):
        GFrame.update(self)
        self.listboxGroups.delete(0, END)
        print(self.parentController.parent.getGroups())
        #for groups in self.parentController.getGroups():
            #self.listboxGroups
    def createGroup(self):
        pass     
    def selectItem(self):
        pass
    def cancel(self):
        self.setUserCreationTextFieldState("disable")
    def saveGroup(self):
        self.parentController.saveGroup();
class FrameCreateTable(GFrame):
    def __init__(self,parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
        GFrame.addMenuBar(self, 1)
        self.types=["number","string"]
        self.listboxTables=Listbox(self)
        self.listboxTables.bind('<<ListboxSelect>>', self.selectTable)
        self.labelTables=Label(self, text="Tables",  width=25, anchor=W);
        self.modifyTableButton=Button(self,text="Modifier la table",width=15,command=self.activateModify)
        self.createButton=Button(self, text="Sauvegarder", width=15,command=self.createTable)
        self.cancelButton= Button(self, text="Annuler", width=15,command=self.cancelTable) 
        self.addColumnButton=Button(self, text="Ajouter Colonne", width=15,command=self.addColumn) 
        self.deleteColumnButton=Button(self,text="Supprimer Colonne",width=15,command=self.deleteColumn)     
        self.treeviewColumns=Treeview(self, selectmode="extended",columns=("Type"))        
        self.entryColumnName=Entry(self)
        self.labelColumnName=Label(self, text="Nouvelle Colonne : ",  width=25, anchor=W);
        self.comboBoxType=Combobox(self,values=self.types);
        self.labelTableName=Label(self, text="Nom de la table : ",  width=25, anchor=W);
        self.entryTableName=Entry(self)
        
        self.treeviewColumns.heading("#0", text="Nom de colonne",anchor=W)
        self.treeviewColumns.heading("Type", text="Type",anchor=W)
        self.labelType=Label(self, text="Type de la colonne : ",  width=25, anchor=W);
        self.comboBoxType.config(state="readonly")
        self.currentTable={}
        
        self.labelTables.grid(column=0,row=0)
        self.listboxTables.grid(column=0,row=1,rowspan=3,padx=30)
        self.labelTableName.grid(column=1,row=0)
        self.entryTableName.grid(column=2,row=0)
        self.labelColumnName.grid(column=1,row=1)
        self.entryColumnName.grid(column=2,row=1)
        self.labelType.grid(column=1,row=2)
        self.comboBoxType.grid(column=2,row=2)
        self.addColumnButton.grid(column=3,row=2)
        self.deleteColumnButton.grid(column=3,row=1)
        self.treeviewColumns.grid(column=1,row=3,columnspan=2) 
        self.createButton.grid(column=1,row=4)
        self.modifyTableButton.grid(column=0,row=4)
        self.cancelButton.grid(column=2,row=4)
        self.deactivateModify()
        self.showAllTablesInListbox()
    def selectTable(self,evt):
        self.entryTableName.insert(0, self.listboxTables.get(ACTIVE))
    def updateFrame(self):
        GFrame.updateFrame(self)
        self.showAllTablesInListbox()
    def showAllTablesInListbox(self): 
        self.listboxTables.delete(0, END)     
        for i in self.parentController.parent.getAllTables():
            self.listboxTables.insert(END, i)

    def activateModify(self):
        self.addColumnButton['state']='normal'
        self.modifyTableButton['state']='disabled'
        self.comboBoxType['state']='normal'
        self.deleteColumnButton['state']='normal'
        self.createButton['state']='normal'
        self.entryTableName['state']='normal'
        self.entryColumnName['state']='normal'
        self.cancelButton['state']='normal'
    def deactivateModify(self):
        self.addColumnButton['state']='disabled'
        self.modifyTableButton['state']='normal'
        self.comboBoxType['state']='disabled'
        self.deleteColumnButton['state']='disabled'
        self.createButton['state']='disabled'
        self.entryTableName['state']='disabled'
        self.entryColumnName['state']='disabled'
        self.cancelButton['state']='disabled'

    def cancelTable(self):
        self.entryColumnName.delete(0, END)
        self.entryTableName.delete(0,END)
        self.treeviewColumns.delete(*self.treeviewColumns.get_children())
        self.currentTable.clear()
        self.deactivateModify()
        
    def addColumn(self):
        self.treeviewColumns.insert("", END,    text=self.entryColumnName.get(), values=(self.comboBoxType.get()))       
        self.currentTable[self.entryColumnName.get()]=self.comboBoxType.get()
        self.entryColumnName.config(text="")
        self.comboBoxType.index(0)
    def deleteColumn(self):
        curItem = self.treeviewColumns.focus()
        self.currentTable.pop(self.listboxColumns.item(curItem)['text'],None)
        
        self.treeviewColumns.delete(curItem)
         
    def createTable(self):
        self.parentController.parent.model.createTable(self.entryTableName.get(),self.currentTable)
        self.entryColumnName.delete(0, END)
        self.entryTableName.delete(0,END)
        self.treeviewColumns.delete(*self.treeviewColumns.get_children())
        self.currentTable.clear()
        self.deactivateModify()

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.tix import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo, askyesno, askquestion, askretrycancel
from Users import *


class View():
    def __init__(self, parent):
        self.root = Tk()
        self.parent = parent
        self.currentFrame = None
        self.styleCreation()
        self.frameLogin = FrameLogin(self, self.root, "Connexion - ERP", width=450, height=280)
        self.root.resizable(0,0)
        self.frameSwapper(self.frameLogin)
        self.root.iconbitmap('icon_erp.ico')
    def login(self):
        self.showLogin()
        self.frameSwapper(self.frameAccueil)
    def initFrames(self):
        self.frameCronJobs = FrameCronJobs(self, self.root, "Jobs chronologiques", width=950, height=500)
        self.frameAccueil = FrameAccueil(self, self.root, "Accueil", width=900, height=500)
        self.frameCreateTable=FrameCreateTable(self, self.root, "Tables", width=900, height=500)
        self.frameGroups=FrameGroups(self, self.root, "Groupes", width=900, height=500)
        self.frameUsersList=FrameUsersList(self, self.root, "Usagers", width=900, height=500)
        self.frameFormulaire=FrameFormulaire(self, self.root, "Formulaire", width=900, height=500)
        self.frameDisplayForm = FrameDisplayForm(self, self.root, "Consulter Formulaire", width=900, height=500)
    def showLogin(self):
        self.menuBar = Menu(self.root, tearoff=0)
        optionMenu = Menu(self.menuBar, tearoff=0)
        optionMenu.add_command(label="Gestion d'usager", command=self.currentFrame.showFrameUsersList)
        optionMenu.add_command(label="Gestion de groupe", command=self.currentFrame.addGroupToDB)
        optionMenu.add_command(label="Gestion de table", command=self.currentFrame.showFrameCreateTable)
        optionMenu.add_command(label="Gestion de formulaire", command=self.currentFrame.showFrameFormulaire)
        optionMenu.add_command(label="Afficher un formulaire", command=self.currentFrame.showFrameDisplayForm)
        optionMenu.add_command(label="Gestion de cron jobs", command=self.currentFrame.showFrameCronJobs)
        optionMenu.add_separator()
        optionMenu.add_command(label="Se deconnecter", command=self.currentFrame.logOutUser)
        optionMenu.add_command(label="Quitter", command = self.root.destroy)
        self.menuBar.add_cascade(label="Modules", menu=optionMenu)
        self.root.config(menu=self.menuBar)
    def hideLogin(self):
        self.root.destroy()
        self.__init__(self.parent)
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
        pass

    def updateFrame(self):
        pass

    def showFrameCronJobs(self):
        self.parentController.frameCronJobs = FrameCronJobs(self.parentController, self.parentController.root, "Jobs chronologiques", width=950, height=500)
        self.parentController.frameSwapper(self.parentController.frameCronJobs)

    def showFrameUsersList(self):
        self.parentController.frameUsersList=FrameUsersList(self.parentController, self.parentController.root, "Usagers", width=900, height=500)
        self.parentController.frameSwapper(self.parentController.frameUsersList)
        
    def showFrameCreateTable(self):
        self.parentController.frameCreateTable=FrameCreateTable(self.parentController, self.parentController.root, "Tables", width=900, height=500)
        self.parentController.frameSwapper(self.parentController.frameCreateTable)
    
    def showFrameFormulaire(self):
        self.parentController.frameFormulaire=FrameFormulaire(self.parentController, self.parentController.root, "Formulaire", width=900, height=500)
        self.parentController.frameSwapper(self.parentController.frameFormulaire)

    def showFrameDisplayForm(self):
        self.parentController.frameDisplayForm = FrameDisplayForm(self.parentController, self.parentController.root, "Consulter Formulaire", width=900, height=500)
        self.parentController.frameSwapper(self.parentController.frameDisplayForm)
        
    def addGroupToDB(self):
        self.parentController.frameGroups=FrameGroups(self.parentController, self.parentController.root, "Groupes", width=900, height=500)
        self.parentController.frameSwapper(self.parentController.frameGroups)
        
    def logOutUser(self):
        self.frameLogin = FrameLogin(self.parentController, self.parentController.root, "Connexion - ERP", width=450, height=280)
        self.parentController.frameSwapper( self.parentController.frameLogin )
        self.parentController.frameLogin.entryName.focus()
        self.parentController.frameLogin.resetEntries()
        self.parentController.hideLogin()


class FrameLogin(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
        fichier = os.path.dirname(sys.argv[0])
        fichier = fichier+"\insertech.gif"
        
        self.imageInsertech = PhotoImage(file = fichier)

        self.labelImageInsertech = Label(self, imag=self.imageInsertech )

        self.label = Label(self, image=self.imageInsertech)
        self.label.grid(row=0, column=0,sticky=W)

        self.labelGreetings = Label(self, text = "Bienvenue!\n\n Veuillez vous connecter pour avoir \n accèss à un monde de possiblitées", font = ("Bell Gothic Std Black", 12))
        self.labelGreetings.grid(row=0,column=1)

        self.labelName = Label(self, text="Usager : ", width=25, anchor=E)
        self.labelName.grid(row=1, column=0,pady = (15,0))
        self.entryName = Entry(self)
        self.entryName.focus_set()
        self.entryName.grid(row=1, column=1, pady = (15,0))

        self.labelPass = Label(self, text="Mot de passe : ",  width=25, anchor=E)
        self.labelPass.grid(row=2, column=0)
        self.entryPass = Entry(self, show="*")
        self.entryPass.grid(row=2, column=1)
        self.entryPass.bind("<Return>", self.callBackLogIn)

        self.ButtonLogin = Button(self, text="Se connecter", width=13, command=lambda:self.parentController.parent.userLogin(self.entryName.get(),self.entryPass.get()))
        self.ButtonLogin.grid(row=3, column=1, sticky=E, ipady = 5, pady = 10)

    def showErrorMsg(self, msg):
        styleError = Style()
        styleError.configure("BW.TLabel",foreground="red")
        labelErrorMsg = Label(self, text = msg, style = "BW.TLabel")
        labelErrorMsg.grid(row=4, columnspan=2, sticky=E)

    def callBackLogIn(self,evt):
        self.parentController.parent.userLogin(self.entryName.get(), self.entryPass.get())

    def resetEntries(self):
        self.entryName.delete(0, END)
        self.entryPass.delete(0, END)
        self.entryName.focus_set()


class FrameAccueil(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
        GFrame.addMenuBar(self, 1)
        self.labelWelcome = Label(self, text="Bienvenue "+"!", font = ("Bell Gothic Std Black", 12))
        self.labelWelcome.grid()


class FrameUsersList(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
        self.frameCreateUser = FrameCreateUser(parentController,self, "Cree un usager", width=400, height=300)
        self.label=Label(self,text="Usagers", width = 10, font = ("Bell Gothic Std Black", 18))
        self.label.grid(row=0, column=0, sticky=W,columnspan=2, pady = 5, padx = 5)
        self.listboxUsers = Listbox(self)
        self.listboxUsers.bind('<<ListboxSelect>>', self.selectListBoxItem)
        self.scrollBarListUsers = Scrollbar(self)

        self.currentListBoxSelection = None
        self.listboxUsers.grid(row=1,column=0,columnspan=2,sticky=W+E+N+S)

        self.scrollBarListUsers.grid(row=1,column=1,sticky=W+E+N+S)
        self.listboxUsers.config(yscrollcommand = self.scrollBarListUsers.set)
        self.scrollBarListUsers.config(command = self.listboxUsers.yview)

        self.buttonModify = Button(self,text="Modifier utilisateur", command=self.buttonModifyToDo)
        self.buttonModify.grid(row=2,column=0,padx=0,sticky=W+E+N+S)
        self.buttonAdd = Button(self,text="Créer utilisateur", command=self.buttonCreateUserTodo)
        self.buttonAdd.grid(row=3,column=0,padx=0,sticky=W+E+N+S)
        self.buttonDelete = Button(self,text="Supprimer utilisateur", command=self.buttonDeleteUserToDo )
        self.buttonDelete.grid(row=4,column=0,padx=0,sticky=W+E+N+S)
        self.frameCreation=Frame(self)
        self.frameCreateUser.grid(column=2,row=1)

        self.refreshUsersInList()
        self.userToModify = None
        self.usernameArray = self.parentController.parent.getUsers()

    def buttonCreateUserTodo(self):
        self.frameCreateUser.setUserCreationTextFieldState('normal')
        self.frameCreateUser.clearUserCreationTextFields()
        self.refreshUserNameArray()

    def buttonDeleteUserToDo(self):
        if self.currentListBoxSelection:
            self.parentController.parent.deleteUser(self.listboxUsers.get(self.listboxUsers.curselection()))
            self.refreshUsersInList()
            self.frameCreateUser.clearUserCreationTextFields()
            self.refreshUserNameArray()
            self.currentListBoxSelection = None
        else:
            self.parentController.showError("Aucune selection","Veuillez svp faire une selection")

    def buttonModifyToDo(self):
        if self.currentListBoxSelection:
            self.frameCreateUser.setUserCreationTextFieldState('normal')
            self.userToModify = self.frameCreateUser.stringVarEntryName.get()
            self.frameCreateUser.ButtonCreate.grid_forget()
            self.frameCreateUser.buttonConfirmModification.grid(row=7, column=0, sticky=E,ipady = 5, pady = 15)
        else:
            self.parentController.showError("Aucune selection","Veuillez svp faire une selection")

    def createUserObjectToSendToController(self):

        username = self.frameCreateUser.stringVarEntryName.get()
        password = self.frameCreateUser.stringVarEntryPass.get()
        groupe = self.frameCreateUser.stringVarGroupeUsager.get()
        firstname = self.frameCreateUser.stringVarEntryNameOfUser.get()
        lastname = self.frameCreateUser.stringVarEntrySurname.get()

        newUser = User(username,password,groupe,firstname,lastname)
        return newUser

    def buttonConfirmitationTodo(self):

        self.parentController.parent.deleteUser(self.userToModify)
        self.parentController.parent.createUser(self.createUserObjectToSendToController())
        self.refreshUsersInList()
        self.refreshUserNameArray()
        self.frameCreateUser.buttonConfirmModification.grid_forget()
        self.frameCreateUser.ButtonCreate.grid(row=7, column=0, sticky=E,ipady = 5, pady = 15)
        self.frameCreateUser.setUserCreationTextFieldState('disable')
        self.currentListBoxSelection = None

    def refreshUserNameArray(self): #to refresh, when needed the local data struct of users that was feteched by query getUsers()
        self.usernameArray = self.parentController.parent.getUsers()

    def refreshCurrentlySelectedUser(self,index):
        nameOfUserToRefresh = self.usernameArray[index][1]
        self.frameCreateUser.stringVarEntryName.set(nameOfUserToRefresh)
        self.frameCreateUser.stringVarEntryPass.set(self.usernameArray[index][2])
        self.frameCreateUser.stringVarGroupeUsager.set(self.usernameArray[index][3])
        self.frameCreateUser.stringVarEntryNameOfUser.set(self.usernameArray[index][4])
        self.frameCreateUser.stringVarEntrySurname.set(self.usernameArray[index][5])

    def selectListBoxItem(self,evt):
        selectedListBox = evt.widget
        index = int(selectedListBox.curselection()[0])
        value = selectedListBox.get(index)
        self.currentListBoxSelection = value
        self.refreshCurrentlySelectedUser(index)

    def refreshUsersInList(self):
        self.listboxUsers.delete(0,END)
        listofUsers = self.parentController.parent.getUsers()
        nameOfUsers = []

        for i in range (len(listofUsers)):
            nameOfUsers.append(listofUsers[i][1])

        for i in nameOfUsers:
            self.listboxUsers.insert(END,i)

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
        self.entryNameAccount.grid(row=1, column=1, sticky=W)
        
        self.labelPass = Label(self, text="Mot de passe : ",  width=25, anchor=E)
        self.labelPass.grid(row=2, column=0, sticky=E)
        self.stringVarEntryPass = StringVar()
        self.entryPass = Entry(self, show="*", state='disable', textvariable = self.stringVarEntryPass)
        self.entryPass.grid(row=2, column=1, sticky=W)
        
        self.labelPassConfirm = Label(self, text="Confirmer le mot de passe : ",  width=25, anchor=E)
        self.labelPassConfirm.grid(row=3, column=0, sticky=E)
        self.entryPassConfirm = Entry(self, show="*", state='disable', textvariable = self.stringVarEntryPass)
        self.entryPassConfirm.grid(row=3, column=1, sticky=W)
        
        self.labelGroup = Label(self, text="Groupe d'usagers : ", width=25, anchor=E)
        self.labelGroup.grid(row=4, column=0, sticky=E)
        self.stringVarGroupeUsager = StringVar()
        self.comboBoxGroup = Combobox(self, text="Admin", state='disable', textvariable = self.stringVarGroupeUsager, width = 17)

        self.comboBoxGroup.grid(row=4, column=1, sticky=W)
        
        self.labelSurname = Label(self, text="Nom : ", width=25, anchor=E)
        self.labelSurname.grid(row=5, column=0, sticky=E)
        self.stringVarEntrySurname = StringVar()
        self.entrySurname = Entry(self, state='disable', textvariable = self.stringVarEntrySurname)
        self.entrySurname.grid(row=5, column=1, sticky=W)
        
        self.labelName = Label(self, text="Prenom : ", width=25, anchor=E)
        self.labelName.grid(row=6, column=0, sticky=E)
        self.stringVarEntryNameOfUser = StringVar()
        self.entryName = Entry(self, state='disable', textvariable = self.stringVarEntryNameOfUser)
        self.entryName.grid(row=6, column=1, sticky=W)

        self.ButtonCreate = Button(self, text="Crée", width=10,state='disable', command=self.buttonCreateConfirmToDo)
        self.ButtonCreate.grid(row=7, column=0, sticky=E,ipady = 5, pady = 15)

        self.buttonConfirmModification = Button(self, text = "Accepter", command=self.parentWindow.buttonConfirmitationTodo )
        
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

        self.stringVars = [

            self.stringVarEntryName,
            self.stringVarEntryPass,
            self.stringVarGroupeUsager,
            self.stringVarEntryName,
            self.stringVarEntrySurname
        ]

        self.addItemsToComboBox()

    def buttonCreateConfirmToDo(self):
        self.parentController.parent.createUser(self.parentWindow.createUserObjectToSendToController())
        self.parentWindow.refreshUsersInList()
        self.clearUserCreationTextFields()
        self.setUserCreationTextFieldState('disable')
        self.parentWindow.refreshUserNameArray()
        self.parentWindow.currentListBoxSelection = None

    def clearUserCreationTextFields(self):
        self.stringVarEntryName.set("")
        self.stringVarEntryPass.set("")
        self.stringVarGroupeUsager.set("")
        self.stringVarEntrySurname.set("")
        self.stringVarEntryNameOfUser.set("")

    def addItemsToComboBox(self):
        groups = self.parentController.parent.getGroups()

        nameOfGroups = []

        for i in range (len(groups)):
            nameOfGroups.append(groups[i][1])



        self.comboBoxGroup['values'] = nameOfGroups

    def setUserCreationTextFieldState(self,widgetState): #'normal' or 'disable'

        for i in self.widgetUserCreation:
            i.configure(state = widgetState)


class FrameCronJobs(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)

        self.stringVarNomCronJob = StringVar()
        self.stringVarBusinessRule = StringVar()
        self.stringVarFrequence = StringVar()
        self.regleAffaireDeBase = [ "Envoyé un email", "Faire un backup", "Write log" ]
        self.typeDeTemps = [ "Minute", "Heure", "Semaine", "Mois", "Annee"]
        self.columnsInCronJobTreeView = ( "Nom de la tâche chrnologique", "À faire", "Temps d'exécution", "Statue")


        self.labelNouveauCronJob = Label(self, text= "Nouveau cron job", font = ("Verdana", 16))

        self.labelNomCronJob = Label(self, text="Nom: ")
        self.entryNomCronJob = Entry(self, textvariable=self.stringVarNomCronJob)

        self.labelAFaire = Label(self, text="A faire: ")
        self.comboBoxAFaire = Combobox(self, textvariable=self.stringVarBusinessRule, width = 17, values=self.regleAffaireDeBase, state="readonly")

        self.labelFrequenceBase = Label(self, text="A chaque: ")
        self.entryFrequence = Entry(self, textvariable=self.stringVarFrequence)
        self.comboBoxTypeTime = Combobox(self, values = self.typeDeTemps, state="readonly")
        self.buttonAdvcaned = Button(self, text = "Propriétées avancées")
        #################################################
        #CODER ICI LES WIDGET POUR PROPRIETES AVANCES###
        ################################################

        self.cronjobsTree = Treeview(self, column=self.columnsInCronJobTreeView, show="headings")
        self.cronjobsTree.heading("Nom de la tâche chrnologique", text = "Nom de la tâche chrnologique")
        self.cronjobsTree.heading("À faire", text = "À faire")
        self.cronjobsTree.heading("Temps d'exécution", text = "Temps d'exécution")
        self.cronjobsTree.heading("Statue", text = "Statue")

        self.labelCronJobs = Label(self, text="Cron jobs", font = ("Verdana", 14))

        self.labelNouveauCronJob.grid(row=0,columnspan=2)

        self.labelNomCronJob.grid(row=1,column=0,pady=5, sticky=E)
        self.entryNomCronJob.grid(row=1, column=1, sticky=W)

        self.labelAFaire.grid(row=2,column=0,pady=5, sticky=E)
        self.comboBoxAFaire.grid(row=2,column=1, sticky=W)

        self.labelFrequenceBase.grid(row=3,column=0,pady=5, sticky=E)
        self.entryFrequence.grid(row=3,column=1, sticky=W)
        self.comboBoxTypeTime.grid(row=3,column=1)
        self.buttonAdvcaned.grid(row=3,column=2)

        self.labelCronJobs.grid(row=4)

        self.cronjobsTree.grid(row=5,columnspan=4,pady=(30,0))

class FrameDisplayForm(GFrame):
    def __init__(self, parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)

        self.linkToDataBaseList = []

        self.labelForms = Label(self, text = "Formulaires")
        self.labelForms.grid(row=0, column=0)
        self.formsListBox = Listbox(self)
        self.formsListBox.grid(row=1, column=0)
        self.formsListBox.bind("<Button-1>", self.selectFormInListView)
        self.showAllFormsInListView()

        self.panelForm = Frame(self)
        self.nomFormulaire = Label(self)

        self.buttonSave = Button(self, text="Sauvegarder", width=19, command=self.sauvegarderALaBD)
        self.buttonSave.grid(row=2, column=0)

    def selectFormInListView(self, event):
        selectedListBox = event.widget
        index = selectedListBox.curselection()[0]
        value = selectedListBox.get(index)[0]
        print(value)
        resultFormSpecs = self.parentController.parent.getFormsSpecs(value)
        print(resultFormSpecs)
        self.panelForm.grid_remove()
        self.nomFormulaire.grid_remove()
        self.builtFormsWithSpecList(resultFormSpecs, value)

    def builtFormsWithSpecList(self, specList, name):

        self.nomFormulaire = Label(self, text=name)
        self.nomFormulaire.grid(row=0, column=1)

        self.panelForm = Frame(self)
        self.panelForm.grid(row=1, column=1)

        count = 1
        for row in specList:
            print("----------FORMULAIRE----------")
            print("Table ->", row[0])
            print("Colonne ->", row[1])
            print("Label ->", row[2])
            print("TypeVue ->", row[3])
            print("Valeurs ->", row[4])
            print("Description", row[5])
            print("------------------------------")

            self.linkToDataBaseList.append([row[0], row[1], row[3]])

            self.label = row[2]
            self.typeVue = row[3]
            self.valeurs = row[4]
            self.description = row[5]

            width = 40

            self.label = Label(self.panelForm, text=  self.label)
            self.label.grid(row=count, column=1)
            if self.typeVue ==  "Entry":
                self.entry = Entry(self.panelForm, width=width)
                self.entry.grid(row=count, column=2)
            elif self.typeVue ==  "ComboBox":
                self.comboBox = Combobox(self.panelForm, width=width-3,values=self.valeurs, state="readonly")
                self.comboBox.current(0)
                self.comboBox.grid(row=count, column=2)
            elif self.typeVue ==  "RadioButton":
                self.radioButton = Radiobutton(self.panelForm, width=width)
                self.radioButton.grid(row=count, column=2)
            elif self.typeVue == "Checkbutton":
                self.checkButton = Checkbutton(self.panelForm, width=width)
                self.checkButton.grid(row=count, column=2)
            elif self.typeVue ==  "SpinBox":
                self.spinBox = Spinbox(self.panelForm, width=width)
                self.spinBox.grid(row=count, column=2)

            count+=1
        print(self.linkToDataBaseList)

    def sauvegarderALaBD(self):

        infoEntre = []

        for i in self.linkToDataBaseList:
            if i[2] == "Entry":
                infoEntre.append([i[0], i[1], self.entry.get()])
            elif i[2] == "ComboBox":
                infoEntre.append([i[0], i[1], self.comboBox.get()])

        print("--------------------------")
        print("Info entre ->", infoEntre)
        print("--------------------------")

        self.parentController.parent.insertDateToDB(infoEntre)





    def showAllFormsInListView(self):
        for i in self.parentController.parent.getFormsNameList():
            self.formsListBox.insert(END,i)

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
        self.tablesTreeView.bind("<Double-Button-1>", self.selectTreeViewItem)

        self.buttonAdd = Button(self, text=">", width=3)
        self.buttonAdd.grid(rowspan=1, column=2)
        self.buttonRemove = Button(self, text="<", width=3)
        self.buttonRemove.grid(rowspan=1, column=2)

        self.labelNameForm = Label(self, text="Nom du formulaire : ")
        self.labelNameForm.grid(row=0, column=3)
        self.entryNameForm = Entry(self)
        self.entryNameForm.grid(row=0, column=4)

        self.columns = ("Type du champs", "Nom du champs", "Type du vue", "Valeurs", "Description")
        self.editFormTableView = Treeview(self, columns=self.columns, show="headings",
                                          displaycolumns=("Type du champs", "Nom du champs", "Type du vue"))
        self.editFormTableView.column("Type du champs", width=170)
        self.editFormTableView.heading("Type du champs", text="Type du champs")
        self.editFormTableView.column("Nom du champs", width=100)
        self.editFormTableView.heading('Nom du champs', text="Nom du champs")
        self.editFormTableView.column("Type du vue", width=80)
        self.editFormTableView.heading('Type du vue', text="Type du vue")
        self.editFormTableView.column("Valeurs", width=100)
        self.editFormTableView.heading('Valeurs', text="Valeurs")
        self.editFormTableView.column("Description", width=100)
        self.editFormTableView.heading('Description', text="Description")
        self.editFormTableView.grid(row=1, column=4)
        self.editFormTableView.bind("<Button-1>", self.selectTableViewItem)

        self.labelTypeChamps = Label(self, text="Type du champs : ")
        self.labelTypeChamps.grid(row=2, column=3)
        self.varTypeChamps = StringVar()
        self.entryTypeChamps = Entry(self, textvariable=self.varTypeChamps, state="disable")
        self.entryTypeChamps.grid(row=2, column=4)

        self.labelNomChamps = Label(self, text="Nom du champs : ")
        self.labelNomChamps.grid(row=3, column=3)
        self.varNomChamps = StringVar()
        self.entryNomChamps = Entry(self, textvariable=self.varNomChamps)
        self.entryNomChamps.grid(row=3, column=4)

        self.labelTypeVue = Label(self, text="Type du vue : ")
        self.labelTypeVue.grid(row=4, column=3)
        self.typeVueValues = ["Entry", "ComboBox", "RadioButton", "Checkbutton", "SpinBox"]
        self.comboBoxTypeVue = Combobox(self, values=self.typeVueValues, state="readonly")
        self.comboBoxTypeVue.current(0)
        self.comboBoxTypeVue.grid(row=4, column=4)
        self.comboBoxTypeVue.bind("<<ComboboxSelected>>", self.changeViewType)

        self.labelValuesFromTypeVue = Label(self, text="Valeur à entrez : ")
        self.labelValuesFromTypeVue.grid(row=5, column=3)
        self.varValues = StringVar()
        self.entryValuesFromTypeVue = Entry(self, textvariable=self.varValues, state="disable")
        self.entryValuesFromTypeVue.grid(row=5, column=4)

        self.labelDescription = Label(self, text="Description : ")
        self.labelDescription.grid(row=6, column=3)
        self.varDescription = StringVar()
        self.entryDescription = Entry(self, textvariable=self.varDescription)
        self.entryDescription.grid(row=6, column=4)

        self.buttonDelectRow = Button(self, text="Supprimer ligne", command=self.deleteItemRow)
        self.buttonDelectRow.grid(row=7, column=4)

        self.buttonCommit = Button(self, text="Sauvgarder", command=self.commitChanges)
        self.buttonCommit.grid(row=8, column=4)

        self.buttonCreatForm = Button(self, text="Crée", command=self.createForm)
        self.buttonCreatForm.grid(row=9, column=4)

        self.entriesVar = [self.varTypeChamps,
                           self.varNomChamps,
                           self.varValues,
                           self.varDescription]

    def changeViewType(self, event):
        if self.comboBoxTypeVue.get() != "Entry" and self.comboBoxTypeVue.get() != "SpinBox":
            self.entryValuesFromTypeVue.config(state="normal")
        else:
            self.entryValuesFromTypeVue.config(state="disable")

    def clearAllEntries(self, listEntries):
        for entry in listEntries:
            entry.set("")
        self.comboBoxTypeVue.current(0)

    def deleteItemRow(self):
        try:
            self.editFormTableView.delete(self.itemID)
            self.clearAllEntries(self.entriesVar)
            self.changeViewType(self)
        except Exception:
            self.parentController.showError("Aucune selection", "Veuillez svp faire une selection")

    def commitChanges(self):
        try:
            self.editFormTableView.insert("", self.selectedItemIndex, values=(self.varTypeChamps.get(),
                                                                              self.varNomChamps.get(),
                                                                              self.comboBoxTypeVue.get(),
                                                                              self.varValues.get(),
                                                                              self.varDescription.get()))
            self.deleteItemRow()
        except Exception:
            self.parentController.showError("Aucune selection", "Veuillez svp faire une selection")

    def createForm(self):
        listeItems = []
        idItems = self.editFormTableView.get_children()
        print("Nb of item in tableView ->", len(idItems))

        for item in idItems:
            listeItems.append(self.editFormTableView.item(item, "values"))
        print(self.entryNameForm.get())
        print(listeItems)

        self.parentController.parent.createNewForm(self.entryNameForm.get(), listeItems)


    def selectTableViewItem(self, event):
        selectedTreeView = event.widget
        self.itemID = selectedTreeView.identify_row(event.y)
        itemValues = selectedTreeView.item(self.itemID, "values")
        itemIndex = selectedTreeView.index(self.itemID)
        if itemValues:
            self.fetchItemValues(itemValues, itemIndex)
        print("Item values ->", itemValues)
        print("Item Index ->", itemIndex)
        print("Item Id ->", self.itemID)
        self.changeViewType(self)

    def fetchItemValues(self, values, index):
        self.selectedItemIndex = index
        self.varTypeChamps.set(values[0])
        self.varNomChamps.set(values[1])
        self.comboBoxTypeVue.set(values[2])
        self.varValues.set(values[3])
        self.varDescription.set(values[4])

    def selectTreeViewItem(self ,event):
        selectedTreeView = event.widget
        itemID = selectedTreeView.identify_row(event.y)
        parentItem = selectedTreeView.parent(itemID)
        itemName = selectedTreeView.item(itemID, "text")
        itemList = []
        if not parentItem: #parentItem represents a table in the data base

            for item in selectedTreeView.get_children(itemID):
                itemList.append(selectedTreeView.item(item, "text"))
            print(itemName,"children ->", itemList)
            self.fetchInfoToEditFormTableView(END, itemName, itemList, self.comboBoxTypeVue.get(), "", "")
        else:
            itemList.append(itemName)
            self.fetchInfoToEditFormTableView(END, parentItem, itemList, self.comboBoxTypeVue.get(), "", "")

        print("Item name ->", selectedTreeView.item(itemID, "text"))
        print("Children ->", selectedTreeView.get_children(itemID))
        print("Item parent ->",selectedTreeView.parent(itemID))
        print("Index ->", selectedTreeView.index(itemID))
        print("-------------------------")

    def fetchInfoToEditFormTableView(self, itemIndex, parentItem, listItems, typeView, values, description):
        if parentItem:
            for item in listItems:
                self.editFormTableView.insert("", itemIndex, values=(parentItem + "." + item, item,
                                                                    typeView, values, description))

    def showAllTablesInTreeView(self):
        countIndexParentItem = 0
        countIndexChildItem = 0
        for parentItem in self.parentController.parent.getAllTables():
            self.tablesTreeView.insert("", countIndexParentItem, parentItem, text=parentItem)
            countIndexParentItem+=1
            for childItem in self.parentController.parent.getTableColumnName(parentItem):
                self.tablesTreeView.insert(parentItem, countIndexChildItem, text=childItem[0])
                countIndexChildItem+=1
            countIndexChildItem=0
           
    def showAllFormsInListView(self):
        for i in self.parentController.parent.getFormsNameList():
            self.formsListBox.insert(END,i)


class FrameAddUserGroup(GFrame):
    def __init__(self,parentController,parentWindow,title,**args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)

        self.label=Label(self,text="Usagers", width = 10, font = ("Bell Gothic Std Black", 18))
        self.label.grid(row=0, column=0, sticky=W,columnspan=2, pady = 5, padx = 5)
        self.listboxUsers = Listbox(self)
        self.listboxUsers.bind('<<ListboxSelect>>', self.refreshSelection)
        self.scrollBarListUsers = Scrollbar(self)

        self.currentListBoxSelection = None
        self.listboxUsers.grid(row=1,column=0,sticky=W+E+N+S)

        self.scrollBarListUsers.grid(row=1,column=1,sticky=W+E+N+S)
        self.listboxUsers.config(yscrollcommand = self.scrollBarListUsers.set)
        self.scrollBarListUsers.config(command = self.listboxUsers.yview)

        self.buttonAddUserToGroup = Button(self, text = "Ajouter au groupe")

        self.refreshUsersInList()

    def refreshUsersInList(self):
        self.listboxUsers.delete(0,END)
        listofUsers = self.parentController.parent.getUsers()
        nameOfUsers = []

        for i in range (len(listofUsers)):
            nameOfUsers.append(listofUsers[i][1])

        for i in nameOfUsers:
            self.listboxUsers.insert(END,i)

    def refreshSelection(self,evt):
        selectedListBox = evt.widget
        index = int(selectedListBox.curselection()[0])
        value = selectedListBox.get(index)
        self.currentListBoxSelection = value #nom de l'usager selectione


class FrameGroups(GFrame):
    def __init__(self,parentController,parentWindow,title,**args):

        GFrame.__init__(self, parentController, parentWindow, title, **args)
        self.labelNameGroup = Label(self, text="Nom de groupe  ", width=25, anchor=W)
        self.labelNameGroup.grid(row=0, column=2, sticky=W)
        self.stringVarEntryName = StringVar()
        self.entryName = Entry(self, state='disable', textvariable = self.stringVarEntryName)
        self.entryName.focus_set()
        self.entryName.grid(row=0, column=3, sticky=W)
        self.labelNiveau = Label(self, text="Niveau de sécurité  ", width=25, anchor=W)
        self.labelNiveau.grid(row=1, column=2, sticky=W)
        self.stringVarLevel = StringVar()
        self.comboBoxLevel = Combobox(self, text="0", state='disable',values=(0,1,2,3,4,5,6,7,8,9,10), textvariable = self.stringVarLevel)
        self.comboBoxLevel.grid(row=1, column=3, sticky=W)
        self.buttonModif = Button(self, text="Sauvegarder", width=15,state='disable', command=self.saveGroup)
        self.buttonModif.grid(row=4, column=2, sticky=N,ipady = 5, pady = 15)
        self.modifying=False;
        self.buttonCancel = Button(self, text="Annuler", width=15, state='disable', command=self.cancel)
        self.buttonCancel.grid(row=4, column=3, sticky=N, ipady = 5, pady = 15)
        self.listboxGroups=Listbox(self,exportselection=False)
        self.listboxGroups.grid(column=0,row=1,rowspan=2,columnspan=2)
        self.listboxGroups.bind('<<ListboxSelect>>', self.selectItem)
        self.buttonCreate=Button(self,text="Nouveau Groupe", width=20, state='enable', command=self.createGroup)
        self.buttonCreate.grid(column=0,row=4,sticky=N, ipady = 5, pady = 15)
        self.buttonModifExist=Button(self, text="Modifier", width=15,state='disable', command=self.modifGroup)
        self.buttonModifExist.grid(column=1,row=4,sticky=N, ipady = 5, pady = 15)
        self.labelGroups=Label(self,text="Groupes")
        self.labelGroups.grid(column=0,row=0)
        self.permissionCheckList=CheckList(self)
        self.permissionCheckList.grid(row=2,column=2,columnspan=2,sticky=E+W+S+N)
        self.permissionCheckList.hlist.add("CL1", text="Modification mot de passe global")
        self.permissionCheckList.hlist.add("CL2", text="Modification mot de passe personnel")
        self.permissionCheckList.hlist.add("CL3", text="Lecture/Modification Cron jobs")
        self.permissionCheckList.hlist.add("CL4", text="Lecture/Modification Règles d'affaire")
        self.permissionCheckList.hlist.add("CL5", text="Lecture de formulaires")
        self.permissionCheckList.hlist.add("CL6", text="Modification de formulaires")
        self.permissionCheckList.hlist.add("CL7", text="Remplissage de formulaires")
        self.permissionCheckList.hlist.add("CL8", text="Modification d'usagers")
        self.permissionCheckList.hlist.add("CL9", text="Lecture d'usagers")
        self.permissionCheckList.hlist.add("CL10", text="Modification rapports")
        self.permissionCheckList.hlist.add("CL11", text="Lecture rapports")
        self.permissionCheckList.setstatus("CL1", "off")
        self.permissionCheckList.setstatus("CL2", "off")
        self.permissionCheckList.setstatus("CL3", "off")
        self.permissionCheckList.setstatus("CL4", "off")
        self.permissionCheckList.setstatus("CL5", "off")
        self.permissionCheckList.setstatus("CL6", "off")
        self.permissionCheckList.setstatus("CL7", "off")
        self.permissionCheckList.setstatus("CL8", "off")
        self.permissionCheckList.setstatus("CL9", "off")
        self.permissionCheckList.setstatus("CL10", "off")
        self.permissionCheckList.setstatus("CL11", "off")
        
        self.permissionCheckList.autosetmode()
        
        self.widgetActivate=[self.buttonCancel,self.buttonModif,self.entryName,self.comboBoxLevel]#liste des widget a activer a la modification
        self.widgetDeactivate=[self.buttonCreate]
        self.currentGroup={}
        self.updateFrame()

        #print()
        
        #configure(state = widgetState)
        self.deactivateModifs()

    def activateModifs(self):
        for widg in self.widgetActivate:
            widg.config(state="enable")
        for widg in self.widgetDeactivate:
            widg.config(state="disable")

    def deactivateModifs(self):
        self.resetFields()
        for widg in self.widgetActivate:
            widg.config(state="disable")
        for widg in self.widgetDeactivate:
            widg.config(state="enable")

    def updateFrame(self):
        GFrame.update(self)
        self.listboxGroups.delete(0, END)       
        for groups in self.parentController.parent.getGroups():
            self.listboxGroups.insert(END,groups[1])

    def resetFields(self):
        self.stringVarEntryName.set("")
        self.comboBoxLevel.set(0);
    def createGroup(self):
        self.activateModifs()
        self.resetFields()
        self.listboxGroups.selection_clear(0,END)
        self.resetCheckList()
    def modifGroup(self):
        self.activateModifs()
        self.buttonModifExist.config(state="disable")
        self.modifying=True

    def selectItem(self,evt):
        self.cancel()
        self.buttonModifExist.config(state="enable")
        index = int(self.listboxGroups.curselection()[0])
        value = self.listboxGroups.get(index)
        self.stringVarEntryName.set(value)
        self.groupSelected=self.parentController.parent.getGroups()[int(self.listboxGroups.curselection()[0])]
        self.currentGroup["oldname"]=self.stringVarEntryName.get()
        self.stringVarLevel.set(str(self.groupSelected[2]))
        self.currentGroup["rights"]=self.parentController.parent.getGroupRights(self.groupSelected[0])
        print(self.currentGroup["rights"])
        if(self.currentGroup["rights"]["motdepasseautre"]==1):
            self.permissionCheckList.setstatus("CL1", "on")
        else:
            self.permissionCheckList.setstatus("CL1", "off")

        if(self.currentGroup["rights"]["motdepassepersonnel"]==1):
            self.permissionCheckList.setstatus("CL2", "on")
        else:
            self.permissionCheckList.setstatus("CL2", "off")

        if(self.currentGroup["rights"]["cronjobs"]==1):
            self.permissionCheckList.setstatus("CL3", "on")
        else:
            self.permissionCheckList.setstatus("CL3", "off")

        if(self.currentGroup["rights"]["regleaffaire"]==1):
            self.permissionCheckList.setstatus("CL4", "on")
        else:
            self.permissionCheckList.setstatus("CL4", "off")

        if(self.currentGroup["rights"]["lireforms"]==1):
            self.permissionCheckList.setstatus("CL5", "on")
        else:
            self.permissionCheckList.setstatus("CL5", "off")

        if(self.currentGroup["rights"]["modifforms"]==1):
            self.permissionCheckList.setstatus("CL6", "on")
        else:
            self.permissionCheckList.setstatus("CL6", "off")

        if(self.currentGroup["rights"]["remplirformulaire"]==1):
            self.permissionCheckList.setstatus("CL7", "on")
        else:
            self.permissionCheckList.setstatus("CL7", "off")

        if(self.currentGroup["rights"]["modifusagers"]==1):
            self.permissionCheckList.setstatus("CL8", "on")
        else:
            self.permissionCheckList.setstatus("CL8", "off")

        if(self.currentGroup["rights"]["lireusagers"]==1):
            self.permissionCheckList.setstatus("CL9", "on")
        else:
            self.permissionCheckList.setstatus("CL9", "off")

        if(self.currentGroup["rights"]["modifrapport"]==1):
            self.permissionCheckList.setstatus("CL10", "on")
        else:
            self.permissionCheckList.setstatus("CL10", "off")

        if(self.currentGroup["rights"]["lirerapport"]==1):
            self.permissionCheckList.setstatus("CL11", "on")
        else:
            self.permissionCheckList.setstatus("CL11", "off")

    def cancel(self):
        self.resetCheckList()
        self.deactivateModifs()
        self.modifying=False;
    def resetCheckList(self):
        self.permissionCheckList.setstatus("CL1", "off")
        self.permissionCheckList.setstatus("CL2", "off")
        self.permissionCheckList.setstatus("CL3", "off")
        self.permissionCheckList.setstatus("CL4", "off")
        self.permissionCheckList.setstatus("CL5", "off")
        self.permissionCheckList.setstatus("CL6", "off")
        self.permissionCheckList.setstatus("CL7", "off")
        self.permissionCheckList.setstatus("CL8", "off")
        self.permissionCheckList.setstatus("CL9", "off")
        self.permissionCheckList.setstatus("CL10", "off")
        self.permissionCheckList.setstatus("CL11", "off")

    def saveGroup(self):
        
        self.currentGroup["name"]=self.stringVarEntryName.get()
        self.currentGroup["security"]=self.comboBoxLevel.get()
        
        self.currentGroup["rights"]={
                                     'motdepasseautre':1 if(self.permissionCheckList.getstatus("CL1")=="on")else 0, 
                                     'motdepassepersonnel':1 if(self.permissionCheckList.getstatus("CL2")=="on")else 0,
                                     'cronjobs':1 if(self.permissionCheckList.getstatus("CL3")=="on")else 0,
                                     'regleaffaire':1 if(self.permissionCheckList.getstatus("CL4")=="on")else 0,
                                     'lireforms':1 if(self.permissionCheckList.getstatus("CL5")=="on")else 0,
                                     'modifforms':1 if(self.permissionCheckList.getstatus("CL6")=="on")else 0,
                                     'remplirformulaire':1 if(self.permissionCheckList.getstatus("CL7")=="on")else 0,
                                     'modifusagers':1 if(self.permissionCheckList.getstatus("CL8")=="on")else 0,
                                     'lireusagers':1 if(self.permissionCheckList.getstatus("CL9")=="on")else 0,
                                     'modifrapport':1 if(self.permissionCheckList.getstatus("CL10")=="on")else 0,
                                     'lirerapport':1 if(self.permissionCheckList.getstatus("CL11")=="on")else 0
                                     }
        
        self.deactivateModifs()
        self.stringVarEntryName.set("")
        self.stringVarLevel.set("")

        self.parentController.parent.saveGroup(self.currentGroup,self.modifying);
        self.updateFrame();

class FrameCreateTable(GFrame):
    def __init__(self,parentController, parentWindow, title, **args):
        GFrame.__init__(self, parentController, parentWindow, title, **args)
        GFrame.addMenuBar(self, 1)
        self.types=["number","string"]
        self.listboxTables=Listbox(self)
        self.listboxTables.bind('<<ListboxSelect>>', self.selectTable)
        self.labelTables=Label(self, text="Tables",  width=25, anchor=W);
        self.modifyTableButton=Button(self,text="Modifier la table",width=15,command=self.modifyTableActivate)
        self.createTableButton=Button(self,text="Nouvelle Table",width=15,command=self.newTable) 
        self.deleteTableButton=  Button(self,text="Supprimer Table",width=15,command=self.deleteTable)     
        
        self.createButton=Button(self, text="Sauvegarder", width=15,command=self.createTable)
        self.modifyButton=Button(self,text="Sauvegarder",width=15,command=self.modifyTable)
        self.cancelButton= Button(self, text="Annuler", width=15,command=self.cancelTable) 
        self.addColumnButton=Button(self, text="Ajouter Colonne", width=15,command=self.addColumn) 
        self.deleteColumnButton=Button(self,text="Supprimer Colonne",width=15,command=self.deleteColumn)     
        self.treeviewColumns=Treeview(self, selectmode="extended",columns=("Type"))        
        self.entryColumnName=Entry(self)
        self.labelColumnName=Label(self, text="Nouvelle Colonne : ",  width=25, anchor=W);
        self.comboBoxType=Combobox(self,values=self.types);
        self.comboBoxType.current(1)
        self.labelTableName=Label(self, text="Nom de la table : ",  width=25, anchor=W);
        self.entryNameString=StringVar()
        self.entryTableName=Entry(self,textvariable=self.entryNameString)
        
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
        self.createTableButton.grid(column=0,row=5)
        self.deleteTableButton.grid(column=0,row=6)
        self.cancelButton.grid(column=2,row=4)
        self.deactivateModify()
        self.showAllTablesInListbox()

    def selectTable(self,evt):
        self.currentTable.clear()
        self.entryNameString.set(self.listboxTables.get(self.listboxTables.curselection()))
        columns=self.parentController.parent.getTableColumnName(self.listboxTables.get(self.listboxTables.curselection()))
        self.treeviewColumns.delete(*self.treeviewColumns.get_children())
        for column in columns:
            self.treeviewColumns.insert("", END,    text=column[0], values=(column[1]))       
            self.currentTable[column[0]]=(column[1])
            self.entryColumnName.config(text="")
        
        print(columns)

    def updateFrame(self):
        GFrame.updateFrame(self)
        self.showAllTablesInListbox()

    def showAllTablesInListbox(self): 
        self.listboxTables.delete(0, END)     
        for i in self.parentController.parent.getAllTables():
            self.listboxTables.insert(END, i)

    def modifyTableActivate(self):
        self.createButton.grid_forget()
        self.modifyButton.grid(column=1,row=4)
        self.activateModify()

    def deleteTable(self):
        self.parentController.parent.model.deleteTable(self.entryTableName.get())
        self.entryNameString.set("")
        self.treeviewColumns.delete(*self.treeviewColumns.get_children())
        self.currentTable.clear()
        self.deactivateModify()
        self.updateFrame()

    def newTable(self):
        self.currentTable.clear()
        self.activateModify()
        self.entryTableName.insert(0,"")
        self.entryColumnName.insert(0,"")
        self.modifyButton.grid_forget()
        self.createButton.grid(column=1,row=4)

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
        self.currentTable.pop(self.treeviewColumns.item(curItem)['text'],None)
        
        self.treeviewColumns.delete(curItem)

    def modifyTable(self):

        self.parentController.parent.model.modifyTable(self.entryTableName.get(),self.currentTable)
        self.currentTable.clear()
        self.entryColumnName.delete(0, END)
        self.entryTableName.delete(0,END)
        self.treeviewColumns.delete(*self.treeviewColumns.get_children())
        self.currentTable.clear()
        self.deactivateModify()
        self.updateFrame()

    def createTable(self):
        self.parentController.parent.model.createTable(self.entryTableName.get(),self.currentTable)
        self.entryColumnName.delete(0, END)
        self.entryTableName.delete(0,END)
        self.treeviewColumns.delete(*self.treeviewColumns.get_children())
        self.currentTable.clear()
        self.deactivateModify()
        self.updateFrame()

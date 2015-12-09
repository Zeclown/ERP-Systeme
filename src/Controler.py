# -*- coding: utf-8 -*-
from ServerCommunication import *
from View import *
from Model import *
import sqlite3
import Pyro4

class Controler():
    def __init__(self):
        self.serverCommunication = ServerCommunication(self)
        self.model = Model(self)
        self.view = View(self)
        self.setUpClient()
        self.view.initFrames()
        #self.testOfDestruction()
        self.view.root.mainloop()
        print("YO")
        
    def setUpClient(self):
        
        try:
            self.serverCommunication.connectToServer()
            self.serverCommunication.server.testConnection()
        except Exception:

            if self.view.showError("Impossible de se connecter au serveur", "Veuillez vous assurer que le serveur est bien actif"):
                self.setUpClient()
            else:
                self.view.root.destroy()

    def userLogin(self):
        username = self.view.frameLogin.entryName.get()
        password = self.view.frameLogin.entryPass.get()

        try:
            testLogIn = self.serverCommunication.logIn(username, password)
            print(testLogIn)
            if testLogIn :
                self.view.frameSwapper(self.view.frameAcceuil) #Balance l'usager a l'accueil
            else:
                self.view.frameLogin.showErrorMsg("Votre informations d'indentification est invalide.")
                self.view.frameLogin.resetEntries()
                
        except Exception:
            
            if self.view.showError("Impossible de se connecter au serveur", "Veuillez vous assurer que le serveur est bien actif"):
                self.serverCommunication.connectToServer()
                self.userLogin()
            else:
                self.view.root.destroy()

    def getAllTables(self):
        return self.model.formsManager.getAllTablesOfDataBase()

    def getTableColumnName(self, table):
        return self.model.formsManager.getTableColumnName(table)

    #def exception(self):
        #if self.view.showError():
            #self.serverCommunication.connectToServer()
            #self.userLogin()
        #else:
            #self.view.root.destroy()

    
    def getFormsNameList(self):
        return self.model.formsManager.getForms()

    def getUsers(self):
        query = 'SELECT * FROM Sys_Usagers'
        return self.serverCommunication.runSQLQuery(query, None)
        
    
    def createUser(self):

        try:
            username = self.view.frameUsersList.frameCreateUser.entryNameAccount.get()
            password = self.view.frameUsersList.frameCreateUser.entryPass.get()

            if username.strip()== "" or password.strip() == "":
                self.view.showError("Usager existant","Pogne en un autre")


            groupeUtilisateur = self.view.frameUsersList.frameCreateUser.comboBoxGroup.get()


            firstName = self.view.frameUsersList.frameCreateUser.entryName.get()
            lastName = self.view.frameUsersList.frameCreateUser.entrySurname.get()


            bindings = [ None, username, password, groupeUtilisateur, firstName, lastName ] #None pour le id

            self.serverCommunication.runSQLQuery('INSERT INTO Sys_Usagers values', bindings )

            print("USAGER CRÉE!!! USERNAME: %s PASSWORD: %s groupeutilisateur: %s" % (username,password,groupeUtilisateur) )
        except sqlite3.IntegrityError:
            self.view.showError("Usager existant","Pogne en un autre")

    def testOfDestruction(self):

        for i in range (50000):
            bindings = [ None, "dragomir"+str(i),"allo" , "ca va", "yooo", "allo" ]
            self.serverCommunication.runSQLQuery('INSERT INTO Sys_Usagers values', bindings )

    def deleteUser(self,accountToDelete):
        self.model.deleteUser(accountToDelete)

    def getGroups(self):
        return self.model.getGroups()
        
    def saveGroup(self,group):
        self.model.saveGroup(group)    
               
if __name__ == '__main__':
    c = Controler()
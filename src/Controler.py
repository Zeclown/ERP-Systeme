# -*- coding: utf-8 -*-
from ServerCommunication import *
from View import *
from Model import *
import sqlite3

class Controler():
    def __init__(self):
        self.serverCommunication = ServerCommunication(self)
        #self.serverCommunication.connectToServer()
        self.view = View(self)
        self.setUpClient()
        self.model = Model(self)
        self.view.initFrames()

        #self.tryToConnectToServer()
        self.view.root.mainloop()
        
    def setUpClient(self):
        
        try:
            self.serverCommunication.connectToServer()
            self.serverCommunication.server.testConnection()
        except Exception:
            print("yo")
            if self.view.showError("Impossible de se connecter au serveur", "Veuillez vous assurer que le serveur est bien actif"):
                self.serverCommunication.connectToServer()
                self.userLogin()
            else:
                self.view.root.destroy()
            
        
    def userLogin(self):
        username = self.view.frameLogin.entryName.get()
        password = self.view.frameLogin.entryPass.get()
        
        try:
            testLogIn = self.serverCommunication.logIn(username,password )
        
            if testLogIn :
                self.view.frameSwapper(self.view.frameAcceuil) #Balance l'usager a l'accueil
            else:
                self.view.frameLogin.showErrorMsg("Votre informations d'indentification est invalide.", "Veuillez réaaaseyyer.")
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

            groupeUtilisateur = self.view.frameUsersList.frameCreateUser.comboBoxGroup.get()

            bindings = [ None, username, password, groupeUtilisateur ] #None pour le id

            self.serverCommunication.runSQLQuery('INSERT INTO Sys_Usagers values', bindings )

            print("USAGER CRÉE!!! USERNAME: %s PASSWORD: %s groupeutilisateur: %s" % (username,password,groupeUtilisateur) )
        except sqlite3.IntegrityError:
            self.view.showError("Usager existant","Pogne en un autre")

    def deleteUser(self,accountToDelete):
        
        query = "DELETE FROM Sys_Usagers WHERE nom = '%s'" % (accountToDelete)

        print("deleted")
        print("QUERY",query)

        self.serverCommunication.runSQLQuery(query, None)


        
    def saveGroup(self):
        pass    
               
if __name__ == '__main__':
    c = Controler()
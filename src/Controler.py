# -*- coding: utf-8 -*-
from ServerCommunication import *
from View import *
from Model import *

class Controler():
    def __init__(self):
        self.serverCommunication = ServerCommunication(self)
        #self.serverCommunication.connectToServer()
        self.setUpClient()
        self.model = Model(self)
        self.view = View(self)
        #self.tryToConnectToServer()
        self.view.root.mainloop()
        
    def setUpClient(self):
        
        try:
            self.serverCommunication.connectToServer()
            self.serverCommunication.server.testConnection()
        except Exception:
            print("yo")
            if self.view.showError():
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
                self.view.frameLogin.showErrorMsg("Votre informations d'indentification est invalide.")
                self.view.frameLogin.resetEntries()
                
        except Exception:
            
            if self.view.showError():
                self.serverCommunication.connectToServer()
                self.userLogin()
            else:
                self.view.root.destroy()

    def getAllTables(self):
        return self.model.formsManager.getTables()

    def exception(self):
        if self.view.showError():
            self.serverCommunication.connectToServer()
            self.userLogin()
        else:
            self.view.root.destroy()

    
    def getFormsNameList(self):
        return self.model.formsManager.getForms()

    def getUsers(self):
        query = 'SELECT * FROM Sys_Usagers'
        return self.serverCommunication.runSQLQuery(query,None)
        
    
    def createUser(self):
        
        username = self.view.frameUsersList.frameCreateUser.entryNameAccount.get()
        password = self.view.frameUsersList.frameCreateUser.entryPass.get()

        groupeUtilisateur = self.view.frameUsersList.frameCreateUser.comboBoxGroup.get()
        
        bindings = [ None, username, password, groupeUtilisateur ] #None pour le id
 
        self.serverCommunication.runSQLQuery('INSERT INTO Sys_Usagers values', bindings )

        print("USAGER CRÉE!!! USERNAME: %s PASSWORD: %s groupeutilisateur: %s" % (username,password,groupeUtilisateur) )
        
    def deleteUser(self,nameOfUserToDelete):
        
        query = "DELETE FROM Sys_Usagers WHERE nom = '%s'" % (nameOfUserToDelete)
        print("deleted")
        print(query)
        self.serverCommunication.runSQLQuery(query, None)
        
        
               
if __name__ == '__main__':
    c = Controler()
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
        
    def setUpClient(self):
        
        try:
            self.serverCommunication.connectToServer()
            self.serverCommunication.server.testConnection()
        except Exception:
            if self.view.showError("Impossible de se connecter au serveur", "Veuillez vous assurer que le serveur est bien actif"):
                self.setUpClient()
            else:
                self.view.root.destroy()

    def userLogin(self,username,password):
        self.serverCommunication.logIn(username,password)

    def getAllTables(self):
        return self.model.formsManager.getAllTablesOfDataBase()

    def getTableColumnName(self, table):
        return self.model.formsManager.getTableColumnName(table)

    def getFormsNameList(self):
        return self.model.formsManager.getForms()

    def getUsers(self):
        return self.model.getUsers()

    def createUser(self,newUser):
        self.model.createUser(newUser)

    def deleteUser(self,accountToDelete):
        self.model.deleteUser(accountToDelete)

    def getGroups(self):
        return self.model.getGroups()
        
    def saveGroup(self,group):
        self.model.saveGroup(group)

    def testOfDestruction(self):
        for i in range (50000):
            bindings = [ None, "dragomir"+str(i),"allo" , "ca va", "yooo", "allo" ]
            self.serverCommunication.runSQLQuery('INSERT INTO Sys_Usagers values', bindings )

if __name__ == '__main__':
    c = Controler()
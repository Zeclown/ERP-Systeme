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
        self.view.root.mainloop()

        
    def setUpClient(self):
        try:
            self.serverCommunication.connectToServer()
            self.serverCommunication.server.testConnection()
        except Exception as e:
            if self.view.showError("Aucune connection au serveur", str(e) ):
                self.setUpClient()
            else:
                self.view.root.destroy()


    def userLogin(self,username,password):

        try:
            self.serverCommunication.logIn(username,password)
        except Exception as e:
            self.view.frameLogin.showErrorMsg(str(e))
            self.view.frameLogin.resetEntries()

    def getAllTables(self):
        return self.model.formsManager.getAllTablesOfDataBase()

    def getTableColumnName(self, table):
        return self.model.formsManager.getTableColumnName(table)

    def getFormsNameList(self):
        return self.model.formsManager.getForms()

    def createNewForm(self, name, formItemList):
        self.model.formsManager.createForm(name, formItemList)

    def getUsers(self):
        return self.model.getUsers()

    def createUser(self,newUser):
        try:
            self.model.createUser(newUser)
        except Exception as e:
            self.view.showError("ERROR", str(e))

    def deleteUser(self,accountToDelete):
        self.model.deleteUser(accountToDelete)

    def getGroups(self):
        return self.model.getGroups()

    def getGroupRights(self,id):
        return self.model.getGroupRights(id)
    def saveGroup(self,group,modify):
        self.model.saveGroup(group,modify)


    #cree 50 000 usagers dans la base de donnees
    def testOfDestruction(self):
        self.model.testOfDestruction()

if __name__ == '__main__':
    c = Controler()
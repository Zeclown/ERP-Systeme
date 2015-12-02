from Table import *
from Formulaire import *
class Model():
    def __init__(self,parent):
        self.formsList = []
        self.parent=parent
        self.tableManager=Table(self)
        self.formsManager=Formulaire(self)
    def createTable(self,tablename,columns):
        self.tableManager.createNewTable(tablename,columns)
    def getGroups(self):
        sqlCommand="SELECT * FROM Sys_GroupesUtilisateurs"
        return self.parent.serverCommunication.runSQLQuery(sqlCommand,None)
    def modifyTable(self,tablename,columns):
        self.tableManager.modifyTable(tablename,columns)
    def deleteTable(self,tablename):
        self.tableManager.deleteTable(tablename)
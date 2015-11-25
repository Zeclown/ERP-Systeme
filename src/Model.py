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
        sqlCommand="SELECT Sys_GroupesUtilisateurs"
        return self.parent.parent.serverCommunication.runSQLQuery(sqlCommand,None)

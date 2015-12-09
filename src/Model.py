from Table import *
from Formulaire import *
from DbManager import *
from Users import *
class Model():
    def __init__(self,parent):
        self.formsList = []
        self.parent=parent
        self.tableManager=Table(self)
        self.formsManager=Formulaire(self)
        self.users=Users(self)

    def deleteUser(self, userToDelete):
        self.users.deleteUsers(userToDelete)

    def createTable(self,tablename,columns):
        self.tableManager.createNewTable(tablename,columns)
    def getGroups(self):
        sqlCommand="SELECT * FROM Sys_GroupesUtilisateurs"
        return self.parent.serverCommunication.runSQLQuery(sqlCommand,None)
    def saveGroup(self,group):
        dbMan=DbManager("data1.db")
        
        sqlCommand="Insert into Sys_GroupesUtilisateurs(nom,niveau) VALUES"
        
        self.parent.serverCommunication.runSQLQuery(sqlCommand,(group["name"],group["security"]))
        group["id"]=self.parent.serverCommunication.runSQLQuery("SELECT id FROM Sys_GroupesUtilisateurs WHERE nom ='"+group["name"]+"'",None)
        sqlCommand="Insert into Sys_droitsGroupes(groupid,motdepasseautre,motdepassepersonnel,cronjobs,regleaffaire,lireforms,modifforms,remplirformulaire,modifusagers,lireusagers,modifrapport,lirerapport) VALUES"
        rights=group["rights"]
        print(rights)
        dbMan.query(sqlCommand,[group["id"],rights["motdepasseautre"],rights["motdepassepersonnel"]
                                                                ,rights["cronjobs"],rights["regleaffaire"],rights["lireforms"]
                                                                ,rights["modifforms"],rights["remplirformulaire"],rights["modifusagers"]
                                                                ,rights["lireusagers"],rights["modifrapport"],rights["lirerapport"]
                                                                ])
    def modifyTable(self,tablename,columns):
        self.tableManager.modifyTable(tablename,columns)
    def deleteTable(self,tablename):
        self.tableManager.deleteTable(tablename)
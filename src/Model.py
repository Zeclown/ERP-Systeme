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

    def getUsers(self):
        return self.users.getUsers()

    def createUser(self,newUser):
        self.users.createUser(newUser)

    def deleteUser(self, userToDelete):
        self.users.deleteUsers(userToDelete)

    def createTable(self,tablename,columns):
        self.tableManager.createNewTable(tablename,columns)
    def getGroupRights(self,id):
        sqlCommand="SELECT *  FROM Sys_droitsGroupes WHERE groupid=" + str(id)
        result=self.parent.serverCommunication.runSQLQuery(sqlCommand,None)[0]
        print(result)
        rights={"motdepasseautre":result[1],"motdepassepersonnel":result[2],
                "cronjobs":result[3],"regleaffaire":result[4],
                "lireforms":result[5],"modifforms":result[6],"remplirformulaire":result[7],"modifusagers":result[8],"lireusagers":result[9],"modifrapport":result[10],"lirerapport":[11]}
        return rights;
    def getGroups(self):
        sqlCommand="SELECT * FROM Sys_GroupesUtilisateurs"
        return self.parent.serverCommunication.runSQLQuery(sqlCommand,None)
    def saveGroup(self,group,modify):

        if(modify==False): #then creates the group
            sqlCommand="Insert into Sys_GroupesUtilisateurs(nom,niveau) VALUES"
            self.parent.serverCommunication.runSQLQuery(sqlCommand,(group["name"],group["security"]))
        else:
            group["id"]=self.parent.serverCommunication.runSQLQuery("SELECT id FROM Sys_GroupesUtilisateurs WHERE nom ='"+group["oldname"]+"'",None)[0][0]
            sqlCommand="UPDATE Sys_GroupesUtilisateurs SET nom='%s' ,niveau=%s WHERE id=%s" % (group["name"],group["security"],group["id"])
            print(sqlCommand)
            self.parent.serverCommunication.runSQLQuery(sqlCommand,None)
        group["id"]=self.parent.serverCommunication.runSQLQuery("SELECT id FROM Sys_GroupesUtilisateurs WHERE nom ='"+group["name"]+"'",None)[0][0]
        if(modify==False):
            sqlCommand="Insert into Sys_droitsGroupes(groupid,motdepasseautre,motdepassepersonnel,cronjobs,regleaffaire,lireforms,modifforms,remplirformulaire,modifusagers,lireusagers,modifrapport,lirerapport) VALUES"
            rights=group["rights"]
            self.parent.serverCommunication.runSQLQuery(sqlCommand,(group["id"],rights["motdepasseautre"],rights["motdepassepersonnel"]
                                                                    ,rights["cronjobs"],rights["regleaffaire"],rights["lireforms"]
                                                                    ,rights["modifforms"],rights["remplirformulaire"],rights["modifusagers"]
                                                                    ,rights["lireusagers"],rights["modifrapport"],rights["lirerapport"]
                        ))
        else:
            rights=group["rights"]
            sqlCommand="UPDATE Sys_droitsGroupes SET motdepasseautre=%d,motdepassepersonnel=%s,cronjobs=%s,regleaffaire=%s,lireforms=%s,modifforms=%s,remplirformulaire=%s,modifusagers=%s,lireusagers=%s,modifrapport=%s,lirerapport=%s WHERE groupid=%s" %(rights["motdepasseautre"],rights["motdepassepersonnel"]
                                                                    ,rights["cronjobs"],rights["regleaffaire"],rights["lireforms"]
                                                                    ,rights["modifforms"],rights["remplirformulaire"],rights["modifusagers"]
                                                                    ,rights["lireusagers"],rights["modifrapport"],rights["lirerapport"],group["id"])
            self.parent.serverCommunication.runSQLQuery(sqlCommand,None)
    def modifyTable(self,tablename,columns):
        self.tableManager.modifyTable(tablename,columns)
    def deleteTable(self,tablename):
        self.tableManager.deleteTable(tablename)

    def testOfDestruction(self):
        for i in range (50000):
            bindings = [ None, "dragomir"+str(i),"allo" , "ca va", "yooo", "allo" ]
            self.parent.serverCommunication.runSQLQuery('INSERT INTO Sys_Usagers values', bindings )
__author__ = 'Alexandre'

class Users():
    def __init__(self,parent):
        self.parent = parent

    def createUser(self,newUser):

        if newUser.username.strip() == "" or newUser.password.strip() == "":
            raise Exception("Vous devez choisir un nom d'usager et un mot de passe")

        bindings = [ None, newUser.username, newUser.password, newUser.group, newUser.name, newUser.lastname]

        self.parent.parent.serverCommunication.runSQLQuery('INSERT INTO Sys_Usagers Values', bindings)

    def getUsers(self):
        query = 'SELECT * FROM Sys_Usagers'
        return self.parent.parent.serverCommunication.runSQLQuery(query, None)

    def deleteUsers(self, accountToDelete):
        query = "DELETE FROM Sys_Usagers WHERE username = '%s'" % (accountToDelete)

        print("deleted")
        print("QUERY",query)

        self.parent.parent.serverCommunication.runSQLQuery(query, None)

##Classe modele d'un usager utile pour passe en parametre a une creation d'usager
class User():
    def __init__(self,username,password,group,name,lastname):
        self.username = username
        self.password = password
        self.group = group
        self.name = name
        self.lastname = lastname


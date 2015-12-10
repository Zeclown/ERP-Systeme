import Pyro4
# -*- coding: utf-8 -*-


class ServerCommunication():
    def __init__(self,parent):
        self.serverAdress = "PYRO:foo@184.162.124.218:8000"
        self.parent = parent
        self.status = None
        self.server = None
        
    def connectToServer(self):
        self.server = Pyro4.Proxy(self.serverAdress)
        if self.server == None:
            raise Exception("Veuillez vous assurer que le serveur est bien actif")

    def runSQLQuery(self,SQLquery, bindings):
        return self.server.executeSql(SQLquery,bindings)

    def logIn(self,username,password):
        if self.server.testConnection:
            print("im in")
            if self.server.loginValidation(username,password):
                self.parent.view.frameSwapper(self.parent.view.frameAcceuil)
            else:
                raise Exception("L'information saisie est erronée.")
                self.view.frameLogin.showErrorMsg("Votre informations d'indentification est invalide.")
                self.view.frameLogin.resetEntries()
        else:
            raise Exception("Connection au serveur impossible.")




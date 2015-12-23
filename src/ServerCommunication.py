import Pyro4
import os.path
import sys
# -*- coding: utf-8 -*-


class ServerCommunication():
    def __init__(self,parent):
        fichier = os.path.dirname(sys.argv[0])
        fichier = fichier+"\Ressources\ip_address_server.txt"
        f = open(fichier, "r")
        self.ipServer = f.readline()
        f.close()
        self.serverAdress = "PYRO:foo@"+self.ipServer+":48261"
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




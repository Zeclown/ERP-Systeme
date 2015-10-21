# -*- coding: utf-8 -*-
import DbManager
import Pyro4
import socket


class Server(object):
    def __init__(self):
        self.dbManager=DbManager.DbManager("data1.db")
    
    def loginValidation(self, user,mdp):
        if self.dbManager.login(user,mdp):
            return True
        else:
            return False
        
    def writeIP(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        self.monip=s.getsockname()[0]

        f = open("ip address.txt", "w")
        print(self.monip)
        f.write(self.monip)
        f.close()
        
    def correctIP(self):
        f = open("ip address.txt", "r")
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        self.monip=s.getsockname()[0]
        
        if(f.readline() != self.monip):
            self.writeIP()

            
    def executeSql(self, query):
        self.dbManager.query(query)
            

serverPyro = Server()   #objet du serveur

daemon = Pyro4.Daemon(host="10.57.47.23",port=43225)      #ce qui écoute les remote calls sur le serveur
uri = daemon.register(serverPyro,"foo")

serverPyro.writeIP()
serverPyro.correctIP()

print("ready")
daemon.requestLoop()
        
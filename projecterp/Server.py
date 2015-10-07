# -*- coding: utf-8 -*-
import Pyro4
import socket
import DbManager

class Server(object):
    def __init__(self):
        self.dbManager = DbManager.DbManager()
        
    
    def loginValidation(self, user):
        print("bien recu! "+user)
        message = "Bonjour "+user+"!"
        return message
 
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
            writeIP()
            
    def executeSql(self, query):
        self.dbManager.query(query)
            
    

serverPyro = Server()   #objet du serveur

daemon = Pyro4.Daemon(host="10.57.47.23",port=43225)      #ce qui écoute les remote calls sur le serveur
uri = daemon.register(serverPyro,"foo")

serverPyro.writeIP()
serverPyro.correctIP()

print("ready")
daemon.requestLoop()
        
# -*- coding: utf-8 -*-
import DbManager
import Pyro4
import socket
import shutil
from threading import Timer


class Server(object):
    def __init__(self):
        self.dbManager=DbManager.DbManager("data1.db")
    
    def loginValidation(self, user, mdp):
        if self.dbManager.login(user, mdp):
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
        
#     def executeCronJobs(self):
#         existingCronJobsInDB = []
#         activeCronJobs = []
#         
#         for i in existingCronJobs:
#             newCronJob = CronJob("placeholder")
#             activeCronJobs.append(newCronJob)
# 
#         for i in activeCronJobs:
#             t = Timer(5.0, hello)
            

    
    def backupDatabase(self):
        shutil.copyfile("data1.db","database_Backup.db")
        
class CronJob():
    def __init__(self,nom):
        self.nom = nom
            

serverPyro = Server()   #objet du serveur

#daemon = Pyro4.Daemon(host="10.57.47.22",port=43225)      #ce qui Ã©coute les remote calls sur le serveur
daemon = Pyro4.Daemon(host="127.0.0.1",port=43225)      #ce qui Ã©coute les remote calls sur le serveur
uri = daemon.register(serverPyro,"foo")

serverPyro.writeIP()
serverPyro.correctIP()

serverPyro.backupDatabase()

print("ready")
daemon.requestLoop()
        

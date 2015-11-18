# -*- coding: utf-8 -*-
import DbManager
import Pyro4
import socket
import shutil
from threading import Timer


class Server(object):
    def __init__(self):
        self.ipDuServeur = "10.57.47.25"
        self.portDuServeur = 48261
        self.dbManager=DbManager.DbManager("data1.db")

        self.databaseVersion = 0
        #f = open("Ressources/Database_Version.txt", "r")
        #print(f.readline())
        #self.databaseVersion = f.readline()
        #f.close()
        #self.createCronJob()
    
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

            

    def executeSql(self, query, bindings = None):
        queryResult = self.dbManager.query(query,bindings)
        return queryResult
    
    def createCronJob(self):
        uneQuerySQL = "SELECT * FROM Sys_Crons"
        cronJobResult = self.executeSql(uneQuerySQL)
        print(cronJobResult)
        
        self.activeCronJobs = []
        
        for i in range(len(cronJobResult)):
            if( cronJobResult[i][5] == 1 ):
                id = cronJobResult[i][0]
                nom = cronJobResult[i][1]
                fnctid = cronJobResult[i][2]
                nbTemps = cronJobResult[i][3]
                frequence = cronJobResult[i][4]
                activeCron = cronJobResult[i][5]
                
                newCronJob = CronJob(self, nom, fnctid, nbTemps, frequence, activeCron)
                self.activeCronJobs.append(newCronJob)
        
    def executeCronJobs(self):
        t = Timer(5.0, self.executeCronJobs)
        t.start()
        print("yoooooooo")
        #existingCronJobsInDB = []
        #activeCronJobs = []
         
        #for i in existingCronJobs:
            #newCronJob = CronJob("placeholder")
            #activeCronJobs.append(newCronJob)
 
        #for i in activeCronJobs:
        
    #def backupDatabase(self):       #Le ID de cette fonction est 1
        #aFileName = "database_Backup_"+ str(self.databaseVersion) +".db"
        #if( os.path.isfile(aFileName) ):
            #shutil.move( aFileName, "Archives/"+aFileName)

        
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

        
class CronJob():
    def __init__(self,nom):
        self.nom = nom
            

serverPyro = Server()   #objet du serveur


daemon = Pyro4.Daemon(host="10.57.47.25",port=48261)      #ce qui écoute les remote calls sur le serveur



#daemon = Pyro4.Daemon(host="127.0.0.1",port=43225)      #ce qui Ã©coute les remote calls sur le serveur


#daemon = Pyro4.Daemon(host="10.57.47.22",port=43225)      #ce qui écoute les remote calls sur le serveur


uri = daemon.register(serverPyro,"foo")

serverPyro.writeIP()
serverPyro.correctIP()

#serverPyro.backupDatabase()

print("ready")
daemon.requestLoop()

# -*- coding: utf-8 -*-
import DbManager
import Pyro4
import socket
import shutil
import os.path
import smtplib
import time
from threading import Timer


class Server(object):
    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        self.monip=s.getsockname()[0]
        
        print(self.monip)
        
        self.ipDuServeur = self.monip
        self.portDuServeur = 48261
        
        self.dbManager=DbManager.DbManager("data1.db")
        
        self.databaseVersion = 0
        """f = open("Ressources/Database_Version.txt", "r")
        self.databaseVersion = f.readline()
        print("DB version:")
        print(self.databaseVersion)
        f.close()"""
        
        #self.createCronJob()
        #self.executeCronJobs()
        
    
    def loginValidation(self, user, mdp):
        if self.dbManager.login(user, mdp):
            return True
        else:
            return False
        
#     def writeIP(self):
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.connect(("gmail.com",80))
#         self.monip=s.getsockname()[0]
# 
#         f = open("ip address.txt", "w")
#         print(self.monip)
#         f.write(self.monip)
#         f.close()
#         
#     def correctIP(self):
#         f = open("ip address.txt", "r")
#         
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.connect(("gmail.com",80))
#         self.monip=s.getsockname()[0]
#         
#         if(f.readline() != self.monip):
#             self.writeIP()
    
    def executeSql(self, query, bindings):
        queryResult = self.dbManager.query(query,bindings)
        return queryResult
    
    def testConnection(self):
        return True
    
    def createCronJob(self):
        uneQuerySQL = "SELECT * FROM Sys_Crons"
        cronJobResult = self.executeSql(uneQuerySQL, None)
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
                 
                newCronJob = CronJob(self, id, nom, fnctid, nbTemps, frequence, activeCron)
                self.activeCronJobs.append(newCronJob)
                
    def createCronJobWhenNew(self):
        uneQuerySQL = "SELECT * FROM Sys_Crons WHERE id = (SELECT MAX(id) FROM Sys_Crons)"
        cronJobResult = self.executeSql(uneQuerySQL, None)
        
        if(cronJobResult[0][5] == 1):
            id = cronJobResult[i][0]
            nom = cronJobResult[i][1]
            fnctid = cronJobResult[i][2]
            nbTemps = cronJobResult[i][3]
            frequence = cronJobResult[i][4]
            activeCron = cronJobResult[i][5]
        
            newCronJob = CronJob(self, id, nom, fnctid, nbTemps, frequence, activeCron)
            self.activeCronJobs.append( newCronJob )
        
    def executeCronJobs(self):
        for i in self.activeCronJobs:
            i.timerExecution()
            
    def executeCronJobsWhenNew(self):
        theLength = len(self.activeCronJobs)
        self.activeCronJobs[theLength-1].timerExecution()

    def backupDatabase(self):       #Le ID de cette fonction est 1
        aFileName = "database_Backup_"+ str(self.databaseVersion) +".db"
        if( os.path.isfile(aFileName) ):
            shutil.move( aFileName, "Archives/"+aFileName)
             
        self.databaseVersion = int(self.databaseVersion)
        self.databaseVersion += 1
         
        aFileName = "database_Backup_"+ str(self.databaseVersion) +".db"
        shutil.copyfile("data1.db", aFileName)
 
    def sendEmail(self, textToSend, subjectEmail, fromEmail, fromPassword, toEmail):    #Le ID de cette fonction est 2
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromEmail, fromPassword)
        msg = subjectEmail+" \n\n "+textToSend
        
        server.sendmail("foobar", toEmail, msg)
        server.quit()
        
    def writeLog(self, messageToSave, typeOfLog):              #Le ID de cette fonction est 3
        currentDate = time.strftime("%d/%m/%Y")
        currentTime = time.strftime("%I:%M:%S")
        f = open("Logs/"+typeOfLog+"_Log.txt", "a")
        f.write(messageToSave+" ---"+currentTime+" - "+currentDate+"---\n")
        f.close()
    
        


class CronJob():
    def __init__(self, parent, id, nom, fnctid, nbTemps, frequence, activeCron):
        self.parent = parent
        self.id = id
        self.nom = nom
        self.functionId = fnctid
        self.nbTemps = int(nbTemps)
        self.frequence = int(frequence)
        self.activeCron = activeCron
         
    def timerExecution(self):
        tempsAExecuter = self.frequence*self.nbTemps
        self.t = Timer( tempsAExecuter ,self.timerExecution)
        self.t.start()
        if(self.activeCron == 0):
            self.cancelTimer()
            
        if(self.functionId == 1):
            self.parent.backupDatabase()
        elif(self.functionId == 2):
                                                    ####################################placeholder
            self.parent.sendEmail("un autre test esti","Subject: "+"un sujet","champsfuturs@gmail.com","A1?champsfutursouverture","unreaved@hotmail.com")     
        elif(self.functionId == 3):
            self.parent.writeLog()
             
    def cancelTimer(self):
        self.t.cancel()
        

serverPyro = Server()   #objet du serveur

daemon = Pyro4.Daemon(host=serverPyro.ipDuServeur, port=serverPyro.portDuServeur)      #ce qui écoute les remote calls sur le serveur

uri = daemon.register(serverPyro, "foo")

#serverPyro.backupDatabase()           #TEST DE BACKUP
#serverPyro.sendEmail("un autre test esti","Subject: "+"un sujet","champsfuturs@gmail.com","A1?champsfutursouverture","unreaved@hotmail.com")    #TEST DE EMAIL
#serverPyro.writeLog("A backup was made", "DBBackup")

print("ready")
daemon.requestLoop()

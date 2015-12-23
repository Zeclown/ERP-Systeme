# -*- coding: utf-8 -*-
import DbManager
import Pyro4
import socket
import shutil
import os.path
import smtplib
import time
import sqlite3
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
        
        #self.createFonctionInTableIfNotExist()
        
        #self.createCronJob()
        #self.executeCronJobs()
        
    def loginValidation(self, user, mdp):
        if self.dbManager.login(user, mdp):
            return True
        else:
            return False
        
    def executeSql(self, query, bindings):
        queryResult = self.dbManager.query(query,bindings)
        return(queryResult)
    
    def testConnection(self):
        return True
    
    def createFonctionInTableIfNotExist(self):        #si les cron jobs hardcodé n'existe pas
        aQuery = "SELECT * FROM Sys_Crons WHERE id = 1"
        result = self.executeSql(aQuery, None)
        if(result == []):
            aQuery = "INSERT INTO Sys_Crons(id,nom,fnct_id,nbTemps,frequence,actif) VALUES (1,'Database Backup',1,4,7,1)"
            self.executeSql(aQuery, None)
        
        aQuery = "SELECT * FROM Sys_Crons WHERE id = 2"
        result = self.executeSql(aQuery, None)
        if(result == []):
            aQuery = "INSERT INTO Sys_Crons(id,nom,fnct_id,nbTemps,frequence,actif) VALUES (2,'Send Email',2,4,7,0)"
            self.executeSql(aQuery, None)
        
        aQuery = "SELECT * FROM Sys_Crons WHERE id = 3"
        result = self.executeSql(aQuery, None)
        if(result == []):
            aQuery = "INSERT INTO Sys_Crons(id,nom,fnct_id,nbTemps,frequence,actif) VALUES (3,'Write Log',3,4,7,0)"
            self.executeSql(aQuery, None)
    
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
        
    def deleteCronJob(self,cronId):
        for cron in self.activeCronJobs:
            if(cron.id == cronId):
                cron.cancelTimer()
                self.activeCronJobs.remove(cron)
                aQuery = "DELETE FROM Sys_Crons WHERE id = %s" %(cronId)
                print(aQuery)
                self.executeSql(aQuery, None)
            
    def executeCronJobs(self):
        for i in self.activeCronJobs:
            i.timerExecution()
    
    def executeCustomCronJob(self,functionId):
        aQuery = "SELECT id FROM Sys_RegleAffaire WHERE id = "+functionId
        RegleAffaire = self.executeSql(aQuery, None)
        aQuery = "SELECT * FROM Sys_RegleAffaireListe WHERE id = "+RegleAffaire
        tabRegleAffaire = self.executeSql(aQuery, None)
        
    
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
        
        logMessage = "la database a fait un backup"
        self.writeLog(logMessage, "databaseLog")
 
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
        f.write("---"+currentTime+" - "+currentDate+"--- "+messageToSave+"\n")
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
        if(self.nbTemps == 1):       #secondes
            tempsAExecuter = self.frequence*1
        elif(self.nbTemps == 2):     #minutes
            tempsAExecuter = self.frequence*60
        elif(self.nbTemps == 3):     #heures
            tempsAExecuter = self.frequence*3600
        elif(self.nbTemps == 4):     #jours
            tempsAExecuter = self.frequence*86400
        elif(self.nbTemps == 5):     #mois (on prend en compte que c'est 30 jours ici)
            tempsAExecuter = self.frequence*2592000
        elif(self.nbTemps == 6):     #an (on prend en compte ici que 1 an est 365 jours
            tempsAExecuter = self.frequence*31536000

        self.t = Timer( tempsAExecuter ,self.timerExecution)
        self.t.start()
        if(self.activeCron == 0):
            self.cancelTimer()
            
        if(self.functionId == 1):
            self.parent.backupDatabase()
        else:
            self.parent.executeCustomCronJob(self.functionId)
             
    def cancelTimer(self):
        self.t.cancel()
        

serverPyro = Server()   #objet du serveur

daemon = Pyro4.Daemon(host=serverPyro.ipDuServeur, port=serverPyro.portDuServeur)      #ce qui écoute les remote calls sur le serveur

uri = daemon.register(serverPyro, "foo")

#serverPyro.backupDatabase()           #TEST DE BACKUP
#serverPyro.sendEmail("un autre test esti","Subject: "+"un sujet","champsfuturs@gmail.com","A1?champsfutursouverture","unreaved@hotmail.com")    #TEST DE EMAIL
#serverPyro.writeLog("A backup was made", "DBBackup")

#serverPyro.createFonctionInTableIfNotExist()
#serverPyro.createCronJob()        #TEST
#serverPyro.executeCronJobs()
#serverPyro.deleteCronJob(1)

print("ready")
daemon.requestLoop()

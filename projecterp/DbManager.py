
# -*- coding: utf-8 -*-
import sqlite3
#la classe de gestion de base de donn�es. elle g�re les requ�tes de base de donn�e
#et est utilis� et visible par le serveur uniquement.

class DbManager():
    def __init__(self,dbPath):
        self.db=sqlite3.connect(dbPath)
        self.cursorDB = self.db.cursor()
        self.createDB()
    def getTable(self,name): #retourne la table en uilisant son nom
        self.cursorDB.execute('select * From' + name)
        names = list(map(lambda x: x[0], cursor.description))
        rows=self.cursorDB.fetchall()
        dictionnary={}
        for i in range(len(names)):
            for j in rows:
                dictionnary[names[i]]=j[i]
        return dictionnary
        
    def getRows(self,tableName,conditions): #retourne une ou plusieur rang� d�pendant d'une liste de condition (WHERE) 
        self.cursorDB.execute('select * From ' + name + " WHERE " + conditions)
        names = list(map(lambda x: x[0], cursor.description))
        rows=self.cursorDB.fetchall()
        dictionnary={}
        for i in range(len(names)):
            for j in rows:
                dictionnary[names[i]]=j[i]
        return dictionnary
    def query(self,query):
        self.cursorDB.execute(query)
        self.cursor.commit()
    def createDB(self):
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_GroupesUtilisateurs
             (id integer primary key, nom text NOT NULL, droits text NOT NULL)''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_Usagers
             (id integer primary key, nom text NOT NULL, mdp text NOT NULL, groupUtilisateur integer  ,FOREIGN KEY(groupUtilisateur) REFERENCES Sys_GroupeUtilisateur(id))''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_Formulaires
             ( id integer primary key,nom text NOT NULL, date_creation Date NOT NULL, derni�re_modif Date NOT NULL  , acces_utilisation integer UNIQUE ,acces_modification integer UNIQUE  )''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_Specificite
             (id integer, nomChamp text NOT NULL, type text NOT NULL,FOREIGN KEY(id) REFERENCES Sys_Formulaires(id))''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_EnumType
             (id integer primary key, nom text NOT NULL)''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_EnumList
             (id integer, nom text NOT NULL,FOREIGN KEY(id) REFERENCES Sys_EnumType(id))''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_RegleAffaire
             (id integer primary key, nom text NOT NULL)''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_Crons
             (id integer primary key, nom text NOT NULL,fnct_id integer, nbTemps integer, frequence integer ,FOREIGN KEY(fnct_id) REFERENCES Sys_RegleAffaire(id))''')    
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_RegleAffaire
             (id integer primary key, nom text NOT NULL)''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_RegleAffaireListe
             (id integer primary key, tableChoisie text NOT NULL,colonne text,operation text ,FOREIGN KEY(id) REFERENCES Sys_RegleAffaire(id) )''')
if __name__ == "__main__":
    db=DbManager("")        
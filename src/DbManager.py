
# -*- coding: utf-8 -*-
import sqlite3
#la classe de gestion de base de donn�es. elle g�re les requ�tes de base de donn�e
#et est utilis� et visible par le serveur uniquement.

class DbManager():
    def __init__(self,dbPath):
        self.db=sqlite3.connect(dbPath,check_same_thread=False)
        self.cursorDB = self.db.cursor()
        self.createDB()


    def query(self,query,bindings):
        if bindings:
            numberOfBindings = len(bindings)
            placeholder = '?'
            placeholders = ', '.join( [placeholder] * numberOfBindings )
            queryToExecute = query + '(%s)' % placeholders


            self.cursorDB.execute(queryToExecute, bindings)

            self.db.commit()
            return self.cursorDB.fetchall()

        self.cursorDB.execute(query)
        self.db.commit()
        return self.cursorDB.fetchall()

    def login(self,name,pswd):
        self.cursorDB.execute('SELECT id From Sys_Usagers Where username=? AND password=?', (name,pswd))
        print("QUERY FOIRER PEUT ETRE", 'SELECT id From Sys_Usagers Where username=? AND password=?', (name,pswd))

        if self.cursorDB.fetchone()!=None:
            return True
        else:
            return False
        
    def createDB(self):
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_GroupesUtilisateurs
             (id integer primary key autoincrement, nom text NOT NULL,niveau integer)''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_Usagers
             (id integer primary key autoincrement, username text NOT NULL UNIQUE, password text NOT NULL, groupUtilisateur integer  , firstName text, lastName text,FOREIGN KEY(groupUtilisateur) REFERENCES Sys_GroupeUtilisateur(id))''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_Formulaires
             ( id integer primary key autoincrement,nom text NOT NULL, date_creation Date NOT NULL, derniere_modif Date NOT NULL  , acces_utilisation integer  ,acces_modification integer   )''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_Form_Spec
             (id integer primary key autoincrement, form_id integer, nomTable text,colonne text, label text NOT NULL, typeView text NOT NULL,valeurs text, description text,FOREIGN KEY(form_id) REFERENCES Sys_Formulaires(id))''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_EnumType
             (id integer primary key autoincrement, nom text NOT NULL)''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_EnumList
             (id integer, nom text NOT NULL,FOREIGN KEY(id) REFERENCES Sys_EnumType(id))''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_Crons
             (id integer primary key autoincrement, nom text NOT NULL,fnct_id integer, nbTemps text, frequence integer ,actif INTEGER,sendEmail bool,email text,sendLog bool,FOREIGN KEY(fnct_id) REFERENCES Sys_RegleAffaire(id))''')    
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_RegleAffaire
             (id integer primary key autoincrement, nom text NOT NULL)''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_RegleAffaireListe
             (id integer primary key autoincrement, tableChoisie text,colonne text,operation text ,FOREIGN KEY(id) REFERENCES Sys_RegleAffaire(id) )''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS Sys_droitsGroupes
        (groupid integer primary key autoincrement, motdepasseautre integer, motdepassepersonnel integer,cronjobs integer,regleaffaire integer, lireforms integer, modifforms integer,remplirformulaire integer, modifusagers integer, lireusagers integer, modifrapport integer,lirerapport integer,FOREIGN KEY(groupid) REFERENCES Sys_GroupesUtilisateurs(id) )''')
        self.cursorDB.execute(''' SELECT * FROM Sys_Usagers WHERE username='admin' ''')
        admin=self.cursorDB.fetchone()
        if(admin==None):
            self.db.execute('''INSERT INTO Sys_Usagers (id,username, password) VALUES (0,'admin','admin')''')
            
if __name__ == "__main__":
    db=DbManager("data1.db")


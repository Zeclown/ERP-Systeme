from ServerCommunication import *
from View import *
from Model import *

class Controler():
    def __init__(self):
        #self.serverCommunication = ServerCommunication()
        #self.serverCommunication.connectToServer()
        self.model = Model(self)
        self.view = View(self)
        self.serverCommunication = ServerCommunication()
        self.tryToConnectToServer()
        self.view.root.mainloop()
        
    def userLogin(self):
        username = self.view.frameLogin.entryName.get()
        password = self.view.frameLogin.entryPass.get()
        
        try:
            
            testLogIn = self.serverCommunication.logIn(username,password )
        
            if testLogIn :
                self.view.frameSwapper(self.view.frameAcceuil) #Balance l'usager a l'accueil
            else:
                print( "FALSE LOG IN" ) #TEMPORAIRE!!!! A FAIRE: Affiche msg d'erreur et efface les champs texte
                self.view.frameLogin.showErrorMsg("Votre informations d'indentification est invalide.")
                self.view.frameLogin.resetEntries()
                
        except Exception:
            
            if self.view.showError():
                self.serverCommunication.connectToServer()
                self.userLogin()
            else:
                self.view.root.destroy()
                
            
    def tryToConnectToServer(self):
        try:
            self.serverCommunication.connectToServer()
        except Exception:
            print("HEY")
            self.view.showError()
            if self.view.showError():
                self.serverCommunication.connectToServer()
            else:
                print("DESTROY")
                self.view.root.quit()

    def getAllTables(self):
        pass

    
    def getFormsNameList(self):
        sqlQuery = "SELECT nom FROM Sys_Formulaires"
        self.model.formsList = self.serverCommunication.runSQLQuery(sqlQuery)
        return self.model.formsList
    
    def createUser(self):
        
        username = self.view.frameUsersList.frameCreateUser.entryNameAccount.get()
        password = self.view.frameUsersList.frameCreateUser.entryNameAccount.get()
        groupeUtilisateur = self.view.frameUsersList.frameCreateUser.entryNameAccount.get()
        
        bindings = [ 8, username, password, groupeUtilisateur]
 
        self.serverCommunication.runSQLQuery('INSERT INTO Sys_Usagers values', bindings )
               
if __name__ == '__main__':
    c = Controler()
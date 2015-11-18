from ServerCommunication import *
from View import *
from Model import *

class Controler():
    def __init__(self):
        self.serverCommunication = ServerCommunication()
        self.serverCommunication.connectToServer()
        self.model = Model(self)
        self.view = View(self)
        self.view.root.mainloop()
        
    def userLogin(self):
        username = self.view.frameLogin.entryName.get()
        password = self.view.frameLogin.entryPass.get()
        
        testLogIn = self.serverCommunication.logIn(username,password )
        
        if testLogIn :
            self.view.frameSwapper(self.view.frameAcceuil) #Balance l'usager a l'accueil
        else:
            print( "FALSE LOG IN" ) #TEMPORAIRE!!!! A FAIRE: Affiche msg d'erreur et efface les champs texte
            self.view.frameLogin.showErrorMsg("Votre informations d'indentification est invalide.")
            self.view.frameLogin.resetEntries()

    def getAllTables(self):
        return self.model.formsManager.getTables()

    
    def getFormsNameList(self):
        return self.model.formsManager.getForms()
        
    
    def createUser(self):
        
        username = self.view.frameUsersList.frameCreateUser.entryNameAccount.get()
        password = self.view.frameUsersList.frameCreateUser.entryNameAccount.get()
        groupeUtilisateur = self.view.frameUsersList.frameCreateUser.entryNameAccount.get()
        
        bindings = [ username, password, groupeUtilisateur]
 
        self.serverCommunication.runSQLQuery('INSERT INTO Sys_Usagers values', bindings )
               
if __name__ == '__main__':
    c = Controler()
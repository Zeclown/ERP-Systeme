from ServerCommunication import *
from View import *

class Controler():
    def __init__(self):
        self.serverCommunication = ServerCommunication()
        self.serverCommunication.connectToServer()
        self.view = View(self)
        self.view.root.mainloop()
        
    def userLogin(self): 
        if self.serverCommunication.logIn(self.view.frameLogin.entryName.get(), self.view.frameLogin.entryPass.get()) :
            self.view.frameSwapper(self.view.frameAcceuil) #Balance l'usager a l'accueil
        else:
            print( "FALSE LOG IN") #TEMPORAIRE!!!! A FAIRE: Affiche msg d'erreur et efface les champs texte
            self.view.frameLogin.resetEntries()
            
            
if __name__ == '__main__':
    c = Controler()
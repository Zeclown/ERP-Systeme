import ServerCommunication
import View

class Controler():
    def __init__(self):
        self.serverCommunication = ServerCommunication()
        self.view = View(self)
        self.view.root.mainloop()
        
    def userLogin(self, user, password):
        self.serverCommunication.logIn(user,password) 
        

if __name__ == '__main__':
    c = Controler()
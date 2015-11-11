import Pyro4

class ServerCommunication():
    def __init__(self):
<<<<<<< HEAD
        #self.serverAdress = "PYRO:foo@10.57.47.22:48261"
        self.serverAdress = "PYRO:foo@127.0.0.1:43225"
=======
        self.serverAdress = "PYRO:foo@10.57.47.25:48261"
>>>>>>> 1dfe00b95e9bb655a7ce5e9341131a3e55402497
        self.status = None
        self.server = None
        
    def connectToServer(self):
        self.server = Pyro4.Proxy(self.serverAdress)
        
    def runSQLQuery(self,SQLquery, bindings = None):
        return self.server.executeSql(SQLquery)
        
    def logIn(self,user,password):
        if user.strip()== "" or password.strip() == "":
            return False
        else:
            message= self.server.loginValidation(user,password)
            print(message)
            return message
            
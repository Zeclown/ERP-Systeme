import Pyro4

class ServerCommunication():
    def __init__(self):
        self.serverAdress = "PYRO:foo@10.57.47.22:48261"
        #self.serverAdress = "PYRO:foo@127.0.0.1:43225"
        self.status = None
        self.server = None
        
    def connectToServer(self):
        self.server = Pyro4.Proxy(self.serverAdress)
        
    def runSQLQuery(self,SQLquery):
        return self.server.executeSql(SQLquery)
        
    def logIn(self,user,password):
        if user.strip()== "" or password.strip() == "":
            return False
        else:
            message= self.server.loginValidation(user,password)
            print(message)
            return message
            
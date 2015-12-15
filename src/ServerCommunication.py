import Pyro4


class ServerCommunication():
    def __init__(self,parent):
        self.serverAdress = "PYRO:foo@10.57.48.22:48261"
        self.parent = parent
        self.status = None
        self.server = None
        
    def connectToServer(self):
        try:
            self.server = Pyro4.Proxy(self.serverAdress)
        except Exception:
            self.parent.exception()
        

    def runSQLQuery(self,SQLquery, bindings):
        return self.server.executeSql(SQLquery,bindings)

        
    def logIn(self,user,password):
        if user.strip()== "" or password.strip() == "":
            return False
        else:
            message= self.server.loginValidation(user,password)
            print(message)
            return message

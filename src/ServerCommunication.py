import Pyro4


class ServerCommunication():
    def __init__(self,parent):
        self.serverAdress = "PYRO:foo@184.162.124.218:8000"
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

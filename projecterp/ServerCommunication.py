import Pyro4

class ServerCommunication():
    def __init__(self):
        self.serverAdress = "PYRO:foo@10.57.47.23:43225"
        self.status = None
        self.server = None
        
    def connectToServer(self):
        self.server = Pyro4.Proxy(self.serverAdress)
        
    def testServer(self):   
        string = input("TEST TEST TEST, BONJOUR ANTOINE!!!!")
        reponse = self.server.loginValidation(string)
        print ( reponse )
        
    def runSQLQuery(self,SQLquery):
        self.server.runQuery(SQLquery)
        
    def logIn(self,user,password):
        if user.strip() or password.strip() == "":
            return False
        else:
            return self.server.loginValidation(user,password)
            
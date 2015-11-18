class Formulaire():
    def __init__(self, parent):
        self.nom = None
        self.parent = parent
        self.formsList = []

    def getTables(self):
        sqlQuery = "SELECT nom FROM Sys_Formulaires"
        self.formsList = self.parent.parent.serverCommunication.runSQLQuery(sqlQuery)
        return self.formsList 
        
    def getForms(self):
        sqlQuery = "SELECT nom FROM Sys_Formulaires"
        print("YOO", self.parent)
        print("YOO#2", self.parent.parent)
        self.formsList = self.parent.parent.serverCommunication.runSQLQuery(sqlQuery)
        return self.formsList

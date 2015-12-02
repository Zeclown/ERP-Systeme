class Formulaire():
    def __init__(self, parent):
        self.nom = None
        self.parent = parent
        self.formsList = []
        self.tableList = []
        self.tableColumns = []
        self.columnsNames = []

    def getAllTablesOfDataBase(self):
        sqlQuery = "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'Dyn_%'"
        self.tableList = self.parent.parent.serverCommunication.runSQLQuery(sqlQuery,None)
        return self.tableList

    def getTableColumnName(self, table):
        #print("Table name : ",table)
        sqlQuery = "PRAGMA table_info('%s')" %(table)
        self.tableColumns = self.parent.parent.serverCommunication.runSQLQuery(sqlQuery,None)
        #print("Results from query : ",self.tableColumns)
        #print("Number of items",len(self.tableColumns))
        self.columnsNames.clear()
        for i in self.tableColumns:
            self.columnsNames.append([i[1],i[2]])
        return self.columnsNames

        
    def getForms(self):
        sqlQuery = "SELECT nom FROM Sys_Formulaires"
        self.formsList = self.parent.parent.serverCommunication.runSQLQuery(sqlQuery,None)
        return self.formsList

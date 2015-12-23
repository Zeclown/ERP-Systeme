class Table():
    def __init__(self,parent):
        self.nom = None
        self.column = []
        self.parent=parent

    def createNewTable(self,tableName,columns):
        tableName=tableName.replace(" ", "")
        sqlCommand="CREATE TABLE Dyn_" + tableName + " ("        
        for column in columns.keys():
            nouvellecolumn=column.replace(" ", "")
            sqlCommand+=" " + nouvellecolumn + " " + columns[column]+","
        sqlCommand=sqlCommand[:-1]
        sqlCommand+=" )"
        print(sqlCommand)
        self.parent.parent.serverCommunication.runSQLQuery(sqlCommand,None)

    def modifyTable(self,tableName,columns):
        tableName=tableName.replace(" ", "")
        sqlCommand="DROP TABLE "+tableName
        self.parent.parent.serverCommunication.runSQLQuery(sqlCommand,None)
        sqlCommand="CREATE TABLE " + tableName + " ("        
        for column in columns.keys():
            nouvellecolumn=column.replace(" ", "")
            sqlCommand+=" " + nouvellecolumn + " " + columns[column]+","
        sqlCommand=sqlCommand[:-1]
        sqlCommand+=" )"
        self.parent.parent.serverCommunication.runSQLQuery(sqlCommand,None)

    def deleteTable(self,tableName):
        sqlCommand="DROP TABLE "+tableName
        self.parent.parent.serverCommunication.runSQLQuery(sqlCommand,None)

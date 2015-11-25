


class Table():
    def __init__(self,parent):
        self.nom = None
        self.column = []
        self.parent=parent
    def createNewTable(self,tableName,columns):
        sqlCommand="CREATE TABLE Dyn_" + tableName + " ("        
        for column in columns.keys():
            sqlCommand+=" " + column + " " + columns[column]+","
        sqlCommand=sqlCommand[:-1]
        sqlCommand+=" )"
        self.parent.parent.serverCommunication.runSQLQuery(sqlCommand,None)
    def modifyTable(self,tableName,columns):
        sqlCommand="DROP TABLE "+tableName
        self.parent.parent.serverCommunication.runSQLQuery(sqlCommand,None)
        self.createNewTable(tableName, columns)



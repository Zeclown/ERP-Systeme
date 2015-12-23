import time

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

    def getFormsSpecs(self, name):
        sqlQuery = "SELECT id FROM Sys_Formulaires WHERE nom = '%s'" % (name)
        result = self.parent.parent.serverCommunication.runSQLQuery(sqlQuery,None)

        sqlQuery = "SELECT nomTable, colonne, label, typeView, valeurs, description FROM Sys_Form_Spec WHERE form_id = '%i'" % (result[0])
        specsForm = self.parent.parent.serverCommunication.runSQLQuery(sqlQuery,None)

        return specsForm

    def createForm(self, name, formItemList):
        sqlQuery = "INSERT INTO Sys_Formulaires Values"
        bindings = [ None, name, self.getDate(), self.getDate(), None, None]
        self.parent.parent.serverCommunication.runSQLQuery(sqlQuery, bindings)

        for item in formItemList:
            index = item[0].find(".")
            lenght = len(item[0])
            print("----------FORMULAIRE----------")
            print("Table ->", item[0][0:index])
            print("Colonne ->", item[0][index+1:lenght])
            print("Label ->", item[1])
            print("TypeVue ->", item[2])
            print("Valeurs ->", item[3])
            print("Description", item[4])
            print("------------------------------")

            sqlQuery = "INSERT INTO Sys_Form_Spec Values"
            bindings = [ None, self.getLastIdOfSys_Formulaires(), item[0][0:index], item[0][index+1:lenght], item[1], item[2], item[3], item[4]]
            self.parent.parent.serverCommunication.runSQLQuery(sqlQuery, bindings)

    def getLastIdOfSys_Formulaires(self):
        sqlQuery = "SELECT id FROM Sys_Formulaires ORDER BY id DESC"
        idResult = self.parent.parent.serverCommunication.runSQLQuery(sqlQuery, None)
        if not idResult:
            result = 1
        else:
            result = idResult[0][0]
        return result

    def getDate(self):
        return time.strftime("%x")

from copy import deepcopy
from static.classes.datacontroller.IDataManager import IDataConnector


class SQLCloud(IDataConnector):
    """
        SQLCloud

    Klasa stwożona dla pobierania, generowania oraz sterowania
    Bazą Danych w jak najmniej
    """
    __instance = None
    # MySQLdb.connect()    __table = None
    DBRepr = dict()

    def __init__(self, db_name='test_cloud'):
        ''' Private constructor  '''
        IDataConnector.__init__(self, db_name)
        cursor = self._connector.cursor()
        self.__table = cursor.execute("SHOW TABLES")
        cursor.close()
        self.__table__Constract()
        if (SQLCloud.__instance == None):
            SQLCloud.__instance = self

    @staticmethod
    def getInstance():
        ''' Static access method '''
        if (SQLCloud.__instance == None):
            SQLCloud()
        return SQLCloud.__instance

    def __table__Constract(self):
        __cursor = self._connector.cursor()
        __cursor.execute("SHOW TABLES")
        tabels = __cursor.fetchall()
        data = dict()
        for tabel in tabels:
            __cursor.execute("SHOW COLUMNS FROM "+tabel[0])
            data.update({ tabel[0] : tuple([x[0] for x in __cursor.fetchall()]) })
        self.DBRepr = data

    def _table__with__type(self, table_name):
        __cursor = self._connector.cursor()
        data = dict()
        __cursor.execute("SHOW COLUMNS FROM " + table_name)
        data.update({table_name: tuple((x[0],x[1]) for x in __cursor.fetchall())})
        self._DBTypeDICT = data

    def insert(self, tableName: str) -> bool:
        """
             Insert

        Twoży metody dodawania wierszy
        do tabeli o podanej nezwie
        :param tableName:
        :return: T/F

        @Serhii Riznychuk
        """
        columns = deepcopy(self.DBRepr[tableName])
        String = "def insert_" + tableName + "(self, " + ", ".join((columns[1:])) + "):\n"
        String = String + "\tsql = \"INSERT INTO `banns`(" + ", ".join(
            ("`" + column + "`" for column in columns[1:])) + ") VALUES (" + ", ".join(
            ("%s" for x in columns[1:])) + ")\"\n"
        String = String + "\t__cursor = self._connector.cursor()\n"
        String = String + "\t__cursor.execute(sql, (" + ", ".join((column for column in columns[1:])) + "))\n"
        String = String + "\tself._connector.commit()\n"
        String = String + "\t__cursor.close()\n"
        String = String + "\treturn 0\n"
        String = "self.insert_" +tableName+"=insert_"+tableName
        try:
            exec(String)
            return True
        except:
            return False

    def update(self, table: str) -> bool:
        """
             Update

        Twoży metodę updatowania danych
        z tabelil o podaje nazwie
        :param table: nazwa tabeli której sie twożona dynamiczna metoda.
        :return: T/F

        @Serhii Riznychuk
        """
        String = "def update_" + table + "(self, **sets):\n"
        String = String + "\tdef functionInside(**whr):\n"
        String = String + "\t\tsql = \"UPDATE `" + table + """` SET "+", ".join(("`"+key+"`=%s" for key, value in sets.items()))+" WHERE "+" AND ".join(("`"+key+"`=%s" for key, v in whr.items()))\n"""
        String = String + "\t\t__cursor = self._connector.cursor()\n"
        String = String + "\t\t__cursor.execute(sql, (([value for key, value in sets.items()]+[value for key, value in whr.items()])))\n"
        String = String + "\t\tself._connector.commit()\n"
        String = String + "\t\t__cursor.close()\n"
        String = String + "\treturn functionInside\n"
        String = "self.update_" + table + "=update_" + table
        try:
            exec(String)
            return True
        except:
            return False

    def select(self, tableName: str) -> bool:
        """
            Select

        Twoży metode pobierania danych
        z tabeli o nazwie tableName
        :param tableName: nazwa tabeli której sie twożona dynamiczna metoda.
        :return: T/F

        @Serhii Riznychuk
        """
        String = "def select_" + tableName + "(self, **wheres):\n"
        String = String + "\tsql=\"SELECT * FROM `" + tableName + "`\"\n"
        String = String + "\tif(len(wheres) > 0):\n"
        String = String + "\t\tsql = sql + \" WHERE \" + \" AND \".join([\"`\"+str(key)+\"`=%s\" for key, value in wheres.items()])\n"
        String = String + "\t__cursor = self._connector.cursor()\n"
        String = String + "\t__cursor.execute(sql, tuple(( wheres[key] for key, value in wheres.items() ))"
        String = String + "\treturn __cursor.fetchall()\n"
        String = "self.select_" + tableName + "= select_" + tableName
        try:
            exec(String)
            return True
        except:
            return False

    def delete(self, tableName: str) -> bool:
        """
           Delete

        Twoży metode zniszczenia danych
        z tabeli o nazwie tableName
        :param tableName: nazwa tabeli której sie twożona dynamiczna metoda.
        :return: T/F

        @Serhii Riznychuk
        """
        String = "def delete_" + tableName + "(self, **kwargs):\n"
        String = String + '\tsql = "DELETE FROM `' + tableName + '`\"\n'
        String = String + '\tif(len(kwargs) > 0):\n'
        String = String + '\t\tsql = sql + " WHERE "+" AND ".join([\"`\"+str(key)+"`=%s" for key, value in kwargs.items()])\n'
        String = String + '\t__cursor = self._connector.cursor()\n'
        String = String + '\t__cursor.execute(sql, tuple(( kwargs[key] for key, value in kwargs.items())))\n'
        String = String + "\tself._connector.commit()\n"
        String = String + "\t__cursor.close()\n"
        String = String + "\treturn 0\n"
        String = "self.delete_" + tableName + "= delete_" + tableName
        try:
            exec(String)
            return True
        except:
            return False

    def merge(self, *args: list, where: dict={}) -> dict:
        before = lambda _id: str(args[args.index(_id)-1])
        after = lambda _id: str(args[args.index(_id)+1])
        concatinate = lambda tableName, _id: str(tableName)+"."+str(_id)

        if(len(args) % 2 != 0 and len(args) > 1):
            sql = "SELECT * FROM"+",".join([" `{}`".format(tablename) for tablename in args[0::2]])+" WHERE "
            sql = sql + " AND ".join([ "{}={}".format(concatinate(before(id), id), concatinate(after(id), id)) for id in args[1::2]])
            if(len(where) > 0):
                sql = sql + " AND " + " AND ".join(["{}={}".format(key,str(where[key])) for key, _ in where.items()])
            cursor = self._connector.cursor()
            cursor.execute(sql)
            cursor.close()
            return cursor.fetchall()
        return dict()





# costam.update_banns(idUser=5)(timeStamp=datetime.date(2009, 10, 18).isoformat(), status=1)
# costam.delete_banns(idUser=2)

from copy import deepcopy
from static.tool.console.vt1000 import BackGround as bg, ForeGround as fg, FormatCode as cd
from static.classes.datacontroller.IDataManager import IDataConnector
from static.tool.console.vt1000 import getTerminalSize
from types import MethodType


class SQLCloud(IDataConnector):
    """
        SQLCloud

    Klasa stwożona dla pobierania, generowania oraz sterowania
    Bazą Danych w jak najmniej
    """
    #__instance = None
    # MySQLdb.connect()    __table = None
    DBRepr = dict()

    def __init__(self, db_name : str ='test_cloud'):
        ''' Private constructor  '''
        super(SQLCloud, self).__init__()
        cursor = self._connector.cursor()
        self.__table = cursor.execute("SHOW TABLES")
        cursor.close()
        self.__table__Constract()
        #if (SQLCloud.__instance == None):
        #   SQLCloud.__instance = self
    """
    @staticmethod
    def getInstance():
        ''' Static access method '''
        if (SQLCloud.__instance == None):
            SQLCloud()
        return SQLCloud.__instance
    """
    def __table__Constract(self):
        __cursor = self._connector.cursor()
        __cursor.execute("SHOW TABLES")
        tabels = __cursor.fetchall()
        data = dict()
        for tabel in tabels:
            __cursor.execute("SHOW COLUMNS FROM "+tabel[0])
            data.update({ tabel[0] : tuple([x[0] for x in __cursor.fetchall()]) })
        self.DBRepr = data

    def _getTableMeta(self, table_name):
        __cursor = self._connector.cursor()
        data = list()
        __cursor.execute("SHOW COLUMNS FROM " + table_name)
        data= [(x[0],x[1]) for x in __cursor.fetchall()]
        return data

    def print(self, table : str = None):
        # selT = bg.white+fg.black
        # selC = bg.lightgrey+fg.cyan
        Header = lambda name="Tables": cd.bold+bg.black+fg.cyan+"{:^11}".format(name)+cd.reset+"   "
        print(Header()+Header("Columns")+"\n"+"\n".join([bg.white+fg.black+"{:<11}{} : {}".format(x, cd.reset,"|".join([bg.black+"{:^16}".format(str(z))+cd.reset for z in values])) for x, values in self.DBRepr.items()]))

    def insert(self, tableName: str):
        """
             Insert

        Twoży metody dodawania wierszy
        do tabeli o podanej nezwie
        :param tableName:
        :return: function

        @Serhii Riznychuk
        """
        columns = deepcopy(self.DBRepr[tableName])
        String = "def insert_" + tableName + "(self, " + ", ".join((columns[1:])) + "):\n"
        String = String + "\tsql = \"INSERT INTO `"+tableName+"`(" + ", ".join(
            ("`" + column + "`" for column in columns[1:])) + ") VALUES (" + ", ".join(
            ("%s" for x in columns[1:])) + ")\"\n"
        # String = String + "\tprint(\"SQL : \""+","+",\"|\",".join((columns[1:]))+")\n"
        String = String + "\tcursor = self._connector.cursor()\n"
        String = String + "\tcursor.execute(sql, (" + ", ".join((column for column in columns[1:])) + ",))\n"
        String = String + "\tself._connector.commit()\n"
        String = String + "\tcursor.close()\n"
        String = String + "\treturn 0\n"
        String = String + "self.insert_"+tableName+" = MethodType(insert_"+tableName+", self)\n"
        try:
            exec(String)
            return getattr(self, "insert_"+tableName)
        except Exception as n:
            _, column = getTerminalSize()
            print("{:-^{column}}".format("Data Base ERROR", column=column))
            return None


    def update(self, tableName: str):
        """
             Update

        Twoży metodę updatowania danych
        z tabelil o podaje nazwie
        :param tableName: nazwa tabeli której sie twożona dynamiczna metoda.
        :return: function

        @Serhii Riznychuk
        """
        String = "def update_" + tableName + "(**sets):\n"
        String = String + "\tdef functionInside(**whr):\n"
        String = String + "\t\tsql = \"UPDATE `" + tableName + """` SET "+", ".join(("`"+key+"`=%s" for key, value in sets.items()))+" WHERE "+" AND ".join(("`"+key+"`=%s" for key, v in whr.items()))\n"""
        String = String + "\t\t__cursor = self._connector.cursor()\n"
        String = String + "\t\t__cursor.execute(sql, (([value for key, value in sets.items()]+[value for key, value in whr.items()])))\n"
        String = String + "\t\tself._connector.commit()\n"
        String = String + "\t\t__cursor.close()\n"
        String = String + "\treturn functionInside\n"
        String = String + "self.update_" + tableName + " = MethodType(update_" + tableName + ", self)\n"
        try:
            exec(String)
            return getattr(self, "update_" + tableName)
        except Exception as n:
            _, column = getTerminalSize()
            print("{:-^{column}}".format("Data Base ERROR", column=column))
            return None

    def select(self, tableName: str):
        """
            Select

        Twoży metode pobierania danych
        z tabeli o nazwie tableName
        :param tableName: nazwa tabeli której sie twożona dynamiczna metoda.
        :return: function

        @Serhii Riznychuk
        """
        String = "def select_" + tableName + "(self, **wheres):\n"
        String = String + "\tsql=\"SELECT * FROM `" + tableName + "`\"\n"
        String = String + "\tif(len(wheres) > 0):\n"
        String = String + "\t\tsql = sql + \" WHERE \" + \" AND \".join([\"`\"+str(key)+\"`=%s\" for key, value in wheres.items()])\n"
        #String = String + "\t\tprint(sql)\n"
        String = String + "\t__cursor = self._connector.cursor()\n"
        String = String + "\t__cursor.execute(sql, (( wheres[key] for key, value in wheres.items())))\n"
        String = String + "\treturn __cursor.fetchall()\n"
        String = String + "self.select_" + tableName + " = MethodType(select_" + tableName + ", self)\n"
        try:
            exec(String)
            return getattr(self, "select_" + tableName)
        except Exception as n:
            _, column = getTerminalSize()
            print("{:-^{column}}".format("Data Base ERROR", column=column))
            return None

    def like(self, tableName: str):
        """
            like

        Twoży metode pobierania danych
        z tabeli o nazwie tableName
        :param tableName: nazwa tabeli której sie twożona dynamiczna metoda.
        :return: function

        @Serhii Riznychuk
        """
        String = "def like_" + tableName + "(self, **likes):\n"
        String = String + "\tsql=\"SELECT * FROM `" + tableName + "`\"\n"
        String = String + "\tif(len(likes) > 0):\n"
        String = String + '\t\tsql = sql + \" WHERE \" + \" AND \".join([ str(key)+" LIKE %s" for key, value in likes.items()])\n'
        #String = String + "\t\tprint(sql, likes)\n"
        String = String + "\t__cursor = self._connector.cursor()\n"
        String = String + "\t__cursor.execute(sql, tuple(( likes[key] for key, value in likes.items())))\n"
        String = String + "\treturn __cursor.fetchall()\n"
        String = String + "self.like_" + tableName + " = MethodType(like_" + tableName + ", self)\n"
        # print(String)
        try:
            exec(String)
            return getattr(self, "like_"+tableName)
        except Exception as n:
            _, column = getTerminalSize()
            print("{:-^{column}}".format("Data Base ERROR", column=column))
            return None

    def delete(self, tableName: str):
        """
           Delete

        Twoży metode zniszczenia danych
        z tabeli o nazwie tableName
        :param tableName: nazwa tabeli której sie twożona dynamiczna metoda.
        :return: function

        @Serhii Riznychuk
        """
        String = "def delete_" + tableName + "(self, **kwargs):\n"
        String = String + '\tsql = "DELETE FROM `' + tableName + '`\"\n'
        String = String + '\tif(len(kwargs) > 0):\n'
        String = String + '\t\tsql = sql + " WHERE "+" AND ".join([\"`\"+str(key)+\"`=%s\" for key, value in kwargs.items()])\n'
        String = String + "\t\tprint(sql, kwargs)\n"
        String = String + '\t__cursor = self._connector.cursor()\n'
        String = String + '\t__cursor.execute(sql, tuple(( kwargs[key] for key, value in kwargs.items())))\n'
        String = String + "\tself._connector.commit()\n"
        String = String + "\t__cursor.close()\n"
        String = String + "\treturn 0\n"
        String = String + "self.delete_" + tableName + " = MethodType(delete_" + tableName + ", self)\n"
        print(String)
        try:
            exec(String)
            return getattr(self, "delete_" + tableName)
        except Exception as n:
            _, column = getTerminalSize()
            print("{:-^{column}}".format("Data Base ERROR", column=column))
            return None

    def merge(self, *args, where: dict={}) -> dict:
        before = lambda _id: str(args[args.index(_id)-1])
        after = lambda _id: str(args[args.index(_id)+1])
        concatinate = lambda tableName, _id: str(tableName)+"."+str(_id)

        if(len(args) % 2 != 0 and len(args) > 1):
            sql = "SELECT * FROM"+",".join([" `{}`".format(tablename) for tablename in args[0::2]])+" WHERE "
            sql = sql + " AND ".join([ "{}={}".format(concatinate(before(id), id), concatinate(after(id), id)) for id in args[1::2]])
            if(len(where) > 0):
                sql = sql + " AND " + " AND ".join(["{}={}".format(key,str(where[key])) for key, _ in where.items()])
            #print(sql)
            cursor = self._connector.cursor()
            cursor.execute(sql)
            # cursor.close()
            return cursor.fetchall()
        return dict()


import MySQLdb
from copy import deepcopy

class SQLCloud(object):

    __instance = None
    __connector = None
    # MySQLdb.connect('trashpanda.pwsz.nysa.pl', 'sergiy1998', 'hspybxeR98>', 'test_cloud')
    __cursor = None
    __table = None
    DBRepr = dict()
    def __init__(self, host='trashpanda.pwsz.nysa.pl', login='sergiy1998', passwd='hspybxeR98>', db_name='test_cloud'):
        ''' Private constructor  '''

        self.__connector = MySQLdb.connect(host, login, passwd, db_name)
        self.__cursor = self.__connector.cursor()
        self.__table = self.__cursor.execute("SHOW TABLES")

        self.__table__Constract()
        if SQLCloud.__instance == None:
            SQLCloud.__instance = self


    @staticmethod
    def getInstance():
        ''' Static access method '''
        if (SQLCloud.__instance == None):
            SQLCloud()
        return SQLCloud.__instance

    def __table__Constract(self):
        __cursor = self.__connector.cursor()
        __cursor.execute("SHOW TABLES")
        tabels = __cursor.fetchall()
        data = dict()
        for tabel in tabels:
            __cursor.execute("SHOW COLUMNS FROM "+tabel[0])
            data.update({ tabel[0] : tuple([x[0] for x in __cursor.fetchall()]) })
        self.DBRepr = data

    def insert_user(self, one, more, time):
        sql = "INSERT INTO `banns`(`one`, `more`, `time`) VALUES (%s, %s, %s)"
        __cursor = self.__connector.cursor()
        __cursor.execute(sql, (one, more, time))
        return 1

    def insert(self, tableName):
        columns = deepcopy(self.DBRepr[tableName])
        string = "def insert_" + tableName + "(self, " + ", ".join((columns[1:])) + "):\n"
        string = string + "\tsql = \"INSERT INTO `banns`(" + ", ".join(
            ("`" + column + "`" for column in columns[1:])) + ") VALUES (" + ", ".join(
            ("%s" for x in columns[1:])) + ")\"\n"
        string = string + "\t__cursor = self.__connector.cursor()\n"
        string = string + "\t__cursor.execute(sql, (" + ", ".join((column for column in columns[1:])) + "))\n"
        string = string + "\treturn 0\n"
        return string

    def update(self, table):
        string = "def update_" + table + "(self, **sets):\n"
        string = string + "\tdef functionInside(**whr):\n"
        string = string + "\t\tsql = \"UPDATE `" + table + """` SET "+", ".join(("`"+key+"`=%s" for key, value in sets.items()))+" WHERE "+" AND ".join(("`"+key+"`=%s" for key, v in whr.items()))\"\n"""
        string = string + "\t\t__cursor = self.__connector.cursor()\n"
        string = string + "\t\t__cursor.execute(sql, (([value for key, value in sets.items()]+[value for key, value in whr.items()])))\n"
        string = string + "\treturn functionInside"
        return string

    def select(self, tableName):
        String = "def select_" + tableName + "(self, **wheres):\n"
        String = String + "\tsql=\"SELECT * FROM `" + tableName + "`\"\n"
        String = String + "\tif(len(wheres) > 0):\n"
        String = String + "\t\tsql = sql + \" WHERE \" + \" AND \".join([\"`\"+str(key)+\"`=%s\" for key, value in wheres.items()])\n"
        String = String + "\t__cursor = self.__connector.cursor()\n"
        String = String + "\t__cursor.execute(sql, tuple(( kwargs[+key+] for key, value in wheres.items() )"
        String = String + "\treturn __cursor.fetchall()\n"
        return String

    def delete(self, tableName):
        String = "def delete_" + tableName + "(self, **kwargs):\n"
        String = String + '\tsql = "DELETE FROM `' + tableName + '`\n'
        String = String + '\tif(len(kwargs) > 0):\n'
        String = String + '\t\tsql = sql " WHERE "+" AND ".join([\"`\"+str(key)+"`=%s" for key, value in kwargs.items()])\n'
        String = String + '\t__cursor = self.__connector.cursor()\n'
        String = String + '\t__cursor.execute(sql, tuple(( kwargs[+key+] for key, value in kwargs.items())))\n'
        return String


los = lambda : "".join(("-" for x in range(0, 70)))

costam = SQLCloud.getInstance()
print(costam.DBRepr)
print(los())
print(costam.insert('banns'))
print(los())
print(costam.update('banns'))
print(los())
print(costam.select('banns'))
print(los())
print(costam.delete('banns'))
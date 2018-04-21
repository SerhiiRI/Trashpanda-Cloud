from static.tool.console.vt1000 import fg, bg, cd
import MySQLdb, random
import datetime
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
        String = "def insert_" + tableName + "(self, " + ", ".join((columns[1:])) + "):\n"
        String = String + "\tsql = \"INSERT INTO `banns`(" + ", ".join(
            ("`" + column + "`" for column in columns[1:])) + ") VALUES (" + ", ".join(
            ("%s" for x in columns[1:])) + ")\"\n"
        String = String + "\t__cursor = self.__connector.cursor()\n"
        String = String + "\t__cursor.execute(sql, (" + ", ".join((column for column in columns[1:])) + "))\n"
        String = String + "\tself.__connector.commit()\n"
        String = String + "\t__cursor.close()\n"
        String = String + "\treturn 0\n"
        return String

    def update(self, table):
        String = "def update_" + table + "(self, **sets):\n"
        String = String + "\tdef functionInside(**whr):\n"
        String = String + "\t\tsql = \"UPDATE `" + table + """` SET "+", ".join(("`"+key+"`=%s" for key, value in sets.items()))+" WHERE "+" AND ".join(("`"+key+"`=%s" for key, v in whr.items()))\n"""
        String = String + "\t\t__cursor = self.__connector.cursor()\n"
        String = String + "\t\t__cursor.execute(sql, (([value for key, value in sets.items()]+[value for key, value in whr.items()])))\n"
        String = String + "\t\tself.__connector.commit()\n"
        String = String + "\t\t__cursor.close()\n"
        String = String + "\treturn functionInside\n"
        return String

    def select(self, tableName):
        String = "def select_" + tableName + "(self, **wheres):\n"
        String = String + "\tsql=\"SELECT * FROM `" + tableName + "`\"\n"
        String = String + "\tif(len(wheres) > 0):\n"
        String = String + "\t\tsql = sql + \" WHERE \" + \" AND \".join([\"`\"+str(key)+\"`=%s\" for key, value in wheres.items()])\n"
        String = String + "\t__cursor = self.__connector.cursor()\n"
        String = String + "\t__cursor.execute(sql, tuple(( wheres[key] for key, value in wheres.items() ))"
        String = String + "\treturn __cursor.fetchall()\n"
        return String

    def delete(self, tableName):
        String = "def delete_" + tableName + "(self, **kwargs):\n"
        String = String + '\tsql = "DELETE FROM `' + tableName + '`\"\n'
        String = String + '\tif(len(kwargs) > 0):\n'
        String = String + '\t\tsql = sql + " WHERE "+" AND ".join([\"`\"+str(key)+"`=%s" for key, value in kwargs.items()])\n'
        String = String + '\t__cursor = self.__connector.cursor()\n'
        String = String + '\t__cursor.execute(sql, tuple(( kwargs[key] for key, value in kwargs.items())))\n'
        String = String + "\tself.__connector.commit()\n"
        String = String + "\t__cursor.close()\n"
        String = String + "\treturn 0\n"
        return String


    def join(self, *args):
        sql = "SELECT * FROM `"+ args[0]+"`"


los = lambda : "".join(("_" for x in range(0, 200)))

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
print(los())

def kolorise(func):
    def inFunc(foreground=fg.cyan, background=bg.black):
        String = foreground+ +  + cd.reset


los()
"""
for x in range(10):
    now = datetime.date((int("20"+str(random.randint(10,99)))), 10, 18)
    str_now = now.isoformat()
    costam.insert_banns(1, x, str_now)
"""
# costam.update_banns(idUser=5)(timeStamp=datetime.date(2009, 10, 18).isoformat(), status=1)
costam.delete_banns(idUser=2)

import threading, MySQLdb, pickle, random
from static.classes.interfaces.IRunnable import IRunnable
from multiprocessing import Queue

class Container(threading.Thread):

    def __init__(self, table, dependProcess="/home/serhii/Projects/llapCloudFlask/static/tool/Binary/cpuController"):
        self.table = table
        self.controller = dependProcess
        host = 'trashpanda.pwsz.nysa.pl'
        login = 'sergiy1998'
        passwd = 'hspybxeR98>'
        db_name = 'pipeline'
        ''' Private constructor  '''
        self.__connector = MySQLdb.connect(host, login, passwd, db_name)
        self.__cursor = self.__connector.cursor()
        self.__table = self.__cursor.execute("SHOW TABLES")
        threading.Thread.__init__(self)

    def __getObject(self):
        sql = "SELECT * FROM `%s` ORDER BY id ASC LIMIT 1"
        __cursor = self.__connector.cursor()
        __cursor.execute(sql, tuple(self.table))
        return __cursor.fetchall()

    def __rmObject(self, object_id):
        sql = "DELETE FROM `%s` WHERE `id`=%s"
        __cursor = self.__connector.cursor()
        __cursor.execute(sql, tuple(self.table, object_id))

    def run(self):
        costam = self.GetFirstObject()
        Runner = pickle.load(costam)

    def sqlSelect(self, table_name):
        pass
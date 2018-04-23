#!/usr/bin/python3
import threading, MySQLdb
import pickle
from static.classes.interfaces.IRunnable import IRunnable
import random
class PipeBuilder(object):
    """ the pipeline"""

    def createTable(self):
        sql = "CREATE TABLE %s (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, obj TEXT NOT NULL)"
        sql = "DROP TABLE %s"


"""    
    __data = list()
    def __init__(self, data):
        self.data = data
        self.lenOfData = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.lenOfData <= 0 :
            raise StopIteration
        else:
            self.lenOfData -=1
        return self.data[self.lenOfData-1]*self.data[self.lenOfData-1]


print([x for x in PipeLine([1, 2, 3, 4])])
"""

class theadingObject(threading.Thread):

    def __init__(self, func, values):

        self.function = func
        self.parameter = values
        threading.Thread.__init__(self)




    def run(self):
        try:
            self.function(self.parameter)
        except:
            raise Exception



class Container:

    def __init__(self, table, dependProcess="/home/serhii/Projects/llapCloudFlask/static/tool/Binary/cpuController"):
        self.table =table
        self.controller = dependProcess
        host='trashpanda.pwsz.nysa.pl'
        login='sergiy1998'
        passwd='hspybxeR98>'
        db_name='pipeline'
        ''' Private constructor  '''
        self.__connector = MySQLdb.connect(host, login, passwd, db_name)
        self.__cursor = self.__connector.cursor()
        self.__table = self.__cursor.execute("SHOW TABLES")
        
    def __getObject(self):
        sql = "SELECT * FROM `%s` ORDER BY id ASC LIMIT 1"
        __cursor = self.__connector.cursor()
        __cursor.execute(sql, tuple(self.table))
        return __cursor.fetchall()

    def __rmObject(self, object_id):
        sql = "DELETE FROM `%s` WHERE `id`=%s"
        __cursor = self.__connector.cursor()
        __cursor.execute(sql, tuple(self.table, object_id))

    def start(self):
            costam = self.GetFirstObject()
            Runner = pickle.load(costam)


    def sqlSelect(self, table_name):
        pass


def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


from subprocess import Popen, PIPE
proc = Popen(("/home/serhii/Projects/llapCloudFlask/static/tool/Binary/cpuController",), shell=True, stdout=PIPE)
proc.wait()
res = proc.communicate()
print("result", res[0].decode("utf-8"))
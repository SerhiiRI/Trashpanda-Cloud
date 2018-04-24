#!/usr/bin/python3
import threading, MySQLdb, pickle, random
from flask_sqlalchemy import SQLAlchemy
from static.classes.interfaces.IRunnable import IRunnable
from multiprocessing import Queue
from .Process import Process


class PipeBuilder(object):
    """ the pipeline"""

    __queue = Queue()
    __table = 0

    def __init__(self, function, controllers:list):

        self.controllers = controllers
        self.function = function
        host = 'trashpanda.pwsz.nysa.pl'
        login = 'sergiy1998'
        passwd = 'hspybxeR98>'
        db_name = 'pipeline'
        self.__connector = MySQLdb.connect(host, login, passwd, db_name)
        self.__cursor = self.__connector.cursor()
        self.__tables = self.__cursor.execute("SHOW TABLES")
        self._createQueueTable()

    def _createQueueTable(self):
        sql = "CREATE TABLE IF NOT EXISTS %s (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, obj TEXT NOT NULL)"
        __cursor = self.__connector.cursor()
        __cursor.execute(sql, tuple(self.__table))
        self.__connector.commit()

    def _deleteTable(self):
        sql = "DROP TABLE %s"
        __cursor = self.__connector.cursor()
        __cursor.execute(sql, tuple(self.__table))
        self.__connector.commit()
        return __cursor.fetchall()



    def _addObject(self):
        tempProcessObject = Process(self.function, tuple(10, ), self.controllers)
        stringProcessObject = pickle.dump(tempProcessObject)
        sql = "INSERT INTO `banns`(`id`, `object`) VALUES (NULL, %s)"
        __cursor = self.__connector.cursor()
        __cursor.execute(sql, (stringProcessObject))
        self.__connector.commit()
        __cursor.close()



    def buildTasks(self):
        self.__queue.put()

    def buildQueue(self):
        self.__queue.put()










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
def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

"""
from subprocess import Popen, PIPE
proc = Popen(("/home/serhii/Projects/llapCloudFlask/static/tool/Binary/cpuController",), shell=True, stdout=PIPE)
proc.wait()
res = proc.communicate()
print("result", res[0].decode("utf-8"))
"""
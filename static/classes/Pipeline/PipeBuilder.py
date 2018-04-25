#!/usr/bin/python3
import threading, MySQLdb, pickle, random
from multiprocessing import Queue
from .Process import Process
from .Controller import Controller

class PipeBuilder(object):
    """
                PipeBuilder
    """

    __queue = Queue()
    __table = None

    def __init__(self, function, controllers: Controller ):
        """
                      __init__
          __Konstruktor__ klasy PipeBuilder
        --------------------------------------
         Twożenia polączenia z bazą danych,or-
        az twożenia konektora na podstawie po-
        lączneia, i przypisywania do poszczeg-
        ólnych parametrów klasy węwnętrzenej
         Na koncu twoży tabele w BD o nazwie
        funkcji.

        :param function: funkcja dla definiowania Objektu typu Process
        :param controllers: objekt typu Controller, slużący dla odpalemnia go w Contenerze.
        TODO: jeden(Obj) -> wielu(tuple(Obj,...)))

        @Serhii Riznychuk
        """

        self.controllers = controllers
        self.function = function
        self.__table = function.__name__
        host = 'trashpanda.pwsz.nysa.pl'
        login = 'sergiy1998'
        passwd = 'hspybxeR98>'
        db_name = 'pipeline'
        self.__connector = MySQLdb.connect(host, login, passwd, db_name)
        self.__cursor = self.__connector.cursor()
        self.__tables = self.__cursor.execute("SHOW TABLES")
        self._createQueueTable()

    def _createQueueTable(self):
        """
        private: CreateQueueTable
        ---------------------------
        Twożenia tabeli jeżeli tak-
        iej nie istnieje dla podan-
        ej nazwy, przychowywaniej w
        zmiennej self.__table

        :return: True
        @Serhii Riznychuk
        """
        sql = "CREATE TABLE IF NOT EXISTS %s (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, obj TEXT NOT NULL)"
        __cursor = self.__connector.cursor()
        __cursor.execute(sql, tuple(self.__table))
        self.__connector.commit()
        return True

    def _deleteTable(self):
        """
        private: DeleteTable
        ----------------------------
        Zniszczenia tabeli o wlasnej
        nazwie self.__table

        :return: Boolean

        @Serhii Rinzychuk
        """
        sql = "DROP TABLE %s"
        __cursor = self.__connector.cursor()
        __cursor.execute(sql, tuple(self.__table))
        self.__connector.commit()
        return True

    def _addObject(self):
        """
                    Add Object
        ----------------------------------
        Twożnia objektu typu class process,
        oraz seralizwania go za pomocą mo-
        dula pickle i polecenia dump(obj)
        dopisywania do bazy danych

        @Serhii Riznychuk
        """
        tempProcessObject = Process(self.function, tuple(10, ), self.controllers)
        # pickle.dump - serializacja objektu
        stringProcessObject = pickle.dump(tempProcessObject)
        sql = "INSERT INTO `"+self.__table+"`(`id`, `object`) VALUES (NULL, %s)"
        __cursor = self.__connector.cursor()
        __cursor.execute(sql, (stringProcessObject))
        del(tempProcessObject)
        del(stringProcessObject)
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
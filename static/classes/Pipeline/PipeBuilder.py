#!/usr/bin/python3
#import pickle
import _pickle as pickle
import threading
from multiprocessing import Queue
from .Process import Process
from .Controller import Controller
from static.classes.datacontroller.IDataManager import IDataConnector
from static.classes.Pipeline.Container import Container
"""

PipelineBuilder

   _________________________________________________Zalożenia____________
  / 1. Pipeline - stworznie Kolejki wykonywanlnej z doczepiąną          |
 |  - don niej jednometodowa logika zbadania i porusznaia sie po niej   |
 |  2. Kontrolla oraz zabiezpiecznia Kontenera procesowego, który jest  |
 |  - zbadany po stronie PipelineBuildera                               |
 |  3. Zapisywania serializowanych objektów do bazy danych              |
 |_____________________________________________________________________/

  ___________________________Start-life______
 /                                           \
|  1. Podciągania procesa z kontenera wg. ID  |
|  2. Deserializacja objekta                  |
|  3. Process.start()                         |
|  4*.Implementacja slownika kolejki          |
|  5*.Stwożenia lambda-buildera funkjalności  |
|     - wedlug parametrów                     | 
| ____________________________________________|
|/                                                    

(Container)              (Contai...)              (Con...)
----------      .......> ----------      .......> ---...
|1.Func. |      :        |1.Func. |      :        |...
|2.Ctrlr.|      :        |2.Ctrlr.|      :        |...
---------- ``````        ---------- ``````        ----...
       ^ 
       |\______________________End-life_________
       |                                       |
       | 1. SQL Clean-up                       |
       | 2. Sprawdzenia dostępnośći przejśćia  |
       | 3. Przejścia                          |
        \______________________________________|


_______________________________________Contaner:_________

1. Process, w śriodeczku którego jest zapakowana Funkcja 
   Podciągana z SQL serializowanego objektu
2. Controller Przejścia 
   Funkcja odpalona zad pomącą subprocesu odczytuje  
   parameter zezwolenia dla każdego przejścia po 
   kolejce
3. Slownik Wagi

"""


class PipeBuilder(IDataConnector):
    """
                PipeBuilder
    """

    __queue = Queue()
    __table = None

    def __init__(self, function, controller: str ):
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
        IDataConnector.__init__(self, DataBase="pipeline")
        # controller - sterownik i glówny architekt przejśćia po obciążeniach procesora
        # funkcja do wykonywania przez procesor
        self.function = function
        self.pathToController = controller
        self.__table = function.__name__
        self._createTable()

    def _createTable(self):
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
        sql = "CREATE TABLE IF NOT EXISTS `%s` (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, obj TEXT NOT NULL)"
        __cursor = self._connector.cursor()
        __cursor.execute(sql, ([self.__table]))
        self._connector.commit()
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
        __cursor = self._connector.cursor()
        __cursor.execute(sql, ([self.__table]))
        self._connector.commit()
        return True

    def addProcess(self, *args):
        """
                    Add Object
        ----------------------------------
        Twożnia objektu typu class process,
        oraz seralizwania go za pomocą mo-
        dula pickle i polecenia dump(obj)
        dopisywania do bazy danych

        @Serhii Riznychuk
        """
        import codecs
        import copyreg
        tempProcessObject = Process(self.function)
        pickle_lock = threading.Lock()
        def serialize_it(not_serialized_object):
            # pickle.dump - serializacja objektu

            pickle_lock.acquire()
            try:
                #stringProcessObject = codecs.encode(pickle.dumps(not_serialized_object), "base64").decode()
                # stringProcessObject = pickle.dumps(tempProcessObject).decode()
                stringProcessObject = pickle.dumps(tempProcessObject).decode()
                # stringProcessObject = copyreg.pickle(Process, not_serialized_object), "base64").decode()
            finally:
                pickle_lock.release()
            return stringProcessObject
        print(serialize_it(tempProcessObject))
        sql = "INSERT INTO `"+self.__table+"`(`object`) VALUES (%s)"
        __cursor = self._connector.cursor()
        __cursor.execute(sql, ([serialize_it(tempProcessObject)]))
        #self._connector.commit()
        __cursor.close()
        del (tempProcessObject)


    def buildQueue(self) -> Queue:
        sql = "SELECT count(*) FROM `{}`".format(self.__table)
        __cursor = self._connector.cursor()
        __cursor.execute(sql, tuple((self.__table)))
        count = __cursor.fetchall()
        for _ in range(count):
            self.__queue.put(Container(self.__table, Controller(self.pathToController)))
        return self.__queue

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
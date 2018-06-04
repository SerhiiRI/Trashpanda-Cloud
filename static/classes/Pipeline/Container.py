from static.classes.datacontroller.IDataManager import IDataConnector
from .AvailableFunctions.FunctionList import functionList
from .Controller import ControllerCPU
from .Threading import ThreadWithReturnValue
import threading
import codecs
import pickle


class Container(threading.Thread, IDataConnector):

    def __init__(self, table, controller: ControllerCPU):
        print("[*] Container building")
        self.table = table
        self.controller = controller
        threading.Thread.__init__(self)
        IDataConnector.__init__(self, DataBase="pipeline")
        self.id, self.function, self.process_argument = self.__getProcess()[0]
        # Dodawania funkcji do kontenera
        # print(self.id, self.function)
        self.__delProcess(self.id)

    def __getProcess(self):
        sql = "SELECT * FROM {} ORDER BY id ASC LIMIT 1".format(self.table)
        __cursor = self._connector.cursor()
        __cursor.execute(sql, ())
        return __cursor.fetchall()

    def __delProcess(self, object_id):
        sql = "DELETE FROM {} WHERE `id`=%s".format(self.table)
        __cursor = self._connector.cursor()
        __cursor.execute(sql, (object_id,))
        self._connector.commit()

    def __addProcess(self, function, process_argumnet):
        """
                    Add Object
        ----------------------------------
        Twożnia objektu typu class process,
        oraz seralizwania go za pomocą mo-
        dula pickle i polecenia dump(obj)
        dopisywania do bazy danych

        @Serhii Riznychuk
        """
        sql = "INSERT INTO {} (`function`, `args`) VALUES (%s, %s)".format(self.table)
        __cursor = self._connector.cursor()
        __cursor.execute(sql, tuple((function, process_argumnet)))
        self._connector.commit()
        __cursor.close()

    def run(self):
        stringArgumnet = self.process_argument.rstrip()
        args = pickle.loads(codecs.decode(stringArgumnet.encode(), "base64"))
        if self.controller.verify():
            print("Critical Server Error")
            self.__addProcess(self.function, self.process_argument)
            return False
        process = ThreadWithReturnValue(target=functionList[self.function], args=args)
        try:
            process.start()
            print(process.join())
            self.__delProcess(object_id=id)
        except Exception:
            self.__addProcess(self.function, self.process_argument)
            raise RuntimeError("[!] Nie udalo ci sie odpalic proces {} o id".format(id), )
        return True

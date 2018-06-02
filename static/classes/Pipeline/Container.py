from static.classes.datacontroller.IDataManager import IDataConnector
from .AvailableFunctions.FunctionList import functionList
from .Controller import Controller
from .Threading import ThreadWithReturnValue
import threading
import codecs
import pickle

#
class Container(threading.Thread, IDataConnector):
    #class Container(IDataConnector):
    # def __init__(self, table, dependProcess="/home/serhii/Projects/llapCloudFlask/static/tool/Binary/cpuController"):

    def __init__(self, table, controller : Controller):
        print("_________________BUILDING CONTAINER__________________")
        self.table = table
        self.controller = controller
        #
        threading.Thread.__init__(self)
        IDataConnector.__init__(self, DataBase="pipeline")
        self.id, self.function, self.process_argument = self.__getProcess()[0]
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
        import codecs
        sql = "INSERT INTO {} (`function`, `args`) VALUES (%s, %s)".format(self.table)
        __cursor = self._connector.cursor()
        __cursor.execute(sql, tuple((function, process_argumnet)))
        self._connector.commit()
        __cursor.close()


    def run(self):

        #print(self.__getProcess())
        stringArgumnet = self.process_argument.rstrip()
        args = pickle.loads(codecs.decode(stringArgumnet.encode(), "base64"))
        # TODO multiselect to lambda
        if self.controller.verify(lambda x: x > 30):
            print("Critical Server Error")
            self.__addProcess(self.function, self.process_argument)
            return False
        process = ThreadWithReturnValue(target=functionList[self.function], args=args)
        try:
            print("Arguments: ", args)
            process.start()
            print(process.join())
            self.__delProcess(object_id=id)
        except Exception:
            self.__addProcess(self.function, self.process_argument)
            print(Exception)
            raise RuntimeError("[!] Nie udalo ci sie odpalic proces {} o id".format(id), )
        finally:
            del(self.controller); del(process)
        return True

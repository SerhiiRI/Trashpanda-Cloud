import threading, MySQLdb, random
import codecs
import pickle
from static.classes.datacontroller.IDataManager import IDataConnector
from static.classes.Pipeline.Process import Process


class Container(threading.Thread, IDataConnector):
    # def __init__(self, table, dependProcess="/home/serhii/Projects/llapCloudFlask/static/tool/Binary/cpuController"):

    def __init__(self, table, controller):
        self.table = table
        self.controller = controller
        threading.Thread.__init__(self)

    def __getProcess(self):
        sql = "SELECT * FROM `%s` ORDER BY id ASC LIMIT 1"
        __cursor = self._connector.cursor()
        __cursor.execute(sql, tuple(self.table))
        return __cursor.fetchall()[1]

    def __delProcess(self, object_id):
        sql = "DELETE FROM `%s` WHERE `id`=%s"
        __cursor = self._connector.cursor()
        __cursor.execute(sql, tuple(self.table, object_id))
        self._connector.commit()


    def run(self):
        id, process_object = self.__getProcess()
        ThreadProcess = pickle.load(process_object)
        # ThreadProcess = pickle.load(codecs.decode(process_object.encode(), "base64"))
        # TODO multiselect to lambda
        if self.controller.verify(lambda x: x < 50):
            return False
        try:
            ThreadProcess.start()
            self.__delProcess(object_id=id)
            del (ThreadProcess)
        except:
            del (ThreadProcess)
            raise RuntimeError("[!] Nie udalo ci sie odpalic proces {} o id".format(id))
        return True
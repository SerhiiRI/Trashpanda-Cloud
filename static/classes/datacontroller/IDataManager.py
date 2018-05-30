import MySQLdb
from static.configs.MainConf import DATABASE
from static.controllers.Permission import Permission
from static.tool.Logs import Log, LogType


class IDataConnector(object):
    """
    Klass twożący sesje do bazy dany
    """
    @Permission.login
    #@Log(LogType.INFO, 107, "Create Connection", printToConsole=True)
    def __init__(self, DataBase="test_cloud"):
        ''' reconstruct SQL requests and create a table '''
        #print(DATABASE[DataBase])
        host = DATABASE[DataBase]["host"]
        user = DATABASE[DataBase]["user"]
        password = DATABASE[DataBase]["password"]
        database = DATABASE[DataBase]["database"]
        self._connector = ""
        try:
            self._connector = MySQLdb.connect(host, user, password, database)
        except (MySQLdb.Error, MySQLdb.Warning) as errorMessage:
            self._connector = None

    @Permission.login
    def _reconfigurate_connection(self, DataBase="test_cloud"):
        ''' reconstruct SQL requests and create a table '''
        host = DATABASE[DataBase]["host"]
        user = DATABASE[DataBase]["user"]
        password = DATABASE[DataBase]["password"]
        database = DATABASE[DataBase]["database"]
        try:
            self._connector = MySQLdb.connect(host, user, password, database)
        except (MySQLdb.Error, MySQLdb.Warning) as errorMessage:
            self._connector = None







# IPermission interface used to implement typical for permission needed
from static.classes.interfaces.IPermission import IPermission
# import module to manipulating on environments variable
import os
# import module to testing MySQL login
from subprocess import Popen, PIPE
# MySQL DataBase
import MySQLdb
from static.configs.DataBaseConfig import DATABASE as db
import getpass


class DataBasePermission(IPermission):

    def test(self, login, password):
        if(os.environ.has_key("TRASHPANDA_USER") and os.environ.has_key("TRASHPANDA_PASSWD") and
                os.environ.has_key("TRASHPANDA_USER") != "" and os.environ.has_key("TRASHPANDA_PASSWD") != ""):
            try:
                print(db['test_cloud'])
                connector =MySQLdb.connect(db["test_cloud"]["host"], login, password, db["test_cloud"]["host"])
            except Exception as m:
                print("You are not logined in the system\n", m)
                return False
        return True

    def rootPermision(self):
        self.rootPermision()

    def login(self):
        if (os.environ.has_key("TRASHPANDA_USER") and os.environ.has_key("TRASHPANDA_PASSWD") and
                os.environ["TRASHPANDA_USER"] != None and os.environ.has_key["TRASHPANDA_PASSWD"] != None):
            self.test()
        print("Please login to (DB)system")
        login = input("Login:")
        print("Password:", end="")
        passwd = getpass.getpass()
        print("THX, bro...")
        if(self.test() == True):

    def logout(self):

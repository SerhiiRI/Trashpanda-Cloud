import getpass
from os import environ as ENV
from static.tool.console.ConsoleTemplate import ConsoleTemplate as templates
from functools import wraps
import MySQLdb

class Permission:

    @staticmethod
    def login(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if(not Permission._test_authorization()):
                return f(*args, **kwargs) if Permission._db_autoriazation() else Permission._error_exit()
            else:
                return f(*args, **kwargs)
        return decorated

    @staticmethod
    def dataBaseAuthentificate(func):
        @wraps(func)
        def with_logging(*args, **kwargs):
            return func(*args, **kwargs) if Permission._db_autoriazation() else Permission._error_exit()
        return with_logging

    @staticmethod
    def _db_autoriazation() -> bool:
        try:
            print("Please login to (DB)system")
            login = input("Login:")
            passwd = getpass.getpass()
        except KeyboardInterrupt:
            return False
        try:
            db = MySQLdb.connect(ENV["TRASHPANDA_HOST"], login, passwd, "mysql")
            ENV["TRASHPANDA_LOGIN"] = login
            ENV["TRASHPANDA_PASSWD"] = passwd
            db.close()
            return True
        except MySQLdb.MySQLError:
            return False
        finally:
            del(login, passwd)

    @staticmethod
    def _error_exit():
        print("\nBye!")

    @staticmethod
    def _test_authorization():
        try:
            db = MySQLdb.connect(ENV["TRASHPANDA_HOST"], ENV["TRASHPANDA_LOGIN"], ENV["TRASHPANDA_PASSWD"], "mysql")
            db.close()
            return True
        except MySQLdb.MySQLError:
            return False



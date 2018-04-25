# IPermission interface used to implement typical for permission needed
from static.classes.interfaces.IPermission import IPermission
# import module to manipulating on environments variable
import os



class DataBasePermission(IPermission):

    def test(self):
        if(os.environ.has_key("TRASHPANDA_USER") and os.environ.has_key("TRASHPANDA_PASSWD") and
                os.environ.has_key("TRASHPANDA_USER") != "" and os.environ.has_key("TRASHPANDA_PASSWD") != ""):

            os.popen("mysql")



    def rootPermision(self):
        self.rootPermision()

    def login(self):
        self.login()


"""
Trashpanda Log-compatible Exception

authors:
@Marcin Ochociński
@Serhii Riznychuk
"""
from static.tool.Logs import ExceptionLog, LogType


class PermissionDenied(Exception):

    @ExceptionLog(LogType.ERROR, 9, "-", printToConsole=True)
    def __str__(self):
        return repr("Bląd uprawnień")


class MySQLConnectorError(PermissionDenied):
    @ExceptionLog(LogType.CRITICAL, 86, "-", printToConsole=True)
    def __str__(self):
        return repr("Bląd podlączenia do Bazy Danych")


class LoginFormError(Exception):
    @ExceptionLog(LogType.ERROR, 101, "-", printToConsole=True)
    def __str__(self):
        return repr("Login Form Error")

# -----------------------------------------------------------------

class DataBaseError(Exception):
    @ExceptionLog(LogType.CRITICAL, 86, "-", printToConsole=True)
    def __str__(self):
        return repr("Bląd Bazy Danych")


class StringCompillingError(Exception):
    @ExceptionLog(LogType.ERROR, 102, "-", printToConsole=True)
    def __str__(self):
        return repr("Bląd interpretacji stringa")


class GetterDataError(DataBaseError):
    @ExceptionLog(LogType.CRITICAL, 61, "-", printToConsole=True)
    def __str__(self):
        return repr("Bląd wyciągania danych")

# -----------------------------------------------------------------


class EnvironmentalException(Exception):
    def __init__(self, variable=None):
        self.variable = variable

    @ExceptionLog(LogType.ERROR, 99, "-", printToConsole=True)
    def __str__(self):
        string = "Bląd zmięnnych śriodowiskowych" \
                 + "" if (self.variable == None) else " ENV-var : "+self.variable
        return repr(string)

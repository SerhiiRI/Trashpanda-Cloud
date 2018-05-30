from static.tool.Logs import Log, LogType


class PermissionDenied(Exception):
    @Log(LogType.CRITICAL, 1, "-", printToConsole=False)
    def __int__(self):
        pass
    def __str__(self):
        return repr("Can`t get access to event")

class Spok(Exception):
    def __str__(self):
        return repr("bląd... synu z nieprawego loża")

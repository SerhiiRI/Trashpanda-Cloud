class ZjebaloException(Exception):
    def __str__(self):
        return repr("Zjebalesz spok....zjebaleś kurwa!")

class Spok(Exception):
    def __str__(self):
        return repr("bląd... synu z nieprawego loża")

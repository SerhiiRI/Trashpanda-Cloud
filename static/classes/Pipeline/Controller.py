from static.tool.FileManager import FileManager
class Controller(object):

    def __init__(self, path, *keys ):
        self.__PathToSystemCommand = 0
        self.keys  = [str(x) for x in keys]

    @property
    def PathToSystemCommand(self):
        return self.__PathToSystemCommand

    @PathToSystemCommand.setter
    def PathToSystemCommand(self, path):
        """
            PathToSystemCommand
    -----------------------------------------
    zbierania danych o pliku i podciąga
    META-informacje dla interpretacji w
    system dla liczenia przez PipeBuilder-a

    @Serhii Riznychuk
        """

        if(FileManager.testExistFile(path)):
            self.__PathToSystemCommand = path



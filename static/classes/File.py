# Class file
import interfaces.IFile

class File(IFile):

    def __init__(self):
        fileID=""
        Name=""
        Extension=""
        filePath=""
        HashSum=""

    def __constructFromDB(self, fileID : str):
        self.fileID = fileID;
        pass


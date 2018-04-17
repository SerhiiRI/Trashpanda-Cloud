# Class file
import static.classes.interfaces.IFile as IFile

class File(IFile.File):

    def __init__(self, data: list):
        self.fileID=""
        self.Name=""
        self.Extension=""
        self.FilePath=""
        self.Size=""
        self.HashSum=""
        self.construct(data)

    def construct(self, data: list):
        self.fileID = data[0]
        self.Name = data[1]
        self.Extension = data[2]
        self.FilePath = data[3]
        self.Size = data[4]
        self.HashSum = data[5]


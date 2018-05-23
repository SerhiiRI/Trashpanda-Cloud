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
        self.Icon=""
        self.construct(data)
        print(self.serialize())

    def construct(self, data: list):
        self.fileID = str(data[0])
        self.Name = str(data[1])
        self.Extension = data[2]
        self.FilePath = str(data[3])
        self.Size = str(data[4])
        self.HashSum = str(data[5])
        if(self.Extension is None):
            self.Icon = "folder-open-empty"
        else:
            self.Icon = "file-image"

    def serialize(self) -> str:
        """Serialized format ID:Name:Extension:FilePath:Size:HashSum"""
        return self.fileID+':'+self.Name+':'+str(self.Extension)+':'+self.FilePath+':'+self.Size+':'+self.HashSum+':'+self.Icon


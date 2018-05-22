import datetime
import hashlib
import os

from static.tool.FileManager import FileManager
from static.classes.datacontroller.SQLController import SQLCloud

class Uploaded_File():
    def __init__(self):
        self.ID_file = ""
        self.ID_File = ""
        self.Version = "1.0"
        self.Name = ""
        self.HashSum = ""
        self.Size = ""
        self.extension = ""
        self.path = ""
        self.accessType = "1"
        self.garbage = "0"
        self.timeCreate = str(datetime.datetime.today())
        self.lastAccess = str(datetime.datetime.today())
        self.OwnerID = ""

    def getInfo(self, file_dir : str, destination_DIR : str, google_ID : str):
        self.HashSum = FileUpload.countHashSum(file_dir)
        self.Size = os.stat(file_dir).st_size
        self.extension = FileManager.extensionSpliter(file_dir)
        self.Name = os.path.basename(file_dir)
        self.path = destination_DIR + self.HashSum + self.extension
        self.OwnerID = google_ID

    def uploadTheShit(self):
        DB = SQLCloud()

        SQL_Insert = DB.insert("file")
        SQL_Select = DB.select("file")

        SQL_Insert(self.OwnerID, self.Name)
        file_data = SQL_Select(self.OwnerID)





class FileUpload():

    @staticmethod
    def upload(filelist, path):
        DUMP_DIR = "/srv/DUMP/"
        Destination_DIR = "/srv/Data/" + path
        """Lista mówiąca ile plików udało się pobrać bez problemów"""
        statusList = list()

        for REQUESTED_FILE in filelist:
            try:
                """Magia Uploadu pliku, Cała logika znajduje się tutaj"""
                filename = REQUESTED_FILE.filename
                DUMP_destination = DUMP_DIR + filename

                """Grand Finale - Zapis Pliku na dysku"""

                REQUESTED_FILE.save(DUMP_destination)
                SHA1 = FileUpload.countHashSum(DUMP_destination)

                if not FileManager.moveFile(DUMP_destination, Destination_DIR, SHA1):
                    FileManager.remove(DUMP_destination)
                    statusList.append([False, filename, DUMP_destination, str(datetime.datetime.today())])
                else:
                    statusList.append([True, filename, DUMP_destination, str(datetime.datetime.today())])

            except:
                print("Error, Error blyat")

        return statusList


    @staticmethod
    def countHashSum(destination : str):

        """Variables"""
        BUF_SIZE = 65536
        sha1 = hashlib.sha1()

        with open(destination, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha1.update(data)

        return sha1.hexdigest()

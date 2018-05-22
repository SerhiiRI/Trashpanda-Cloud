import datetime
import hashlib
from static.tool.FileManager import FileManager

class FileUpload():

    @staticmethod
    def upload(filelist):
        DUMP_DIR = "/srv/DUMP/"
        """Lista mówiąca ile plików udało się pobrać bez problemów"""
        statusList = list()

        for REQUESTED_FILE in filelist:
            try:
                """Magia Uploadu pliku, Cała logika znajduje się tutaj"""
                filename = REQUESTED_FILE.filename
                destination = DUMP_DIR + filename

                """Grand Finale - Zapis Pliku na dysku"""

                REQUESTED_FILE.save(destination)
                SHA1 = FileUpload.countHashSum(destination)

                if not FileManager.moveFile(destination, DUMP_DIR, SHA1):
                    FileManager.remove(destination)
                    statusList.append([False, filename, destination, str(datetime.datetime.today())])
                else:
                    statusList.append([True, filename, destination, str(datetime.datetime.today())])

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

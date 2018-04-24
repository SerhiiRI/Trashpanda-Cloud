# Tu musi być klasa lub do chuja dużo procedur
# z możliwościa wykorzystywania ich dla szybkiego
# tworznia katalogów, linków na objekt, kopijowania,
# wycinania, sprawdzenia, testowania plików w
# drzewie systemu plikowego
# Do każdej metody musi byc stworzony Log.

import os
import shutil

class FileManager(object):

    @staticmethod
    def createFolder(path: str):
        try:
            '''Sprawdzanie istnienia ścieżki'''
            if not os.path.exists(path):
                os.makedirs(path)
                print("Directory Successfully Created")
            else:
                print("Directory Already Exists")

        except:
            print("Błąd createFolder")
            return False

        return True

    @staticmethod
    def moveFile(pathA: str, pathB: str, md5: str):
        '''Rozbicie pathA na scieżkę pliku oraz rozszerzenie'''

        if not os.path.isfile(pathA):
            print("Brak pliku o takiej ścieżce")
            return False

        fileName , fileExtension = os.path.splitext(pathA)
        '''Sprawdzenie czy plik posiada rozszerzenie, polityka chmury: brak rozszerzenia - JEB SIE'''

        if fileExtension == "":
            print("Requested file lacks file extension, you ain't fuckin' with trashpanda's policy NIGGAAAAAA")
            return False
        else:
            pathB = pathB + md5 + fileExtension
            os.rename(pathA, pathB)

        return True

    @staticmethod
    def remove(path: str):
        try:
            if path[len(path) - 1] != "/":
                return FileManager.removeFile(path)
            else:
                return FileManager.RemoveDir(path)
        except:
            print("Remove function fatal error")
            return False

    @staticmethod
    def removeFile(path: str) -> bool:
        try:
            os.remove(path)
        except:
            print("There is no requested file to remove")
            return False

        return True

    @staticmethod
    def removeDir(path: str) -> bool:
        try:
            shutil.rmtree(path)
        except:
            print("There is no requested directory to remove")
            return False

        return True

    @staticmethod
    def _checkHealth(filePath: str):

        name = filePath
        print("... Procesing " + os.getcwd() + "/" + name + "...")
        stat = os.stat(name)
        if (not stat[4] and not stat[5] and not stat[6] and not stat[7] and not stat[8]):
            return 0
        else:
            try:
                c_file = open(name, "rb")
                lenght = stat.st_size
                for c_size in range(lenght):
                    c_byte = c_file.read(1)
                    if (len(c_byte) != 1 and c_byte == "" and c_size == lenght):
                        return 1
                    if (len(c_byte) != 1 and c_size != lenght):
                        return 0
            except IOError as error:
                return False
        return True

    @staticmethod
    def createLink(pathA: str, pathB: str):

        '''Sprawdzenie czy plik o podanej ścieżce istnieje'''
        if not os.path.isfile(pathA):
            print("Brak pliku o takiej ścieżce")
            return False

        '''Wyciągnięcie pełnej nazwy wraz z rozszerzeniem z pliku pierwotnego'''
        filename = os.path.basename(pathA)

        '''Sprawdzenie czy podana ścieżka jest prawidłowa'''
        if not os.path.isdir(pathB):
            print("Ścieżka jest niewłaściwa lub nie istnieje")
            return False

        '''Próba utworzenia symlink'u'''
        try:
            os.symlink(pathA, pathB + filename)
        except:
            print("Symlink Error, check whether symlink with such name does not already exist in requested directory")
            return False

        return True

    @staticmethod
    def swapOwner(pathA: str, pathB: str):
        pass

    @staticmethod
    def testExistFile(path):
        '''
                testExistFile

        :param path: path to testing file on existing in the file system
        :return: True/False
        Testing file on existing

        @Serhii Riznychuk
        '''
        return os.path.isfile(path)

    @staticmethod
    def getMeta(path):
        """
                  GetMeta

        Otrzymania metainformacji dla plików
        i zwócenia jako <class tuple>
        return: ( Name, Size, LastAccess )

        @Serhii Riznychuk
        """

        Size = os.stat(Route)

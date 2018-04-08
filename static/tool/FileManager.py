# Tu musi być klasa lub do chuja dużo procedur
# z możliwościa wykorzystywania ich dla szybkiego
# tworznia katalogów, linków na objekt, kopijowania,
# wycinania, sprawdzenia, testowania plików w
# drzewie systemu plikowego
# Do każdej metody musi byc stworzony Log.

import os

class FileManager(object):

    def __init__(self):
        pass

    def createFolder(self, path: str):
        try:
            '''Sprawdzanie istnienia ścieżki'''
            if not os.path.exists(path):
                os.makedirs(path)
                print("Directory Successfully Created")
            else:
                print("Directory Already Exists")

        except(NameError):
            print(NameError)
            return False

        return True

    def moveFile(self, pathA:str, pathB:str, md5:str):
        '''Rozbicie pathA na scieżkę pliku oraz rozszerzenie'''
        fileName , fileExtension = os.path.splitext(pathA)
        '''Sprawdzenie czy plik posiada rozszerzenie, polityka chmury: brak rozszerzenia - JEB SIE'''

        if fileExtension is None :
            print("Lacking File Extension")
            return False
        else:
            pathB = pathB + md5 + fileExtension



    def Remove(self):
        pass

    def CheckHealth(self):
        pass

    def CreateLink(self):
        pass

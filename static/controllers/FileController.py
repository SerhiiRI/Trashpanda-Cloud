"""
Klasa tworząca listę plików i katalogów znajdujących się w aktualnie wybranej przez klienta lokalizacji
Kierunek Działąń:

1.gatherHashes(path) - Funkcja skanująca wybraną przez klienta przestrzeń dyskową, tworzy i zwraca listę
Hashy oraz katalogów.

2.gatherInfo(Hash) - Funkcja wywołująca zapytanie do bazy danych dla pojedynczego pliku, oczekuje zwrotu listy,
zawierającej pełne informacje o pliku. Zwraca instancje klas File oraz FileInfo.

3.creteLists() - Funkcja przygotowująca listy obiektów klas File oraz FileInfo. Wewnątrz funkcji zawiera się
pętla *foreach* pozwalająca na wykonanie metody *gatherInfo* dla każdego z Hashy uzyskanych metodą *gatherHashes*.
Jeśli Hash będzie za krótki, bądź plik nie będzie posiadał rozszerzenia zostanie uznany za katalog i
zostanie pominięty dla funkcji *gatherInfo*
"""

import glob, os, shutil
import static.classes.File as File
from static.classes.datacontroller.SQLController import SQLCloud


class FileController(object):
    def __init__(self):
        self.defaultRoute = "/srv/Data"
        self.SQL_Controller = SQLCloud()

    """Ścieżka *Path* powinna być w formacie [ /userID/katalog1/katalog2/ ], czyli slash na początku i końcu"""
    def gatherDiskInfo(self, Path = "") -> list:
        Route = self.defaultRoute + Path
        temp = glob.glob(Route+"*")
        Files = list()

        for file in temp:
            Size = os.stat(file).st_size
            FullPath = file

            hash = file.split("/")[-1]
            print('szukamy')
            try:
                Data_Reader = self.SQL_Controller.merge("file", "idFile", "version", where={"hashsume" : hash.split(".")[0]})

                Name = Data_Reader[0][2]
                print("imie " + Name)
                fileID = Data_Reader[0][0]
                Extension = self.extensionSpliter(file)
            except Exception as ex:
                print(ex)
                Name = file.split("/")[-1]
                fileID = "Folder"
                Extension = "None"
                FullPath = FullPath + '/'


            """Wypełnianie Listy informacjami dla konstruktora klasy File"""
            TEMP = list()
            TEMP.append(fileID)
            TEMP.append(Name)
            TEMP.append(Extension)
            TEMP.append(FullPath)
            TEMP.append(Size)
            TEMP.append(hash)
            """Dodawanie do listy plików obiektów klasy File"""
            Files.append(File.File(TEMP))

        return Files

    def extensionSpliter(self, filename : str):
        ext = ""
        tab = filename.split(".")

        if len(tab) > 2:
            if len(tab[-2]) > 2:
                ext = "." + tab[-2] + "." + tab[-1]
            else:
                ext = "." + tab[-1]
        elif len(tab) == 2:
            ext = "." + tab[-1]
        else:
            ext = None
        return ext

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

import glob
import os
import shutil
import static.classes.File as File

class FileController(object):
    def __init__(self):
        pass

    def gatherHashes(self, client_ID: str) -> list:
        pass

    def gatherItemInfo(self, hashsum: str):
        pass

    def createLists(self, hashes: list) -> list:
        pass


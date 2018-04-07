#
# _________________________________________________________
# |This Interfejs used to create ORM table data controlelr|
# ---------------------------------------------------------
#        \   ^__^
#         \  (oo)\_______
#            (__)\       )\/\
#                ||----w |
#                ||     ||
# class IOrm przyznaczony dla tworzenia na jego
# podstawie klasy dla sterowania MySQL bazą danych.
# Np tabelie [Tag, Tags, Words] jest pobierane
# do klasy "LinkController(IOrm)", pochodnej
# od interfejsu IOrm dla diagnostyki, statystyk
# oraz jakiejkolwiek implementacji bizness logiki.
# Zbior danych otrzymany od SQL żądania w żadnen
# sposub nie musi być otwarty, wszystkie dane
# muszą być wypisane za pomącą metod funkcyjnym paradygmatem.
# Np Map, fileter, z przykazanymi metodami zęwnętrznej
# logiki... np:
# zbior_danych = map( fucja sortująća lub (lambda x: x> 0)), zbiorSQLDanych )
# no i tak dalej.



import MySQLdb

class IOrm(object):

    def __init__(self, sql_question):
        ''' reconstruct SQL requests and create a table '''
        try:
            __construct(sql_question)
        except (MySQLdb.Error, MySQLdb.Warning) as errorMessage:
            print(errorMessage)

    def __construct(sql="" : str):
        raise NotImplementedError(" [*] konstruktor interfejsu IOrm nie jest zaimplementowany w pochodenj klasie "+self.__name)

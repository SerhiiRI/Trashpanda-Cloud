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
from static.configs.MainConf import DATABASE
from static.controllers.Permission import Permission


class IDataConnector(object):

    @Permission.login
    def __init__(self, DataBase="test_cloud"):
        ''' reconstruct SQL requests and create a table '''
        #print(DATABASE[DataBase])
        host = DATABASE[DataBase]["host"]
        user = DATABASE[DataBase]["user"]
        password = DATABASE[DataBase]["password"]
        database = DATABASE[DataBase]["database"]
        self._connector = ""
        try:
            self._connector = MySQLdb.connect(host, user, password, database)
        except (MySQLdb.Error, MySQLdb.Warning) as errorMessage:
            self._connector = None

    @Permission.login
    def _reconfigurate_connection(self, DataBase="test_cloud"):
        ''' reconstruct SQL requests and create a table '''
        host = DATABASE[DataBase]["host"]
        user = DATABASE[DataBase]["user"]
        password = DATABASE[DataBase]["password"]
        database = DATABASE[DataBase]["database"]
        try:
            self._connector = MySQLdb.connect(host, user, password, database)
        except (MySQLdb.Error, MySQLdb.Warning) as errorMessage:
            self._connector = None







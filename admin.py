#!/usr/bin/python3
import argparse
import os
from os import environ as ENV

ENV['TRASHPANDA_HOST'] = "trashpanda.pwsz.nysa.pl"
ENV['CLOUD_MAX_FILE_SIZE'] = '1MB'
ENV['CLOUD_PROJECT_PATH'] = os.getcwd()
ENV['CLOUD_TRASHBOX'] = '/srv/Data/'
ENV['TRASHPANDA_LOGIN'] = ENV['TRASHPANDA_LOGIN'] if 'TRASHPANDA_LOGIN' in ENV else "sergiy1998"
ENV['TRASHPANDA_PASSWD'] = ENV['TRASHPANDA_PASSWD'] if 'TRASHPANDA_PASSWD' in ENV else "hspybxeR98>"

from static.controllers.AdminControllers import user, file, system


"""
NAME 
        admin - program to manage administration cloud-layout

SYNOPSIS
        admin [-dafs]

DESCRIPTION 
        
        Program systemowego admnistrowania dla chmury trashpandy, jest odrębnei napisanym programem, dla sterowania klientami, dostepem, oraz wykonywania usuwania, dodawania, wprowadzania zmian w danych chmóry "Trashpanda". Jest integrowany i wykorzystywany w śilniku wyszukiwarki Trashpanda.

COMMAND-LINE OPTIONS

        user - module for control users
        file - module for file control
        stat - wypisywania ogólnej statystyki servera
        Mandatory arguments to long options are mandatroy for short options too.

        -u --user
        -f --file
        -s --statistic
                
"""


def admin():
    '''
    :name Admin.py
    Admin.py - jest plik zażądzający
    dla listy plików oraz użytkowników
    glównym calem którego jest podmia-
    na typowego (web-go.) trybu stero-
    wania.
    :return view of tool program

    @Serhii Rinzychuk
    '''
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="Type of change", description="valid subcommand", help='descriptor')
    user_parser = subparsers.add_parser('user', help="Tool for managing list of users")
    user_parser.add_argument('email', action="store", help="user google-mail adress")
    user_parser.add_argument('-b', '--ban', action="store", dest="ban", type=int, default=0, help="add user to ban-list")
    user_parser.add_argument('-s', '--stat', action= "store_true", dest="stat", default=False, help="write user statistic")
    user_parser.add_argument('-l', '--links', action="store_true", dest="links", default=False, help="get list of open links")
    user_parser.add_argument('-d', '--delete', action="store_true", dest="to_delete", default=False, help="delete current user")
    user_parser.add_argument('-R', '--add-to-root', action="store_true", dest="to_root", default=False, help="add root permission for selected user")
    user_parser.add_argument('-N', '--delete-from-root', action="store_true", dest="no_root", default=False, help="cencel root permission for selected user")
    user_parser.set_defaults(func=user.do)

    file_parser = subparsers.add_parser('file', help='file manager command')
    file_parser.add_argument('filename', action="store", help="get file name")
    file_parser.add_argument('-v', '--versions', action="store", dest="version", default=False, help="managering only version of file")
    file_parser.add_argument('-u', '--users', action="store_true", dest="users", default=False, help="write only users statisctic to file")
    file_parser.add_argument('-d', '--delete', action="store_true", dest="to_delete", default=False, help="remove file(or version with key -v )")
    file_parser.add_argument('-l', '--lock-link', action="store_true", dest="to_lock", default=False, help="close link to file(or version with key -v)")
    file_parser.add_argument('-s', '--stat', action="store_true", dest="stat", default=False, help="statistic to file")
    file_parser.set_defaults(func=file.do)

    """
    stat_parser = subparsers.add_parser('stat', help='Trashpanda-server statisctics')
    stat_parser.add_argument('-u', '--users', action="store_true", dest="users", default=False, help="main users statistics")
    stat_parser.add_argument('-f', '--files', action="store_true", dest="files", default=False, help="storeged file statistics")
    stat_parser.add_argument('-s', '--servers', action="store_true", dest="servers", default=False, help="active server information")
    stat_parser.add_argument('-l', '--logs', action="store_true", dest="logs", default=False, help="writing last log")
    stat_parser.set_defaults(func=system.do)
    """

    if __name__ == '__main__':
        args = parser.parse_args()
        if not vars(args):
            parser.print_usage()
        else:
            return args.func(args)

admin()

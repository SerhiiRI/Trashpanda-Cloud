from flask import Blueprint, request, jsonify, session
from static.controllers.admin import adminScript, testUser
from static.tool.FileManager import FileManager
from static.blueprints.pathFix import pathFixer

searchEngine = Blueprint('searchEngine', __name__, template_folder='templates')


@searchEngine.route('/search')
def renderRootLogin():
    login = request.args.get('login')
    haslo = request.args.get('haslo')
    if(testUser(login, haslo=haslo)):
        print("jeseś adminem")
    else:
        print("nie jestes adminem")


@searchEngine.route('/admin')
def renderRootScript():
    comand = request.args.get('command')
    return adminScript(comand)

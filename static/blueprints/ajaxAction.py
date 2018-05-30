from flask import Blueprint, request, jsonify, session
from static.tool.FileManager import FileManager

ajaxAction = Blueprint('ajaxAction', __name__, template_folder='templates')

def pathFixer(path, gid):
    print('PathFixer: {0} {1}'.format(path, gid))
    paths = path.split('/')
    try:
        paths.remove('')
        print("Remove: {}".format(path))
    except:
        print('ajaxAction: paths.remove() - Nie znaleziono pustych znakow.')
    try:
        paths.remove('home')
        print("Remove home: {}".format(path))
    except:
        print('ajaxAction: paths.remove(home) - Nie znaleziono klucza home.')
    try:
        paths.pop()
        print("Pop: {}".format(path))
    except:
        print('ajaxAction: paths.pop() - Lista jest pusta.')
    print("Fix list: {0}".format(paths))
    finalPath = '/' + gid + '/'
    for path in paths:
        finalPath += path + '/'
    return finalPath

@ajaxAction.route('/ajax_action', methods=['POST'])
def sessionControler():
    if request.form.get('action') == 'add-dir':
        print('Run add dir.')
        newDir = [request.form.get('name'), request.form.get('currentdir')]
        newDir[1] = pathFixer(newDir[1], session.get('googleID'))
        create = '/srv/Data' + newDir[1] + newDir[0] + '/'
        print('Create: {}'.format(create))
        try:
            result = FileManager.createFolder(str(create))
        except:
            result = 'Błąd katalogów'
        print('Create path: {0} ___ Result: {1}'.format(create, result))
        return jsonify({'name': newDir[0]})

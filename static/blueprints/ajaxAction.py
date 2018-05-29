from flask import Blueprint, request, jsonify, session
from static.tool.FileManager import FileManager

ajaxAction = Blueprint('ajaxAction', __name__, template_folder='templates')

def pathFixer(path):
    splitPath = path.split('/')
    if splitPath[0] == 'home':
        splitPath[0] = session.get('googleID')
        path = '/'
        for part in splitPath:
            path = path + part + '/'
        return path

@ajaxAction.route('/ajax_action', methods=['POST'])
def sessionControler():
    if request.form.get('action') == 'add-dir':
        newDir = [request.form.get('name'), request.form.get('currentdir')]
        newDir[1] = pathFixer(newDir[1])
        create = '/srv/Data' + newDir[1] + newDir[0] + '/'
        result = FileManager.createFolder(create)
        print('Create path: {0} ___ Result: {1}'.format(create, result))
        return jsonify({'name': newDir[0]})

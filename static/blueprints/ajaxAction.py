from flask import Blueprint, request, jsonify, session
from static.tool.FileManager import FileManager
from static.blueprints.pathFix import pathFixer

ajaxAction = Blueprint('ajaxAction', __name__, template_folder='templates')


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

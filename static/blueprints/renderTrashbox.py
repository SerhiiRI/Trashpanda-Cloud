from flask import Blueprint, session, render_template

from static.controllers.FileController import FileController

renderTrashbox = Blueprint('renderTrashbox', __name__, template_folder='templates')


@renderTrashbox.route('/mytrashbox', defaults={'pathToDir': 'home'})
@renderTrashbox.route('/mytrashbox/<pathToDir>')
def mytrashbox(pathToDir):
    '''
    :param pathToDir:
    :return: na podstawie ścieżki zwraca widok
    '''
    init = {'include': 'trashbox'}
    paths = pathToDir
    if paths == 'home':
        backpath = ''
        currentdir = 'home'
        finalPath = ''
    else:
        paths = paths.split('.')
        finalPath = ''
        currentdir = paths[-1]
        if len(paths) > 1:
            backpath = paths[-2]
        else:
            backpath = paths[0]
        for path in paths:
            finalPath = finalPath + '/' + path
    if 'googleID' in session:
        finalPath = '/' + session['googleID'] + finalPath + '/'
    else:
        return render_template('index.html')

    filecontroller = FileController()
    files = filecontroller.gatherDiskInfo(finalPath)
    # Dane testowe
    print(files)
    print("Files: " + str(len(files)))
    print("Get pathToDir: " + pathToDir)
    print("Set currentDir: " + currentdir)
    print("Set backPath: " + backpath)
    print("Set finalPath: " + finalPath)
    return render_template('trashbox_base.html', backpath=backpath, currentdir=currentdir, init=init)

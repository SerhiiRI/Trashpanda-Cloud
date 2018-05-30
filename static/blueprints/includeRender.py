from flask import Blueprint, session, render_template, redirect, request

from static.blueprints.testFile import getTestFiles
from static.blueprints.testFile import getEmptyFiles
from static.classes.FileUpload import FileUpload
from static.controllers.FileController import FileController

includeRender = Blueprint('includeRender', __name__, template_folder='templates')


@includeRender.route('/include/include_trashbox', methods=['GET', 'POST'])
def renderMyTrashbox():
    '''
    :return: my Trashbox with ajax
    '''
    print('Including.')
    if 'googleID' in session:
        gid = session['googleID']
        if gid:
            print('Pobranie szablonu my trashbox.')

            if request.method == 'GET':
                backpath = ''
                currentdir = 'home'
                finalPath = '/' + session['googleID'] + '/'

            elif request.method == 'POST':
                origin = request.form.get('attr1')
                paths = origin
                print('New path: {}'.format(origin))

                if paths == '':
                    return "<script>goTo('/');</script>"
                if paths == 'home' or paths == '/home/' or paths == '/srv/Data/home/' or paths == '/srv/Data/' + session['googleID'] + '/':
                    paths = '/' + session['googleID'] + '/'

                paths = paths.split('/')
                try:
                    paths.remove('')
                except:
                    print('I_Trashbox: Nie zaleziono pustych znakow.')
                try:
                    paths.pop()
                except:
                    print('I_Trashbox: paths.pop() - Tablica jest pusta.')

                finalPath = ''
                currentdir = ''
                backpath = ''

                x=0
                for path in paths:
                    if path != 'srv' and path != 'Data':
                        finalPath = finalPath + '/' + path
                        if path == session['googleID']:
                            currentdir += '/home/'
                        else:
                            currentdir += path + '/'
                finalPath += '/'

                if len(paths) > 1:
                    if currentdir == session.get('googleID'):
                        backpath = ''
                    else:
                        bpaths = paths
                        try:
                            bpaths.pop()
                        except:
                            print('I_Trashbox: bpaths.pop() - Tablica jest pusta.')
                        for path in bpaths:
                            backpath = backpath + '/' + path
                        backpath += '/'
                else:
                    currentdir = 'home'
                    backpath = ''
                print('Original: {} || Final: {} || Current: {} || Back: {}'.format(origin, finalPath, currentdir,
                                                                                    backpath))

            try:
                filecontroller = FileController()
                files = filecontroller.gatherDiskInfo(finalPath)
            except:
                files = getEmptyFiles()
            return render_template('include/include_trashbox.html', files=files, backpath=backpath,
                                   currentdir=currentdir)
        else:
            return redirect('/')

    print('My Trashbox: Access denied')
    return redirect('/')


@includeRender.route('/include/include_upload', methods=['POST'])
def upload_file():
    print('Include upload.')
    currentdir = request.form.get('attr1')
    print("py currentdir: " + currentdir)
    return render_template('include/include_upload.html', currentdir=currentdir)


def pathFixer(path, gid):
    print('PathFixer: {0} {1}'.format(path, gid))
    paths = path.split('/')
    try:
        paths.remove('')
    except:
        print('Nie znaleziono pustych znakow.')
    try:
        paths.remove('home')
    except:
        print('Nie znaleziono klucza home.')
    try:
        paths.pop()
    except:
        print('I_Trashbox: paths.pop() - Tablica jest pusta.')
    print("Fix list: {0}".format(paths))
    finalPath = '/' + gid + '/'
    for path in paths:
        finalPath += path + '/'
    return finalPath

@includeRender.route('/upload_file_to_db', methods=['POST'])
def upload():
    path = request.form.get('currentdir')
    print('Orginal path: {}'.format(path))
    if path[0] != '/':
        path = '/' + path
    if path[-1] != '/':
        path = path + '/'
    path = pathFixer(path, session.get('googleID'))
    print('Upload path: {0}'.format(path))
    if 'file_to_upload' in request.files:
        file = request.files['file_to_upload']
        print("File: " + str(file.filename).encode('utf-8'))
    else:
        print("Ni ma ; - ;")
    desc = request.form.get('description')
    tab = FileUpload.upload(file, path, session.get('googleID'), desc)

    for item in tab:
        print(item)

    return redirect('/mytrashbox')

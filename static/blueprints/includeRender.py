from flask import Blueprint, session, render_template, redirect, request

from static.blueprints.pathFix import pathFixer
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
                if paths == 'home' or paths == '/srv/Data/home/' or paths == '/srv/Data/' + session['googleID'] + '/':
                    paths = '/' + session['googleID'] + '/'

                paths = paths.split('/')
                paths.remove('')
                paths.pop()

                finalPath = ''
                backpath = ''

                x=0
                for path in paths:
                    if path != 'srv' and path != 'Data':
                        finalPath = finalPath + '/' + path
                finalPath += '/'

                if len(paths) > 1:
                    currentdir = paths[-1]
                    if currentdir == session.get('googleID'):
                        currentdir = 'home'
                        backpath = ''
                    else:
                        bpaths = paths
                        bpaths.pop()
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
        print("File: " + file.filename)
    else:
        print("Ni ma ; - ;")
    desc = request.form.get('description')
    tab = FileUpload.upload(file, path, session.get('googleID'), desc)

    for item in tab:
        print(item)

    return redirect('/mytrashbox')

from flask import Blueprint, session, render_template, redirect, request
from static.blueprints.testFile import getTestFiles
from static.blueprints.testFile import getEmptyFiles
from static.controllers.FileController import FileController

includeRender = Blueprint('includeRender', __name__, template_folder='templates')


@includeRender.route('/include/include_trashbox', defaults={'pathToDir': 'home'})
@includeRender.route('/include/include_trashbox/<pathToDir>')
def renderMyTrashbox(pathToDir):
    '''
    :return: my Trashbox with ajax
    '''
    print('Including.')
    if 'googleID' in session:
        gid = session['googleID']
        if gid:
            print('Pobranie szablonu my trashbox.')
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
                return redirect('/')

            try:
                filecontroller = FileController()
                files = filecontroller.gatherDiskInfo(finalPath)
            except:
                files = getEmptyFiles()
            print("Files: _" + str(len(
                files)) + "_ Get pathToDir: _" + pathToDir + "_ Set currentDir: _" + currentdir + "_ Set backPath: _" + backpath + "_Set finalPath: _" + finalPath + '_')
            return render_template('include/include_trashbox.html', files=files, backpath=backpath,
                                   currentdir=currentdir)

    print('My Trashbox: Access denied')
    return redirect('/')


@includeRender.route('/include/include_upload', methods=['POST'])
def upload_file():
    print('Include upload.')
    currentdir = request.form.get('attr1')
    print("py currentdir: " + currentdir)
    return render_template('include/include_upload.html', currentdir=currentdir)

@includeRender.route('/include/include_googleID')
def include_googleID():
    print('Include google sign in.')
    return render_template('include/include_googleID.html')


@includeRender.route('/include/include_index')
def include_index():
    print('Include index.')
    return render_template('include/include_index.html')

import logging
import os
import sys
import static.configs.EnvConf
import tempfile
from time import sleep

from static.controllers.Permission import Permission
from static.tool.Logs import Log, LogType
from static.tool.FileManager import FileManager
from static.controllers.FileController import FileController
from static.classes.Registration import Register, isRegistered

from static.classes.FileUpload import FileUpload

from flask import Flask, render_template, send_file
from flask import request, session, jsonify


app = Flask(__name__)
app.secret_key = os.urandom(24)


def getTestPathData():
    paths = [{
        'icon': 'file-image',
        'name': 'twoja_stara.png',
        'lock': 'lock',
        'size': '2.4 MB',
        'tag': ['#hehe', '#lol', '#yolololololo', '#hehe', '#lol', '#yololo'],
    },
        {
            'icon': 'folder-open-empty',
            'name': 'twoja_stara.png',
            'lock': '',
            'size': '',
            'tag': [],
        }
    ]
    return paths

@app.route('/')
def index():
    return render_template('index.html')


'''
    Dodanie/Update/Odczyt sesji
    
    :param name
    :param value
    :return value

'''
@app.route('/sessionControler', methods=['POST'])
def sessionControler():
    print("Wywołano session flask.")
    if request.form.get('action') == 'set':
        name = request.form.get('name')
        param = request.form.get('param')
        session[name] = param
        print("Dodano sesję o nazwie: " + name + " = " + param)
        return jsonify({'param': param})

    if request.form.get('action') == 'get':
        name = request.form.get('name')
        if session[name]:
            param = session[name]
            print("Pobrano sesję o nazwie: " + name)
            return jsonify({'param': param})
        elif session[name]:
            sleep(0.5)
            param = session[name]
            print("Pobrano sesję o nazwie: " + name)
            return jsonify({'param': param})
        else:
            print("Nie znaleziono sesji: " + name)
            return jsonify({'param': ''})


@app.route('/info')
def info():
    return render_template('info_pages/info.html')


@app.route('/about')
def about():
    return render_template('info_pages/about.html')
    # return redirect("https://www.asciipr0n.com/pr0n/morepr0n/pr0n03.txt", code=302)
    # hackerman... jo-jo-jo


@app.route('/contact')
def kontakt():
    return render_template('info_pages/contact.html')


@app.route('/download')
def download():
    #path = request.form.get('filePath')
    path = "/srv/Data/mikus/plik.txt"
    name = os.path.basename(path)
    return send_file(path, attachment_filename=name , as_attachment=True)


# @app.route('/mytrashbox', methods=['GET','POST'])
# def mytrashbox():
#     try:
#         path = "/" + request.form.get('google_id') + "/"
#     except:
#         path = "/"
#     files = FileManager.listDir(path)
#     return render_template('trashbox_test.html', items=files, path=path)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('info_pages/404.html'), 404
    # return redirect("https://www.asciipr0n.com/pr0n/morepr0n/pr0n04.txt", code=302)

@app.route('/mytrashbox', defaults={'pathToDir':'home'})
@app.route('/mytrashbox/<pathToDir>')
def mytrashbox(pathToDir):
    paths = getTestPathData()
    backpath = ''
    currentdir = 'home'
    if(pathToDir == "home"):
        return render_template('trashbox.html', file=paths, backpath=backpath, currentdir=currentdir)

'''
    - Sprawdzenie czy użytkownik jest w bazie
    - Rejestracja użytkownika
'''
@app.route('/registry', methods=['POST'])
def registry():
    print("Autoryzacja rozpoczeta.")
    if request.form.get('action') == 'auth':
        gid = request.form.get('gid')
        res = isRegistered(gid)
        if res == True:
            print("Sukces!");
            return jsonify({'auth': res})
        else:
            print("Failed! isRegistred: {}".format(res));
            return jsonify({'auth': res})

    if request.form.get('action') == 'registry':
        print("Proces rejestracji: przechwycenie danych.")
        gid = request.form.get('gid')
        name = request.form.get('name')
        email = request.form.get('email')
        token = request.form.get('token')
        print("Zapis do bazy.")
        print("Odebrano dane: " + gid + " " + name + " " + email + " " + token);
        ans = Register(gid, name, email, token)
        print("Rejestracja: {0}".format(ans))
        return jsonify({'res': "Teraz jesteś jednym z nas i masz dostęp do swojego TrashBox'a! Najpierw jednak się zaloguj!"})


@app.route('/upload/',  methods=['POST'])
def upload():
    REQUESTED_FILES = request.files.getlist('fileToUpload')
    current_path = request.files.getlist('pathToDir')
    tab = FileUpload.upload(REQUESTED_FILES, current_path)

    for item in tab:
        print(item)

    return render_template('/upload_download/upload.html')

# @Permission.login
# @Log(LogType.INFO, 2, "-", printToConsole=False)
def startServer():
    if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0", port=5000)


startServer()
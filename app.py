import logging
import os
import sys
import static.configs.EnvConf
import tempfile
from time import sleep

from static.controllers.Permission import Permission
from static.tool.Logs import Log, LogType
from flask_mail import Mail, _Mail
from flask_mail import Message

from static.tool.FileManager import FileManager
from static.controllers.FileController import FileController
from static.classes.Registration import Register, isRegistered

from static.classes.FileUpload import FileUpload

from flask import Flask, render_template, send_file
from flask import request, session, jsonify

app = Flask(__name__)
app.secret_key = os.urandom(24)


def getTestFiles():
    paths = [{
        'fileID': '1',
        'Name': 'kociaki',
        'Extension': '.png',
        'FilePath': '/',
        'Size': '240000',
        'HashSum': '123',
        'Icon': 'file-image',
    },
        {
            'fileID': '2',
            'Name': 'TrashPanda',
            'Extension': 'None',
            'FilePath': '/',
            'Size': '2450000',
            'HashSum': '4556',
            'Icon': 'folder-open-empty',
        },
    ]
    return paths

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'trashpandacloud@gmail.com'
app.config['MAIL_PASSWORD'] = 'TrashPanda1'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail()
mail.init_app(app)




@app.route('/')
def index():
    return render_template('index.html')



@app.route('/maill', methods=['POST'])
def maill():
    text = request.form.get('message')
    tresc = text
    podpis = request.form.get('podpis')
    msg = Message("Message from user: " + podpis, sender='trashpandacloud@gmail.com', recipients=['orlikx@gmail.com'])
    msg.body = tresc + '\n' + podpis
    mail.send(msg)
    return "Sent"
    # text = request.form.get('message')
    # print("Mail: " + text)
    # return text


'''
    Dodanie/Update/Odczyt sesji
    
    :param name
    :param value
    :return value
'''
@app.route('/sessionControler', methods=['POST'])
def sessionControler():
    print("Wywolano session flask.")
    if request.form.get('action') == 'set':
        name = request.form.get('name')
        param = request.form.get('param')
        session[name] = param
        print("Dodano sesje o nazwie: " + name + " = " + param)
        return jsonify({'param': param})

    if request.form.get('action') == 'get':
        name = request.form.get('name')
        if name in session:
            param = session[name]
            print("Pobrano sesje o nazwie: " + name)
            return jsonify({'param': param})
        elif name in session:
            sleep(0.5)
            param = session[name]
            print("Pobrano sesje o nazwie: " + name)
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


@app.route('/download', methods=['POST'])
def download():
    if request.form.get('action') == 'download':
        path = request.form.get('path')
        # path = "/srv/Data/mikus/plik.txt"
        name = os.path.basename(path)
        return send_file(path, attachment_filename=name , as_attachment=True)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('info_pages/404.html'), 404
    # return redirect("https://www.asciipr0n.com/pr0n/morepr0n/pr0n04.txt", code=302)

@app.route('/mytrashbox', defaults={'pathToDir':'home'})
@app.route('/mytrashbox/<pathToDir>')
def mytrashbox(pathToDir):
    paths = pathToDir
    if paths == 'home':
        backpath = ''
        currentdir = 'home'
        finalPath = ''
    else:
        paths = paths.split('.')
        finalPath = ''
        currentdir = paths[-1]
        if len(paths)>1:
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
    files = getTestFiles()
    print("Files: " + str(len(files)))
    print("Get pathToDir: " + pathToDir)
    print("Set currentDir: " + currentdir)
    print("Set backPath: " + backpath)
    print("Set finalPath: " + finalPath)
    return render_template('trashbox.html', files=files, backpath=backpath, currentdir=currentdir)

'''
    - AJAX
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
            session['googleID'] = gid
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
        # print("Odebrano dane: " + gid + " " + name + " " + email + " " + token);
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

@app.route('/n/ser/h/', methods=['GET'])
def fortest():
    from static.controllers.AdminControllers.main import render
    return render()

@Permission.login
@Log(LogType.INFO, 2, "-", printToConsole=False)
def startServer():
    if __name__ == '__main__':
        # mi niie jebie kto zmienia porty i adress, no prosze śliedzić za danymi które commitujecie
        # tu jest kurwa mać 0.0.0.0 na porcie 5000!!!!!!!!
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        app.run(debug=True, host="0.0.0.0", port=5000)

startServer()

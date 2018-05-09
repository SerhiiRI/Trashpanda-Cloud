import logging
import sys
import static.configs.EnvConf
from static.controllers.Permission import Permission
import os
import static.configs.EnvironmentVariable
from static.controllers.authorization import Permission
import tempfile
from static.tool.Logs import Log, LogType
from static.tool.FileManager import FileManager
from flask import Flask, render_template, redirect, request, jsonify, send_file
from flask import Flask, render_template, redirect, request, jsonify, render_template_string, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/userCheck', methods=['POST'])
def userCheck():
    # print('Check userID...')
    id = request.form['uid']
    # print(id)
    if id:
        inDB = 'true'
        return jsonify({'res': inDB})

    return jsonify({'error': 'Missing data!'})


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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('info_pages/404.html'), 404
    # return redirect("https://www.asciipr0n.com/pr0n/morepr0n/pr0n04.txt", code=302)



@app.route('/mytrashbox', methods=['GET'])
def mytrashbox():
    getPath = request.args.get('path')
    print(getPath)
    '''
    ! Od Aleksa dla mikusia
    ! Tu ci podsyłam zmienną path w której będzie np home
    ! Zwróć mi ls (katalogi i piliki w home)    
    '''
    paths = [{
        'icon': 'file-image',
        'name': 'twoja_stara.png',
        'lock': 'lock',
        'size': '2.4 MB',
        'tag':['#hehe', '#lol', '#yolololololo', '#hehe', '#lol', '#yololo'],
    },
        {
            'icon': 'folder-open-empty',
            'name': 'twoja_stara.png',
            'lock': '',
            'size': '',
            'tag': [],
        }
    ]
    # backpath pozwoli wrócić do poprzedniego katalogu
    backpath = 'home'
    currentdir = 'home'
    # lista symuluje pętlę for w jinja2
    lista = []
    for x in range(0, 20):
        lista.append(x)
    return render_template('trashbox.html', file=paths, lista=lista, backpath=backpath, currentdir=currentdir)


@Permission.login
@Log(LogType.INFO, 2, "-", printToConsole=False)
def startServer():
    if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0", port=5000)


startServer()

import logging
import sys
import os
import static.configs.EnvironmentVariable
from static.controllers.authorization import Permission
import tempfile
from static.tool.Logs import Log, LogType
from static.tool.FileManager import FileManager
from flask import Flask, render_template, redirect, request, jsonify, send_file

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
        return jsonify({'res' : inDB})

    return jsonify({'error' : 'Missing data!'})


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


@app.route('/mytrashbox', methods=['GET','POST'])
def mytrashbox():
    try:
        path = "/" + request.form.get('google_id') + "/"
    except:
        path = "/"
    files = FileManager.listDir(path)
    return render_template('trashbox_test.html', items=files, path=path)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('info_pages/404.html'), 404
    # return redirect("https://www.asciipr0n.com/pr0n/morepr0n/pr0n04.txt", code=302)


#@Permission.login
@Log(LogType.INFO, 2, "-", printToConsole=False)
def startServer():
    if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0", port=5000)


startServer()
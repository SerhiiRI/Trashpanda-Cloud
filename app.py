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

from static.blueprints.testFile import getTestFiles
from static.blueprints.jsSessionFix import jsSessionFix
from static.blueprints.infoPages import infoPages
from static.blueprints.loginORregistry import loginORregistry
from static.blueprints.renderTrashbox import renderTrashbox
from static.blueprints.includeRender import includeRender

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(jsSessionFix)
app.register_blueprint(infoPages)
app.register_blueprint(loginORregistry)
app.register_blueprint(renderTrashbox)
app.register_blueprint(includeRender)


@app.route('/download', methods=['POST'])
def download():
    if request.form.get('action') == 'download':
        path = "/srv/Data" + request.form.get('path')
        # path = "/srv/Data/mikus/plik.txt"
        name = os.path.basename(path)
        return send_file(path, attachment_filename=name , as_attachment=True)


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
# @Log(LogType.INFO, 2, "-", printToConsole=False)
def startServer():
    if __name__ == '__main__':
        # mi niie jebie kto zmienia porty i adress, no prosze śliedzić za danymi które commitujecie
        # tu jest kurwa mać 0.0.0.0 na porcie 5000!!!!!!!!
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        app.run(debug=True, host="0.0.0.0", port=5000)

startServer()

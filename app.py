import logging
import os
import sys
import static.configs.EnvConf
import tempfile
from time import sleep

from static.blueprints.pathFix import pathFixer
from static.controllers.Permission import Permission
# from static.tool.Logs import Log, LogType
from static.tool.FileManager import FileManager
from static.controllers.FileController import FileController
from static.classes.Registration import Register, isRegistered

from static.classes.FileUpload import FileUpload

from flask import Flask, render_template, send_file, redirect
from flask import request, session, jsonify

from static.blueprints.testFile import getTestFiles
from static.blueprints.jsSessionFix import jsSessionFix
from static.blueprints.simpleRoute import simpleRoute
from static.blueprints.loginORregistry import loginORregistry
from static.blueprints.renderTrashbox import renderTrashbox
from static.blueprints.includeRender import includeRender
from static.blueprints.ajaxAction import ajaxAction

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(jsSessionFix)
app.register_blueprint(simpleRoute)
app.register_blueprint(loginORregistry)
app.register_blueprint(renderTrashbox)
app.register_blueprint(includeRender)
app.register_blueprint(ajaxAction)



@app.route('/download', methods=['POST'])
def download():
    if request.form.get('action') == 'download':
        path = request.form.get('path')
        # path = "/srv/Data/mikus/plik.txt"
        name = os.path.basename(path)
        return send_file(path, attachment_filename=name, as_attachment=True)



@app.route('/n/ser/h/', methods=['GET'])
def fortest():
    from static.controllers.AdminControllers.main import render
    return render()


@Permission.login
# @Log(LogType.INFO, 2, "-", printToConsole=False)
def startServer():
    if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0", port=5000)


startServer()

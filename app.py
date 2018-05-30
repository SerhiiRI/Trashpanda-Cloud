import logging
import os
import sys
import static.configs.EnvConf
import tempfile
from time import sleep

from static.blueprints.pathFix import pathFixer
from static.controllers.Permission import Permission
from static.tool.Logs import Log, LogType
from static.tool.FileManager import FileManager
from static.controllers.FileController import FileController
from static.classes.Registration import Register, isRegistered
from flask_mail import Mail, Message

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
from static.blueprints.searchEngine import searchEngine

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(jsSessionFix)
app.register_blueprint(simpleRoute)
app.register_blueprint(loginORregistry)
app.register_blueprint(renderTrashbox)
app.register_blueprint(includeRender)
app.register_blueprint(ajaxAction)
app.register_blueprint(searchEngine)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dendarrus@gmail.com'
app.config['MAIL_PASSWORD'] = 'Klaudynka123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail()
mail.init_app(app)


@app.route('/sendMail', methods=['POST'])
def sendMail():

    tresc = request.form.get('message')
    podpis = request.form.get('podpis')
    msg = Message("Message from user: " + podpis, sender='trashpandacloud@gmail.com',
                  recipients=['trashpandacloud@gmail.com'])
    msg.body = tresc + '\n' + podpis
    mail.send(msg)
    return 'Send message.'


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
@Log(LogType.INFO, 2, "Run application", printToConsole=False)
def startServer():
    if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0", port=5000)


startServer()

from static.classes.FileUpload import FileUpload

import logging
import sys
import os

import static.scripts.EnvironmentVariable
from flask import Flask, render_template, redirect, request, jsonify, send_file

app = Flask(__name__)
DUMP_DIR = "/srv/DUMP/"


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


@app.route('/mytrashbox')
def mytrashbox():
    return render_template('trashbox.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('info_pages/404.html')
    # return redirect("https://www.asciipr0n.com/pr0n/morepr0n/pr0n04.txt", code=302)


@app.route('/send')
def send():
    return render_template('upload_download/send.html')


@app.route('/upload',  methods=['POST'])
def upload():
    REQUESTED_FILES = request.files.getlist('fileToUpload')
    tab = FileUpload.upload(REQUESTED_FILES)

    for item in tab:
        print(item)

    return render_template('/upload_download/upload.html')

    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

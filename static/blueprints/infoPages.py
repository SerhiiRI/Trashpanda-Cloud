from flask import Blueprint, request, session, jsonify, render_template

infoPages = Blueprint('infoPages', __name__, template_folder='templates')


@infoPages.route('/')
def index():
    '''
    :return: Search and login page
    '''
    return render_template('index.html')


@infoPages.route('/info')
def info():
    '''
    :return: Info page
    '''
    return render_template('info_pages/info.html')


@infoPages.route('/about')
def about():
    '''
    :return: About us
    '''
    return render_template('info_pages/about.html')


@infoPages.route('/contact')
def kontakt():
    '''
    :return: page with contacts
    '''
    return render_template('info_pages/contact.html')


@infoPages.errorhandler(404)
def page_not_found(e):
    return render_template('info_pages/404.html'), 404

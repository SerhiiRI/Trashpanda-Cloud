from flask import Blueprint, request, session, jsonify, render_template, redirect

simpleRoute = Blueprint('simpleRoute', __name__, template_folder='templates')


@simpleRoute.route('/')
def index():
    '''
    :return: Search and login page
    '''
    return render_template('index.html')


@simpleRoute.route('/info')
def info():
    '''
    :return: Info page
    '''
    return render_template('info_pages/info.html')


@simpleRoute.route('/about')
def about():
    '''
    :return: About us
    '''
    return render_template('info_pages/about.html')


@simpleRoute.route('/contact')
def kontakt():
    '''
    :return: page with contacts
    '''
    return render_template('info_pages/contact.html')


@simpleRoute.errorhandler(404)
def page_not_found(e):
    return render_template('info_pages/404.html'), 404


@simpleRoute.route('/mytrashbox')
def mytrashbox():
    '''
    :return: template my trashbox
    '''
    if 'googleID' in session:
        gid = session['googleID']
        if gid:
            init = {'include': 'trashbox'}
            return render_template('trashbox_base.html', init=init)
    print('Trashbox: Access denied')
    return redirect('/')

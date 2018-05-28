from flask import Blueprint, session, render_template, redirect, url_for
from static.blueprints.testFile import getTestFiles

includeRender = Blueprint('includeRender', __name__, template_folder='templates')


@includeRender.route('/include/include_trashbox')
def renderMyTrashbox():
    '''
    :return: my Trashbox with ajax
    '''
    print('Including.')
    if 'googleID' in session:
        gid = session['googleID']
        if gid:
            print('Pobranie szablonu my trashbox.')
            return render_template('include/include_trashbox.html', files=getTestFiles())
    return redirect('/')

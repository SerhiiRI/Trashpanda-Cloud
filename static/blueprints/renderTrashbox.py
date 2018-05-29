from flask import Blueprint, session, render_template

from static.controllers.FileController import FileController

renderTrashbox = Blueprint('renderTrashbox', __name__, template_folder='templates')


@renderTrashbox.route('/mytrashbox')
def mytrashbox():
    '''
    :return: template my trashbox
    '''
    init = {'include': 'trashbox'}
    return render_template('trashbox_base.html', init=init)

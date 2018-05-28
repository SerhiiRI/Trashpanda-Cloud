from time import sleep
from flask import Blueprint, request, session, jsonify

jsSessionFix = Blueprint('jsSessionFix', __name__, template_folder='templates')


@jsSessionFix.route('/sessionControler', methods=['POST'])
def sessionControler():
    '''
        Session:
        * Add
        * Update
        * Get
        :param set name of session
        :param set value in to session
        :return get value from session
    '''
    print("Wywolano session flask.")
    if request.form.get('action') == 'set':
        name = request.form.get('name')
        param = request.form.get('param')
        session[name] = param
        print("Dodano sesje o nazwie: " + name + " = " + param)
        return jsonify({'param': param})

    if request.form.get('action') == 'get':
        name = request.form.get('name')
        if name in session:
            param = session[name]
            print("Pobrano sesje o nazwie: " + name)
            return jsonify({'param': param})
        elif name in session:
            sleep(0.5)
            param = session[name]
            print("Pobrano sesje o nazwie: " + name)
            return jsonify({'param': param})
        else:
            print("Nie znaleziono sesji: " + name)
            return jsonify({'param': ''})

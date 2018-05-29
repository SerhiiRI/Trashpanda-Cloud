from flask import Blueprint, request, session, jsonify
from static.classes.Registration import Register, isRegistered

loginORregistry = Blueprint('loginORregistry', __name__, template_folder='templates')

@loginORregistry.route('/registry', methods=['POST'])
def registry():
    '''
        * AJAX
        * Sprawdzenie czy użytkownik jest w bazie
        * Rejestracja użytkownika
    '''
    print("Autoryzacja rozpoczeta.")
    if request.form.get('action') == 'auth':
        gid = request.form.get('gid')
        res = isRegistered(gid)
        if res == True:
            print("Sukces!");
            session['googleID'] = gid
            return jsonify({'auth': res})
        else:
            print("Failed! isRegistred: {}".format(res));
            return jsonify({'auth': res})

    if request.form.get('action') == 'registry':
        print("Proces rejestracji: przechwycenie danych.")
        gid = request.form.get('gid')
        name = request.form.get('name')
        email = request.form.get('email')
        token = request.form.get('token')
        print("Zapis do bazy.")
        ans = Register(gid, name, email, token)
        print("Rejestracja: {0}".format(ans))
        return jsonify({'res': "Teraz jesteś jednym z nas i masz dostęp do swojego TrashBox'a! Najpierw jednak się zaloguj!"})

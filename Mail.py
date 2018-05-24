from flask import Flask, request
from flask_mail import Mail
from flask_mail import Message

app2 = Flask(__name__)
app2.config['MAIL_SERVER'] = 'smtp.gmail.com'
app2.config['MAIL_PORT'] = 465
app2.config['MAIL_USERNAME'] = 'trashpandacloud@gmail.com'
app2.config['MAIL_PASSWORD'] = 'TrashPanda1'
app2.config['MAIL_USE_TLS'] = False
app2.config['MAIL_USE_SSL'] = True
mail = Mail(app2)

zmienna = "nr uzytkownika lub tytul maila"
tresc = "Przykladowa zawartosc maila"
podpis = "przeslany podpis"


@app2.route("/")
def index():
    msg = Message(zmienna, sender='trashpandacloud@gmail.com', recipients=['orlikx@gmail.com'])
    msg.body = tresc + podpis
    mail.send(msg)
    return "Sent"


if __name__ == '__main__':
    app2.run(debug=True)

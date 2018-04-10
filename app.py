from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    info = [{
        'title':'Trushpanda Cloud',
        'info':'Trashpanda!',
    }]
    return render_template('index.html', info=info)


if __name__ == '__main__':
    app.run(debug=True)

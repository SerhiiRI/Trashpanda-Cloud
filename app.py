from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    info = 'Trashpanda Cloud'
    return render_template('index.html', info=info)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

import static.scripts.EnvironmentVariable
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/about')
def about():
    return render_template('about.html')
    # return redirect("https://www.asciipr0n.com/pr0n/morepr0n/pr0n03.txt", code=302)
    # hackerman... jo-jo-jo

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
    # return redirect("https://www.asciipr0n.com/pr0n/morepr0n/pr0n04.txt", code=302)
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

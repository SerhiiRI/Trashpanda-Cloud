from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # info = [{
    #     'title':'Trushpanda Cloud',
    #     'id':'23487623874623764',
    #     'pic':'/static/pic/testpic.jpg',
    # }]
    info = ["Trashpanda Cloud"]
    userData = [23487623874623764, "/static/pic/testpic.jpg"]
    return render_template('index.html', info=info, data=userData)


if __name__ == '__main__':
    app.run(debug=True)

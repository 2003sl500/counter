from types import MethodDescriptorType
from flask import Flask, render_template, request, redirect, session
from flask.helpers import url_for
app = Flask(__name__)
app.secret_key = "1234567890"

@app.route("/")
def index():
    if 'count' in session:
        print('key exists')
        session['count'] += int(1)
        result = session['count']
    else:
        print("key 'counter' does NOT exist")
        session['count'] = int(1)
        result = session['count']
    
    return render_template("index.html", result = result)

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    result = 0
    return render_template('index.html', result = result)

@app.route('/counter', methods = ['POST'])
def counter():
    session['count'] += int(2)
    result =  session['count']
    return render_template("index.html", result = result)

@app.route('/reset', methods = ['POST'])
def reset():
    session['count'] = 0
    result = session['count']
    return render_template("index.html", result = result)

if __name__ == "__main__":
    app.run(debug=True)
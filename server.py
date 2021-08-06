from flask import Flask, render_template, redirect, session
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

@app.route('/destroy_session', methods = ['POST'])
def destroy_session():
    session.clear()
    result = 0
    return redirect('/')

@app.route('/counter', methods = ['POST'])
def counter():
    session['count'] += int(1)
    result =  session['count']
    return redirect("/")

@app.route('/reset', methods = ['POST'])
def reset():
    session['count'] = 0
    result = session['count']
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
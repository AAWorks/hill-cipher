from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'physiscmakesmesad'

@app.route('/', methods=['GET','POST'])
def landing_page():
    return render_template("landing_page.html")

@app.route('/machine', methods=['GET', 'POST'])
def machine():
    return render_template("machine.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
    text = request.form["text"]
    field00 = request.form["field00"]
    field01 = request.form["field01"]
    field10 = request.form["field10"]
    field11 = request.form["field11"]
    return render_template("result_page.html")

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
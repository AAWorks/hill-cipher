from flask import Flask, render_template, request, session, redirect, url_for
import numpy as np

with open("app/cipher.py", "rb") as source_file:
    code = compile(source_file.read(), "app/cipher.py", "exec")
exec(code)

app = Flask(__name__)
app.secret_key = 'physiscmakesmesad'

@app.route('/', methods=['GET','POST'])
def landing_page():
    try:
        return render_template("landing_page.html")
    except:
        return render_template("error.html")

@app.route('/machine', methods=['GET', 'POST'])
def machine():
    try:
        return render_template("machine.html")
    except:
        return render_template("error.html")

@app.route('/encode', methods=['GET', 'POST'])
def encode():
    text = request.form["text"]
    matrix = [[request.form["00"], request.form["01"]], [request.form["10"], request.form["11"]]]
    if "" in matrix or text == "":
        return redirect('/machine')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])
    result = encrypt(text, matrix)
    return render_template("result_page.html", result=result)

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    text = request.form["text"]
    key = request.form["key"]
    if text == "" or key == "" or len(key) != len(text) ** 2:
        return redirect('/machine')
    result="nothing here yet"
    return render_template("result_page.html", result=result)

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
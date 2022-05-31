from flask import Flask, render_template, request, session, redirect, url_for

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

@app.route('/loading')
def load():
    try:
        return render_template('loading_page.html')
    except:
        return render_template('error.html')

@app.route('/cipher', methods=['GET', 'POST'])
def encode():
    global result
    text = request.form["text"]
    matrix = [[request.form["00"], request.form["01"]], [request.form["10"], request.form["11"]]]
    if text == "":
        return redirect('/machine')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not matrix[i][j]:
                return redirect('/machine')
            matrix[i][j] = int(matrix[i][j])
    result = encrypt(text, matrix, False) if request.form["cipher"] == "Encode" else decrypt(text, matrix, True)
    return redirect("/loading")

@app.route('/result', methods=['GET', 'POST'])
def result():
    try:
        if type(result) != str:
            return render_template('result_page.html', result="Refreshed or fiddling with the url? Either way, begone!")
        return render_template('result_page.html', result=result)
    except:
        return render_template('error.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run(port=8000)
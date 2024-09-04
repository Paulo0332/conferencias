from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/conferencia1")
def conferencia1():
    return render_template("conferencia1.html")

@app.route("/conferencia2")
def conferencia2():
    return render_template("conferencia2.html")

@app.route("/conferencia3")
def conferencia3():
    return render_template("conferencia3.html")

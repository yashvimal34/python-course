from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = "yash1233003648dkjh939093"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/flash")
def flash_message():
    flash("This is flash message!")
    return redirect(url_for('index'))

app.run(debug=True)
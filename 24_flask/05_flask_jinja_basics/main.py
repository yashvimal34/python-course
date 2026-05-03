from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "Ramesh":90,
        "Krishna":89,
        "Asmit":100,
        "Yash":96
    }
    return render_template("index.html", marks=marks)
app.run(debug=True)
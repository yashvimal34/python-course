from flask import Flask, render_template

# app = Flask(__name__, static_url_path="/public") # THis is how you can change the url path, but remember one thing that when you are changing url make sure you have put '/'.

app = Flask(__name__, static_folder="assets", static_url_path="/public") # by changing folder remove '/'.

@app.route("/")
def hello_world():
    return render_template("index.html")

app.run(debug=True)
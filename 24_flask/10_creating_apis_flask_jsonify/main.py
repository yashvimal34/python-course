from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def json():
    marks = {
        "Yash": 98,
        "Rahul": 89,
        "Kartikeya": 70,
        "Utkarsh": 96,
        "Vansh": 56,
        "Vinay": 76,
    }
    values = [1, marks, 66]
    return jsonify(values)

app.run(debug=True)
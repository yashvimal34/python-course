from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "pub_9932339419384906bafc8654e4fb569c"  # Replace with your API key

@app.route("/", methods=["GET", "POST"])
def index():
    news_list = []
    query = ""

    if request.method == "POST":
        query = request.form.get("query")
        url = f"https://newsdata.io/api/1/latest?apikey={API_KEY}&q={query}"
        response = requests.get(url)
        data = response.json()

        if "results" in data:
            news_list = data["results"]

    return render_template("index.html", news_list=news_list, query=query)

if __name__ == "__main__":
    app.run(debug=True)

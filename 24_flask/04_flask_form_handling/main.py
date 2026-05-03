from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["Get", "POSt"])
def form():
    if (request.method == "POST"):

        # Let's see how to handle the form.

        with open("file.txt", "w") as f:
            f.write(f"The name is {request.form['name']} and the email is {request.form['email']}")
        return render_template("form.html")
    
            # But remember the above the method is not recomended for production or any professional work.
    else:
        return render_template("form.html")

app.run(debug=True)
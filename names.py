from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

names = []

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    if name:
        names.append(name)
    return redirect(url_for("index"))

@app.route("/list")
def name_list():
    return render_template("list.html", names=names)

if __name__ == "__main__":
    app.run(port=5001, debug=True)

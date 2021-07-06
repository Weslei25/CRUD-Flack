from app import app
from flask import render_template


@app.route("/index/<user>")
@app.route("/", defaults={"user":None, "password":None})
def index(user, password):
    return render_template("index.html")

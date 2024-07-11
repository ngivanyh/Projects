from flask import Flask, render_template, request, redirect, session
from subprocess import run
from flask_session import Session


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


output = ""

@app.route("/", methods=["GET", "POST"])
def root():
    global output
    if request.method == "POST":
        user_cmd = request.form.get("cmd")
        user_in = request.form.get("input")
        cmd = run(user_cmd.split(), capture_output=True, input=user_in.encode())
        output = cmd.stdout.decode()

        return redirect("/")
    else:
        return render_template("index.html", output=output)
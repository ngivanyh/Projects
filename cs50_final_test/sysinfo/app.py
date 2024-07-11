from flask import Flask, render_template
import platform, socket

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():

    sysinfo = [platform.processor(), platform.architecture(), platform.system(), platform.node(), platform.platform(), socket.gethostbyname(socket.gethostname())]
    return render_template("index.html", sysinfo=sysinfo)
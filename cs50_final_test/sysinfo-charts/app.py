from flask import Flask, render_template
import platform, socket, psutil

app = Flask(__name__)

sysinfo_general = platform.uname()
cpu_info = platform.processor()
cpu_count = psutil.cpu_count(logical=False)
logical_cpu_count = psutil.cpu_count(logical=True)

sysinfo = [sysinfo_general.system, sysinfo_general.node, sysinfo_general.release, sysinfo_general.version, sysinfo_general.machine, sysinfo_general.processor]
cpu_infos = [cpu_info, cpu_count, logical_cpu_count]
memory = psutil.virtual_memory().percent

@app.route("/", methods=["GET"])
def root():
    print(memory)
    return render_template("index.html", sysinfo=sysinfo, cpu_infos=cpu_infos, memory=memory)
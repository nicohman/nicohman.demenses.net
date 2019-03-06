from flask import Flask,send_from_directory,send_file,abort
import os
app = Flask(__name__)
@app.route("/")
def index():
    return send_file("export/index.html")
@app.route("/<path:path>")
def serve(path):
    files = os.listdir("export")
    if path in files:
        return send_from_directory("export",path)
    elif path + ".html" in files:
        return send_from_directory("export",path + ".html")
    else:
        abort(404)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 4000)

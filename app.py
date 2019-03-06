from flask import Flask,send_from_directory,send_file,abort
import os
from export import export
export()
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
@app.errorhandler(404)
def not_found():
    return "The path you specified could not be found."
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 4000)

from pyquery import PyQuery as pq
from org_sourcehut.convert import convert,export_all
import os
import json
def export():
    fd = open("config.json", "r")
    config = json.load(fd)
    links = config['links']
    os.system("emacs --batch -l export.el -f export")
    export_all("export",links=links,show_up_link=False)
if __name__ == "__main__":
    export()

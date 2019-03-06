from pyquery import PyQuery as pq
from org_sourcehut.convert import convert
import os
import json
def is_html(name):
    return ".html" in name
def export():
    fd = open("config.json", "r")
    config = json.load(fd)
    links = config['links']
    os.system("emacs --batch -l export.el -f export")
    pages = os.listdir("export")
    for page in filter(is_html,pages):
        convert("export/"+page, links=links, show_up_link=False)
if __name__ == "__main__":
    export()

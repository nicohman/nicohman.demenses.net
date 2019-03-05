from pyquery import PyQuery as pq
from org_sourcehut.convert import convert
import os
def is_html(name):
    return ".html" in name
os.system("emacs --batch -l export.el -f export")
pages = os.listdir("export")
for page in filter(is_html,pages):
    convert("export/"+page)

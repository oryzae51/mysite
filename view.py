import os
from html_sanitizer import Sanitizer

def getList():
    sanitizer = Sanitizer()
    files = os.listdir('data')
    listStr = ''
    for i in files:
        i = sanitizer.sanitize(i)
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name = i)
    return listStr

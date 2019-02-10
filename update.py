#!C:\Users\starh\AppData\Local\Programs\Python\Python36\python.exe
#-*- coding: utf-8 -*-
import sys
import codecs
import cgi
import os
import view
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print('''content-type: text/html; charset=utf-8\n''')

form = cgi.FieldStorage()
if 'id' in form:
	pageId = form["id"].value
	description = open('data/'+pageId, 'r', encoding='UTF-8').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'

files = os.listdir('data')
lstStr = ''
for i in files:
    lstStr = lstStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=i)


print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {lstStr}
  </ol>
  <a href="create.py">create</a>
  <form action="process_update.py" method="post">
  	<input type="hidden" name="pageId" value="{form_default_title}">
    <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
    <p><textarea rows="4" name="description" placeholder="description" >{form_default_description}</textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId, desc=description, lstStr=view.getList(), form_default_title=pageId, form_default_description=description))

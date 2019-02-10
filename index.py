#!C:\Users\starh\AppData\Local\Programs\Python\Python36\python.exe
#-*- coding: utf-8 -*-
import sys
import codecs
import cgi
import os
import view
from html_sanitizer import Sanitizer
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print('''content-type: text/html; charset=utf-8\n''')

form = cgi.FieldStorage()
if 'id' in form:
	title = pageId = form["id"].value
	description = open('data/'+pageId, 'r', encoding='UTF-8').read()
	#description = description.replace('<', '&lt;')
	#description = description.replace('>', '&gt;')
	sanitizer = Sanitizer()
	title = sanitizer.sanitize(title)
	description = sanitizer.sanitize(description)
	update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
	delete_action = '''
		<form action="process_delete.py" method="post">
			<input type="hidden" name="pageId" value="{}">
			<input type="submit" value="delete">
		</form>
	'''.format(pageId)
else:
	title = pageId = 'Welcome'
	description = 'Hello, web'
	update_link = ''
	delete_action = ''

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
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=title, desc=description, lstStr=view.getList(), update_link=update_link, delete_action=delete_action))

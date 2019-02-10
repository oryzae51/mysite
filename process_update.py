#!C:\Users\starh\AppData\Local\Programs\Python\Python36\python.exe
#-*- coding: utf-8 -*-
import sys
import codecs
import cgi
import os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value

opened_file=open('data/'+pageId, 'w', encoding='UTF-8')
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageId, 'data/'+title)

###중요!!!###
#redirection 이라는 헤더라고 함
print("Location: index.py?id="+title, "\n")

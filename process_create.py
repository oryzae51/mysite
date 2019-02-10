#!C:\Users\starh\AppData\Local\Programs\Python\Python36\python.exe
#-*- coding: utf-8 -*-
import sys
import codecs
import cgi
import os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value

opened_file=open('data/'+title, 'w', encoding='UTF-8')
opened_file.write(description)
opened_file.close()

###중요!!!###
#redirection 이라는 헤더라고 함
print("Location: index.py?id="+title, "\n")

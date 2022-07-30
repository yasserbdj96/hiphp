#!/usr/bin/env python
# coding:utf-8
#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

#START{
import eel
from hiphp import *
from src.php import *
import os


eel.init(f'{os.path.dirname(os.path.realpath(__file__))}/src')
#eel.init('src')

#connect:
@eel.expose
def connect(key,url):
    p1=hiphp(key,url,retu=True)
    try:
        connected=p1.run("echo 'connected!';")
        if connected=="connected!":
            return "connected"
        else:
            hole=p1.get_hole()
            return hole
    except:
        hole=p1.get_hole()
        return hole

#ls:
@eel.expose
def ls(key,url):
    p1=hiphp(key,url,retu=True)
    return p1.run(php_ls())

#cat:
@eel.expose
def cat(key,url,path):
    p1=hiphp(key,url,retu=True)
    return p1.run(php_cat(path))

#save:
@eel.expose
def save(key,url,path,content):
    p1=hiphp(key,url,retu=True)
    return p1.run(php_save(path,content))

#delete:
@eel.expose
def delte(key,url,path):
    p1=hiphp(key,url,retu=True)
    return p1.run(php_delte(path))

#rename:
@eel.expose
def ren(key,url,path,newname):
    p1=hiphp(key,url,retu=True)
    return p1.run(php_ren(path,newname))

#add:
@eel.expose
def add_new(key,url,path):
    p1=hiphp(key,url,retu=True)
    return p1.run(php_add(path))

#permissions:
@eel.expose
def new_permi(key,url,path,permi):
    p1=hiphp(key,url,retu=True)
    return p1.run(php_permi(path,permi))

eel.start("index.html",host="127.0.0.2",port=96,size=(850,400))
#}END.

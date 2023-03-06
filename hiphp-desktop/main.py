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
import sys
import os
import json

try:
    try:
        sys.path.insert(0,f'..{os.sep}hiphp')
        from hiphp import *
        from hiphp.hiphpversion import __version__
    except:
        # this just if hiphp installed on ubuntu:
        sys.path.insert(0, '/usr/share/hiphp/')
        from hiphp import *
        from hiphp.hiphpversion import __version__
except:
    try:
        from hiphp import *
        from hiphp.hiphpversion import __version__
    except:
        sys.path.insert(0, '..')
        from hiphp import *
        from hiphp.hiphpversion import __version__
    
import eel
from src.php import *

hiphp_desktop_version="0.2.0"

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
def version():
    return "Desktop V"+hiphp_desktop_version,"hiphp V"+__version__

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

#info:
@eel.expose
def info(key,url,path):
    p1=hiphp(key,url,retu=True)
    return p1.run(php_file_info(path))

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

#down_from_path:
@eel.expose
def download_file(key,url,path):
    p1=hiphp(key,url,retu=True)
    return p1.run(down_from_path(path))

#darkmode:
@eel.expose
def darkmode():
    thispath=os.path.dirname(os.path.abspath(__file__))
    with open(f'{thispath}/src/config.json', 'r+') as f:
        data = json.load(f)
        if data['Dark Mode']=="True":
            data['Dark Mode']="False"
        else:
            data['Dark Mode']="True"
        how=data['Dark Mode']
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()  
    return how

try:
    run_type=sys.argv[1]
    if run_type=="ipynb":
        host_ip="127.0.0.1"
        host_port=1000
    elif run_type=="docker":
        host_ip="0.0.0.0"
        host_port=8080
    elif run_type=="local":
        host_ip="127.0.0.1"
        host_port=8080
    else:
        exit()
except:
    print(f"USAGE : python3 {sys.argv[0]} <ipynb/docker/local>")

#iswork:
@eel.expose
def iswork():
    return "True"

print(f"hiphp-dst run on : {run_type}@{host_ip}:{host_port}")

if run_type=="docker":
    import socket
    ip_address = socket.gethostbyname(socket.gethostname())
    print(f"Listening on {ip_address}:{host_port}")

#eel.start("index.html",host=host_ip,port=host_port,size=(1050,500))
if run_type=="ipynb":
    from pyngrok import ngrok

    try:
        auth_token=sys.argv[2]
    except:
        print(f"USAGE : python3 {sys.argv[0]} <ipynb> <auth_token>")
        exit()

    ngrok.set_auth_token(auth_token)
    public_url = ngrok.connect(host_port).public_url
    print(f"Sharing app at {public_url}")
    eel.start("index.html",host=host_ip,port=host_port)
    with True:
        pass

    print("Killing streamlit app")
    print("Killing ngrok tunnel")
    ngrok.kill()
    raise
else:
    eel.start("index.html",host=host_ip,port=host_port,mode='default')
#}END.

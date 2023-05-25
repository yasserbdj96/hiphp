#!/usr/bin/env python
# coding:utf-8
#   |                                                         |   #
# --+---------------------------------------------------------+-- #
#   |    Code by: yasserbdj96                                 |   #
#   |    Email: yasser.bdj96@gmail.com                        |   #
#   |    GitHub: github.com/yasserbdj96                       |   #
#   |    Sponsor: github.com/sponsors/yasserbdj96             |   #
#   |    BTC: bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9      |   #
#   |                                                         |   #
#   |    All posts with #yasserbdj96                          |   #
#   |    All views are my own.                                |   #
# --+---------------------------------------------------------+-- #
#   |                                                         |   #

#START{
from flask import Flask, request, render_template
import sys

# import hiphp:
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


app = Flask(__name__)

# home:
@app.route('/')
def index():
    return render_template('index.html')

# login:
@app.route('/login', methods=['POST'])
def login():
    u = request.form['u']
    p = request.form['p']
    p1=hiphp(p,u,retu=True)
    try:
        connected=p1.run("echo 'yes!';")
        if connected=="yes!":
            return connected
        else:
            hole=p1.get_hole()
            return hole
    except:
        hole=p1.get_hole()
        return hole

@app.route('/search')
def search():
    query = request.args.get('q')
    return f'Searching for "{query}"'

if __name__ == '__main__':
    app.run(debug=True)
#}END.
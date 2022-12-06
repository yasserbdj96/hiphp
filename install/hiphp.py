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
from hiphp import *
from hiphp.hiphpversion import __version__
import sys

#help
if sys.argv[1]=="--help":
    from hiphp.hiphphelp import *
    print(help(__version__))
    exit()

#geth
elif sys.argv[1]=="--geth":
    try:
        p1=hiphp(key=sys.argv[2],url=sys.argv[3],lang=sys.argv[4])
    except:
        p1=hiphp(key=sys.argv[2],url=sys.argv[3])
    # Get the hole Code:
    p1.get_hole()# Copy this code into the file whose path you entered earlier. ex: https://localhost/index.php
    exit()

#version
elif sys.argv[1]=="--version":
    print(__version__)
#
else:
    KEY=sys.argv[1]
    URL=sys.argv[2]
    try:
        LANG=sys.argv[3]
    except:
        LANG="php"

    p2=hiphp(key=KEY,url=URL,lang=LANG,retu=True)
    p1=hiphp(key=KEY,url=URL,lang=LANG)#Default: retu=False.
    # Command line interface:
    if emsg_1 not in p2.cli():
        p1.cli()
    else:
        # Get the hole Code:
        p1.get_hole()# Copy this code into the file whose path you entered earlier. ex: https://localhost/index.php
#}END.
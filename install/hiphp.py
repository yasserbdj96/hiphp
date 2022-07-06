#!/usr/bin/env python
# coding:utf-8
# code by : yasserbdj96
# email : yasser.bdj96@gmail.com

#START{
from hiphp import *
import sys

if sys.argv[1]=="--help":
    from hiphp.hiphphelp import *
    print(help())
    exit()
elif sys.argv[1]=="--geth":
    p1=hiphp(key=sys.argv[2],url=sys.argv[3])
    # Get the hole Code:
    p1.get_hole()# Copy this code into the file whose path you entered earlier. ex: https://localhost/index.php
    exit()
else:
    KEY=sys.argv[1]
    URL=sys.argv[2]
    p2=hiphp(key=KEY,url=URL,retu=True)
    p1=hiphp(key=KEY,url=URL)#Default: retu=False.
    # Command line interface:
    if emsg_1 not in p2.cli():
        p1.cli()
    else:
        # Get the hole Code:
        p1.get_hole()# Copy this code into the file whose path you entered earlier. ex: https://localhost/index.php
#}END.


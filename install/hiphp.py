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
    # connect:
    p1=hiphp(key=sys.argv[1],url=sys.argv[2])#Default: retu=False.
    # Command line interface:
    p1.cli()
#}END.

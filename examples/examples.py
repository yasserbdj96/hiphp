#!/usr/bin/env python
# coding:utf-8
# code by : yasserbdj96
# email : yasser.bdj96@gmail.com

#START{
from hiphp import *

try:
    import os
    import sys
    #
    URL = os.environ['URL'] if "URL" in os.environ else sys.argv[2]
    KEY = os.environ['KEY'] if "KEY" in os.environ else sys.argv[1]
except Exception as e:
    print(f"USAGE : python3 {sys.argv[0]} <KEY> <URL>")
    exit()
    #pass

# connect:
p1=hiphp(key=KEY,url=URL)#Default: retu=False.

# Get the hole Code:
p1.get_hole()# Copy this code into the file whose path you entered earlier. ex: https://localhost/index.php

# Example:1
# Command:
p1.run("echo 'this is a test';")

# Example:2
# Run code from file:
p1.run_file("./examples.php")# Run code from file.
p1.run_file("./examples.php","var1==true","var2==hiii")# Run code from file With the entry of variables.

# Example:3
# Upload a file:
p1.upload("./examples.php")# Upload a file to the current directory.
p1.upload("./examples.php","./upload_path/")# Upload a file to a specific directory.

# Example:4
# Command line interface:
p1.cli()
#}END.
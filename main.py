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
import argparse
import os
import sys

from hiphp import *
from hiphp.hiphpversion import __version__
from hiphp.hiphplogo import logo
from hiphp.hiphphelp import *

python_path = sys.executable

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add arguments with names
parser.add_argument('--KEY', '--key', dest='KEY', type=str, default=os.getenv('KEY', ''), help='Specifies the key (key) for the operation.')
parser.add_argument('--URL', '--url', dest='URL', type=str, default=os.getenv('URL', ''), help='Specifies the URL (url) for the operation.')
parser.add_argument('--DOCKER', '--docker', dest='DOCKER', action='store_true', default=bool(os.getenv('DOCKER', False)), help='Specifies whether to use Docker (docker) or not. Set to "True" to enable Docker usage.')
parser.add_argument('--DST', '--dst', dest='DST', action='store_true', default=bool(os.getenv('DST', False)), help='')
parser.add_argument('--TK', '--tk', dest='TK', action='store_true', help='')
parser.add_argument('--IPYNB', '--ipynb', dest='IPYNB', action='store_true', default=bool(os.getenv('IPYNB', False)), help='')
parser.add_argument('--TOKEN', '--token', dest='TOKEN', type=str, default=os.getenv('TOKEN', ''), help='Specifies the token (token) for the operation.')

parser.add_argument('--HELP', '--h', dest='HELP', default=os.getenv('HELP', False), action='store_true', help='')
parser.add_argument('--GETH', '--geth', dest='GETH', default=os.getenv('GETH', False), action='store_true', help='')
parser.add_argument('--VERSION', '--version', '--v', dest='VERSION', default=os.getenv('VERSION', False), action='store_true', help='')

parser.add_argument('--VIEWLOGO', '--viewlogo', dest='VIEWLOGO', default=os.getenv('VIEWLOGO', False), action='store_true', help='')

# Parse the command-line arguments
args = parser.parse_args()

# Check if --IPYNB exists and --TOKEN does not exist
if args.IPYNB and not args.TOKEN:
    print("Error: --IPYNB exists, but --TOKEN is missing. Aborting script execution.")
    exit()

# Access the variables by their names
KEY = args.KEY
URL = args.URL
DOCKER=args.DOCKER
IPYNB=args.IPYNB
DST=args.DST
TK=args.TK
TOKEN=args.TOKEN
#
HELP = args.HELP
GETH = args.GETH
VERSION = args.VERSION

VIEWLOGO = args.VIEWLOGO

#help
if HELP:
    print(help(__version__))
    exit()

if VIEWLOGO:
    print(logo(__version__))
    exit()

#geth
if GETH:
    p1=hiphp(key=KEY,url=URL)
    # Get the hole Code:
    p1.get_hole()# Copy this code into the file whose path you entered earlier. ex: https://localhost/index.php
    exit()

#version
if VERSION:
    print(__version__)
    exit()

# hiphp-desktop
if DST:
    os.chdir("hiphp-desktop")
    if DOCKER:
        os.system(f"{python_path} main.py --DOCKER")
    elif IPYNB:
        command=f'{python_path} main.py --IPYNB'
        arguments=[]
        # Assuming KEY contains the value 'm123' or m123
        if TOKEN!='':
            arguments.append('--TOKEN')
            arguments.append(TOKEN)

        subprocess_args = [command] + arguments
        os.system(" ".join(subprocess_args))
        #os.system(f"{python_path} main.py --IPYNB --TOKEN='{TOKEN}'")
    else:
        os.system(f"{python_path} main.py")

# hiphp-tk
elif TK:
    os.chdir("hiphp-tk")
    command=f'{python_path} main.py'
    arguments=[]
    # Assuming KEY contains the value 'm123' or m123
    if KEY!='':
        arguments.append('--key')
        arguments.append(KEY)
    if URL!='':
        arguments.append('--url')
        arguments.append(URL)
    subprocess_args = [command] + arguments
    os.system(" ".join(subprocess_args))

else:
    if KEY=="" or URL=="" and not VIEWLOGO:
        file_path = os.path.basename(__file__)
        os.system(f"{python_path} {file_path} --help")
        exit()
    elif VIEWLOGO:
        pass
    else:
        # connect:
        p1=hiphp(key=KEY,url=URL)#Default: retu=False.
        p2=hiphp(key=KEY,url=URL,retu=True)

        # Command line interface:
        if emsg_1 not in p2.cli():
            p1.cli()
        else:
            # Get the hole Code:
            p1.get_hole()# Copy this code into the file whose path you entered earlier. ex: https://localhost/index.php
#}END.
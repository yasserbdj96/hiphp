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
from hexor import *
from hiphp.hiphpfunc import center

# logo:
def logo(__version__):
    logo=""
    c_red="#ea4335"#red
    c_blue="#4285f4"#blue
    c_yellow="#fbbc05"#yellow
    c_green="#34a853"#green
    c_white="#f7f7f7"

    color=hexor(True,"hex")
    #bl=biglibrary(returning=True)
    logox="\n"
    logox+=color.c(center("             ▄███████▄    ▄█    █▄       ▄███████▄"),c_red)
    logox+="\n"
    logox+=color.c(center("            ███    ███   ███    ███     ███    ███"),c_red)
    logox+="\n"
    logox+=color.c(center("╦   ╦       ███    ███   ███    ███     ███    ███"),c_red)
    logox+="\n"
    logox+=color.c(center("║   ║ ═╦═ ▀█████████▀  ▀▀███▀▀▀▀███▀  ▀█████████▀ "),c_red)
    logox+="\n"
    logox+=color.c(center("╠═══╣  ║    ███          ███    ███     ███       "),c_red)
    logox+="\n"
    logox+=color.c(center("║   ║  ║    ███          ███    ███     ███       "),c_red)
    logox+="\n"
    logox+=color.c(center("╩   ╩ ═╩═  ▄████▀        ███    █▀     ▄████▀     "),c_red)
    logox+="\n"
    logox+=color.c(center("+-----------------------------------------------------------------------------------+"),c_red)
    logox+="\n"
    logox+=color.c(center(f"HIPHP - Free & Open Source Project"),c_yellow)
    logox+="\n"
    logox+=color.c(center(f"A Backdoor Tool for Controlling PHP-based Sites"),c_yellow)
    logox+="\n"
    logox+=color.c(center(f"Version: {__version__} by yasserbdj96"),c_green)
    logox+="\n"
    logox+=color.c(center(f"Visit: https://yasserbdj96.github.io/hiphp/"),c_blue)
    logox+="\n"
    logox+=color.c(center("+-----------------------------------------------------------------------------------+"),c_red)
    logox+="\n"
    logox+=color.c("\n [!] '--help' for more informations.\n",c_yellow)
    logox+=color.c(" [!] '--exit' OR 'Ctrl+C' for exit.\n",c_yellow)
    #logox+="\n"

    return logox
#
"""
try:
    import sys
    from hiphpversion import __version__
    if sys.argv[1]=="ok_view":
        print("hiii")
        #print(logo(__version__))
        exit()
    else:
        pass
except:
    pass"""
#}END.

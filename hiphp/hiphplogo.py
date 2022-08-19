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
from hexor import *

# logo:
def logo(__version__):
    logo=""
    c_red="#ea4335"#red
    c_blue="#4285f4"#blue
    c_yellow="#fbbc05"#yellow
    c_green="#34a853"#green

    color=hexor(True,"hex")

    spas=" "*5
    code_by=color.c("Code by -> ",c_yellow)+color.c("yasserbdj96",c_green)
    logo+=color.c(f"""
{spas}             ▄███████▄    ▄█    █▄       ▄███████▄ 
{spas}            ███    ███   ███    ███     ███    ███ 
{spas}╦   ╦       ███    ███   ███    ███     ███    ███ 
{spas}║   ║ ═╦═ ▀█████████▀  ▀▀███▀▀▀▀███▀  ▀█████████▀  
{spas}╠═══╣  ║    ███          ███    ███     ███        
{spas}║   ║  ║    ███  V{__version__} ███    ███     ███ 
{spas}╩   ╩ ═╩═  ▄████▀        ███    █▀     ▄████▀ {code_by}\n""",c_red)
    logo+=color.c(" "*17+"https://github.com/yasserbdj96\n",c_blue)
    #logo+=self.color.c(" "*37+"Code by -> ",self.c_yellow)+self.color.c("yasserbdj96\n",self.c_green)
    #logo+=self.color.c("\n - You are now connected safety. You can print the PHP commands below for comprehensive control of the site.\n",self.c_blue)
    logo+=color.c("\n - '--help' for more informations.\n",c_yellow)
    logo+=color.c(" - '--exit' OR 'Ctrl+C' for exit :)\n\n",c_yellow)
    return logo
#
try:
    import sys
    from hiphpversion import __version__
    if sys.argv[1]=="ok_view":
        print(logo(__version__))
except:
    pass
#}END.
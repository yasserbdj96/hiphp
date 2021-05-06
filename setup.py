#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com
#s
import os
from os import path
from setuptools import setup,find_packages
from hiphp.__version__ import __version__,__name__,__author__,__author_email__,__description__,__Author_WebSite__,__Source_Code__,__keywords__,__install_requires__,__license__,__copyright__,__README_MD__title__,__README_MD__description__,__README_MD__Installation__,__README_MD__changelog__,__travis__install__,__travis__script__

#read:
def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()

#__version__:
f=open('version.txt','w')
f.write(f"{__version__}")
f.close()
#os.sep
#__README_MD__:
__README_MD__data=read("README.html")
if path.exists("screenshot/screenshot.png"):
    __README_MD__data=__README_MD__data.replace('{__README_MD__screenshot__}',"screenshot/screenshot.png")
else:
    __README_MD__data=__README_MD__data.replace('<p align="center">\n	<img alt="byRo0t96" align="center" src="https://raw.githubusercontent.com/byRo0t96/{__name__}/main/{__README_MD__screenshot__}">\n</p><br><br>',"")
__README_MD__data=__README_MD__data.replace('{__README_MD__title__}',__README_MD__title__)
__README_MD__data=__README_MD__data.replace('{__README_MD__description__}',__README_MD__description__)
__README_MD__data=__README_MD__data.replace('{__name__}',__name__)
__README_MD__data=__README_MD__data.replace('{__README_MD__Installation__}',"\n```\n"+__README_MD__Installation__+"\n```\n")
if path.exists("usage.py"):
    __README_MD__data=__README_MD__data.replace('{__README_MD__Usage__}',"\n```python \n"+read("usage.py")+"\n```\n")
else:
    __README_MD__data=__README_MD__data.replace('<h2>Usage:</h2>\n{__README_MD__Usage__}',"")
if path.exists("examples"):
    __README_MD__Examples__=""
    for file in os.listdir("examples"):
        if file.endswith(".py"):
            __README_MD__Examples__=__README_MD__Examples__+"\n```python\n"+read(os.path.join("examples",file))+"\n```\n\n"
    __README_MD__data=__README_MD__data.replace('{__README_MD__Examples__}',__README_MD__Examples__)
else:
    __README_MD__data=__README_MD__data.replace('<h2>Examples:</h2>\n{__README_MD__Examples__}',"")
    
changelog=""
for i in range(len(__README_MD__changelog__)):
    changelog=changelog+__README_MD__changelog__[i]+"\n\n"
__README_MD__data=__README_MD__data.replace('{__README_MD__changelog__}',changelog)
r=open('README.md','w')
r.write(__README_MD__data)
r.close()

#changelog:
c=open('changelog.txt','w')
c.write(changelog)
c.close()

#.travis:
__travis__data=read("travis.txt")
t_install=""
for i in range(len(__travis__install__)):
    t_install=t_install+"  - "+__travis__install__[i]+"\n"
__travis__data=__travis__data.replace('{__travis__install__}',t_install)

t_script=""
for i in range(len(__travis__script__)):
    t_script=t_script+"  - "+__travis__script__[i]+"\n"
__travis__data=__travis__data.replace('{__travis__script__}',t_script)

t=open('travis.yml','w')
t.write(__travis__data)
t.close()

# Setting up:
setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__description__,
    long_description_content_type="text/markdown",
    long_description=read("README.md"),
    license=__license__,
    packages=find_packages(),
    project_urls={
        'Author WebSite':__Author_WebSite__,
        'Source Code':__Source_Code__,
    },
    install_requires=__install_requires__,
    keywords=__keywords__,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        f"License :: OSI Approved :: {__license__}",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires=">=3.x.x"
)
#e
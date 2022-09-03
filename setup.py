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
from setuptools import setup,find_packages

setup(
    name="hiphp",
    version=__version__,
    author="yasserbdj96",
    author_email="yasser.bdj96@gmail.com",
    description='''hiphp - free & open source project for create a BackDoor to control php-based sites In the normal internet or sites in The Onion Router (tor network).''',
    long_description_content_type="text/markdown",
    long_description=open('README.md','r', encoding="utf8").read(),
    license='''MIT License''',
    packages=find_packages(),
    project_urls={
        'Source': "https://github.com/yasserbdj96/hiphp",
        'Documentation': "https://yasserbdj96.github.io/hiphp",
        'Chat': "https://gitter.im/yasserbdj96/hiphp",
        'WebSite':"https://yasserbdj96.github.io/"
    },
    install_requires=["requests","hexor","biglibrary"],
    keywords=["windows","macos","linux","docker","cli","php","http","remoteaccess","backdoor","controller","https","hacking","python3","onion","termux","payload","website-hacking","yasserbdj96","revisioncontrol","hiphp"],
    classifiers=[
        "Environment :: Web Environment",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP"
    ],
    python_requires=">=3.x.x"
)
#}END.
#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com 
#s
from setuptools import setup, find_packages

# Setting up
setup(
    name="hiphp",
    version=open('version.txt').read(),
    author="Yasser BDJ (Ro0t96)",
    author_email="by.root96@gmail.com",
    description='A package for controlling a php-based website.',
    long_description_content_type="text/markdown",
    long_description=open('README.rst').read(),
    packages=find_packages(),
    project_urls={  # Optional
        'Author WebSite': "https://byro0t96.github.io/",
        'Author Github': "https://github.com/byRo0t96",
        'Source Code': 'https://github.com/byRo0t96/hiphp',
    },
    install_requires=['requests','ashar','hexor'],
    keywords=['python','hiphp','php','cli'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
#e
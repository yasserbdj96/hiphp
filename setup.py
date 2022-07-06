#!/usr/bin/env python
# coding:utf-8
# code by : yasserbdj96
# email : yasser.bdj96@gmail.com

#START{
from setuptools import setup,find_packages
setup(
    name="hiphp",
    version="0.2.18",
    author="yasserbdj96",
    author_email="yasser.bdj96@gmail.com",
    description='''hiphp is BackDoor to control php-based sites hiphp can be controlled by sending commands, files, and tokens to the site using the http/https protocol. After copying the code and placing it in any php file on the target website, you will have permissions to enter it, read all files, delete and even upload new files to it. Also, this back door is password protected.''',
    long_description_content_type="text/markdown",
    long_description=open('README.md','r').read(),
    license='''MIT License''',
    packages=find_packages(),
    project_urls={
        'Source Code': "https://github.com/yasserbdj96/hiphp",
        'Author WebSite': "https://yasserbdj96.github.io/",
        'Instagram': "https://www.instagram.com/yasserbdj96/",
    },
    install_requires=["ashar","requests","hexor","asciitext"],
    keywords=['yasserbdj96', 'python', 'hiphp', 'php', 'backdoor.', 'http/https'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Topic :: Communications :: Email'
    ],
    python_requires=">=3.x.x"
)
#}END.
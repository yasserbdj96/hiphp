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
from setuptools import setup,find_packages

setup(
    name="hiphp",
    version=__version__,
    author="yasserbdj96",
    author_email="yasser.bdj96@gmail.com",
    description='''hiphp - free & open source project for create a BackDoor to control PHP-based sites.''',
    long_description_content_type="text/markdown",
    long_description=open('README_PYPI.md','r', encoding="utf8").read(),
    license='''MIT License''',
    packages=find_packages(),
    url='https://github.com/yasserbdj96/hiphp',
    project_urls={
        'Source': "https://github.com/yasserbdj96/hiphp",
        'WebSite': "https://yasserbdj96.github.io/hiphp",
        'Documentation': "https://yasserbdj96.github.io/hiphp",
        'Chat': "https://gitter.im/yasserbdj96/hiphp",
        'Author WebSite':"https://yasserbdj96.github.io/",
        'Sponsor': "https://github.com/sponsors/yasserbdj96"
    },
    #required_by=['example_package'],
    install_requires=["requests","hexor","BeautifulSoup4"],
    keywords = ["HIPHP BackDoor", "Open-source tool", "Remote control", "PHP programming", "HTTP/HTTPS protocol", "POST/GET method", "Port 80", "File download", "File editing", "Tor networks", "Password protection", "Webmasters", "Third-party software", "User-friendly", "Access rights", "Directory structure", "Flexibility", "Security", "Compatibility", "Content management"],
    classifiers=[
        "Environment :: Web Environment",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP"
    ],
    #python_requires=">=3.9"
)
#}END.

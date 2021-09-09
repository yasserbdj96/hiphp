from setuptools import setup,find_packages
setup(
    name="hiphp",
    version="0.1.13",
    author="Yasser Bdj (Boudjada Yasser)",
    author_email="yasser.bdj96@gmail.com",
    description='''backdoor control php sites, The site is controlled by sending commands, files and codes to the site using the http or https protocol. After copying the code and placing it in any php file on the target website, you will have permissions to enter it, read all files, delete and even upload new files to it. Also, this backdoor is password protected and non-reverse encryption.''',
    long_description_content_type="text/markdown",
    long_description=open('README.md','r').read(),
    license='''MIT License''',
    packages=find_packages(),
    url="https://github.com/yasserbdj96/hiphp",
    project_urls={
        'Author WebSite': "https://yasserbdj96.github.io/",
    },
    install_requires=['pipincluder'],
    keywords=['yasserbdj96', 'python', 'hiphp', 'for', 'control', 'php', 'websites.', 'backdoor', 'control', 'php', 'sites,', 'The', 'site', 'is', 'controlled', 'by', 'sending', 'commands,', 'files', 'and', 'codes', 'to', 'the', 'site', 'using', 'the', 'http', 'or', 'https', 'protocol.', 'After', 'copying', 'the', 'code', 'and', 'placing', 'it', 'in', 'any', 'php', 'file', 'on', 'the', 'target', 'website,', 'you', 'will', 'have', 'permissions', 'to', 'enter', 'it,', 'read', 'all', 'files,', 'delete', 'and', 'even', 'upload', 'new', 'files', 'to', 'it.', 'Also,', 'this', 'backdoor', 'is', 'password', 'protected', 'and', 'non-reverse', 'encryption.'],
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
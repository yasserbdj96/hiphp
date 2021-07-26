from setuptools import setup,find_packages
setup(
    name="hiphp",
    version="0.1.10",
    author="Yasser Bdj (Boudjada Yasser)",
    author_email="yasser.bdj96@gmail.com",
    description='''A package for controlling a php-based website.''',
    long_description_content_type="text/markdown",
    long_description=open('README.md','r').read(),
    license='''MIT License''',
    packages=find_packages(),
    url="https://github.com/yasserbdj96/hiphp",
    project_urls={
        'Author WebSite': "https://yasserbdj96.github.io/",
    },
    install_requires=['pipincluder', 'requests', 'ashar', 'hexor'],
    keywords=['yasserbdj96', 'python', 'hiphp', 'for', 'control', 'php', 'websites.', 'A', 'package', 'for', 'controlling', 'a', 'php-based', 'website.'],
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
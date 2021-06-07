from setuptools import setup,find_packages
setup(
    name="hiphp",
    version="0.1.9",
    author="Yasser BDJ (Ro0t96)",
    author_email="by.root96@gmail.com",
    description='''A package for controlling a php-based website.''',
    long_description_content_type="text/markdown",
    long_description=open('README.md','r').read(),
    license="Apache Software License",
    packages=find_packages(),
    url="https://github.com/byRo0t96/hiphp",
    project_urls={
        'Author WebSite': "https://byro0t96.github.io/",
    },
    install_requires=['pipincluder', 'requests', 'ashar', 'hexor'],
    keywords=['python', 'hiphp', 'php', 'cli'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires=">=3.x.x"
)
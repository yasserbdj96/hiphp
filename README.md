<img align="right" height="250" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/install/hiphp.png" alt="hiphp by yasserbdj96">
<h1>hiphp for control php websites.</h1>
<p>hiphp is BackDoor to control php-based sites hiphp can be controlled by sending commands, files, and tokens to the site using the http/https protocol. After copying the HIPHP_HOLE_CODE and placing it in any php file on the target website, you will have permissions to enter it, read all files, delete and even upload new files to it. Also, this back door is password protected.</p>

[![Python package](https://github.com/yasserbdj96/hiphp/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/yasserbdj96/hiphp/actions/workflows/python-app.yml) [![Docker image](https://github.com/yasserbdj96/hiphp/actions/workflows/docker-image.yml/badge.svg)](https://github.com/yasserbdj96/hiphp/actions/workflows/docker-image.yml) [![CodeFactor](https://www.codefactor.io/repository/github/yasserbdj96/hiphp/badge)](https://www.codefactor.io/repository/github/yasserbdj96/hiphp) [![pages-build-deployment](https://github.com/yasserbdj96/hiphp/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/yasserbdj96/hiphp/actions/workflows/pages/pages-build-deployment) [![Visitors](https://visitor-badge.laobi.icu/badge?page_id=yasserbdj96.hiphp)](https://github.com/yasserbdj96/hiphp)

<h2>You can use this version of the project as:</h2>
[✓] Command line interface CLI.<br>
[✓] Graphical user interface GUI (beta).<br>
[✓] Python Module.<br>
[✓] Script.<br>
[✓] Container.

<h2>Languages:</h2>
* python3<br>
* php

<h2>Requirements</h2>
[✓] ashar<br>
[✓] requests<br>
[✓] hexor<br>
[✓] asciitext

<h2>Supported Distributions:</h2>

| Distribution     | Version Check | Python Test Version       | Supported | Status    | Everything works |
| :--------------: | :-----------: | :-----------------------: | :-------: | :-------: | :--------------: |
| Ubuntu           | 20.04.4       | 3.6, 3.7, 3.8, 3.9, 3.10  | Yes       | Working   | Yes              |
| Windwos          | 10.0.20348    | 3.6, 3.7, 3.8, 3.9, 3.10  | Yes       | Working   | Yes              |
| MacOS            | 11.6.6        | 3.6, 3.7, 3.8, 3.9, 3.10  | Yes       | Working   | Yes              |
| Android (termux) | 10            | 3.6, 3.7, 3.8, 3.9, 3.10  | Yes       | Working   | Yes              |
| Android (nethunter)| 10 (2022.3) | 3.6, 3.7, 3.8, 3.9, 3.10  | Yes       | Working   | Yes              |

<h2>Docker pull,build & run:</h2>

```bash
# pull:
>>> docker pull yasserbdj96/hiphp:latest

# build:
>>> docker build -t docker.io/yasserbdj96/hiphp:latest .

# run:
>>> docker run -e KEY="<KEY>" -e URL="<URL>" -i -t docker.io/yasserbdj96/hiphp:latest
```

<h2>Github Packages pull,build & run:</h2>

```bash
# pull:
>>> docker pull ghcr.io/yasserbdj96/hiphp:latest

# build:
>>> docker build -t ghcr.io/yasserbdj96/hiphp:latest .

# run:
>>> docker run -e KEY="<KEY>" -e URL="<URL>" -i -t ghcr.io/yasserbdj96/hiphp:latest
```

<h2>Python Package Installation:</h2>

```
# install from pypi:
>>> pip install hiphp

# local install:
>>> git clone https://github.com/yasserbdj96/hiphp.git
>>> cd hiphp
>>> sudo python setup.py install

# uninstall:
>>> pip uninstall hiphp
```

<h2>Ubuntu Installation:</h2>

```
# install:
>>> git clone https://github.com/yasserbdj96/hiphp.git
>>> pip install -r hiphp/requirements.txt
>>> cd hiphp/install
>>> bash install.sh -i
>>> hiphp

# update:
>>> cd hiphp/install
>>> bash install.sh -up

# uninstall:
>>> cd hiphp/install
>>> bash install.sh -u
```

<h2>Run without installation:</h2>

```
>>> git clone https://github.com/yasserbdj96/hiphp.git
>>> cd hiphp
>>> pip install -r requirements.txt
>>> python3 run.py <KEY> <URL>
```

<h2>Script Usage:</h2>

```python
from hiphp import *

# connect:
p1=hiphp(key="<KEY>",url="<URL>")
```

<h2>Script Examples:</h2>

```python
#START{
from hiphp import *

# connect:
p1=hiphp(key="123",url="http://127.0.0.1/index.php")#Default: retu=False.
#p1=hiphp(key="123",url="http://kfdjlkgjflkgjdfkjgkfdjgkjdfkgjk.onion/index.php")
#p1=hiphp(key="123",url="https://google.com/index.php")

# Get the hole Code:
p1.get_hole()# Copy this code into the file whose path you entered earlier. ex: https://localhost/index.php

# Example:1
# Command:
p1.run("echo 'this is a test';")

# Example:2
# Run code from file:
p1.run_file("./examples.php")# Run code from file.
p1.run_file("./examples.php","var1==true","var2==hiii")# Run code from file With the entry of variables.

# Example:3
# Upload a file:
p1.upload("./examples.php")# Upload a file to the current directory.
p1.upload("./examples.php","./upload_path/")# Upload a file to a specific directory.

# Example:4
# Command line interface:
p1.cli()
#}END.
```

<h2>Screenshot:</h2>

<div align="center">
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot.png" alt="hiphp by yasserbdj96">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot0.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot0.png" alt="hiphp by yasserbdj96">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot1.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot1.png" alt="hiphp by yasserbdj96">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot2.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot2.png" alt="hiphp by yasserbdj96">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/scripts/hiphp_ftp/screenshot/screenshot.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/scripts/hiphp_ftp/screenshot/screenshot.png" alt="hiphp by yasserbdj96">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/scripts/hiphp_desktop/screenshot/screenshot.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/scripts/hiphp_desktop/screenshot/screenshot.png" alt="hiphp by yasserbdj96">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/scripts/hiphp_desktop/screenshot/screenshot1.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/scripts/hiphp_desktop/screenshot/screenshot1.png" alt="hiphp by yasserbdj96">
    </a>
</div>

<h2>Changelog History:</h2>

```
## 0.2.21 [18-08-2022]
 - Fix not being able to install internally on Nethunter.
 - Fix some issues in uploading files.
 - Add Update option.
 - Bug fixes & performance improvements.

## 0.2.20 [10-08-2022]
 - Change the display of files in the command "--ls"
 - Fix "HIPHP_HOLE_CODE".
 - Add "--cls" to clear console.
 - Slight change to the command line interface logo.
 - Bug fixes & performance improvements.

## 0.2.19 [30-07-2022]
 - Preparing for the new version.
 - Rework the software rights with the addition of the Bitcoin wallet address.
 - new logo design.
 - Bug fixes & performance improvements.

## 0.2.18 [06-07-2022]
 - Bug fixes & performance improvements.

## 0.2.17 [03-07-2022]
 - Bug fixes on windows os.

## 0.2.16 [02-07-2022]
 - Bug fixes & performance improvements.

## 0.2.15 [22-06-2022]
 - New build.
 - More stability.
 - Command interface update.
 - More commands.
 - Giving access to .onion sites.
 - help menu update.
 - Bug fixes & performance improvements.

## 0.1.14
 - help menu update.
 - Bug fixes & performance improvements.

## 0.1.13
 - Safety upgrade.
 - Bug fixes & performance improvements.

## 0.1.12
 - Safety upgrade.
 - Bug fixes & performance improvements.

## 0.1.11
 - Command interface update.
 - Bug fixes & performance improvements.

## 0.1.10
 - Fix Bugs.

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

<h1></h1> 



Don't forget to star ⭐ this repository
<br>

all posts [`#yasserbdj96`](#yasserbdj96) ,all views my own.

<br>
<div align="center">
    <a href="http://yasserbdj96.github.io/">Go to this link to get more information.</a>
</div>
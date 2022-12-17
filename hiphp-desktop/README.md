<h2>Run Hiphp-desktop:</h2>

```bash
# Dwonload:
❯ git clone https://github.com/yasserbdj96/hiphp.git
❯ cd hiphp

# install requirements:
❯ pip install -r requirements.txt
❯ pip install -r hiphp-desktop/requirements-dst.txt
❯ pip install -r hiphp-linux/requirements-linux.txt #for linux os.
❯ pip install -r hiphp-win/requirements-win.txt #for windows os.

# run with hiphp-desktop tool:
❯ cd hiphp-desktop
❯ python3 main.py

# Run with Makefile:
❯ make run arg="dst" url="<URL>" key="<KEY>"

# For Linux:
cd hiphp-linux
❯ bash run-hiphp-desktop.sh

# For Windows:
# Do not forget to modify the "config.ini" file or use the following command:
# > python -c "import sys; open('config.ini','w+').write('python_default_path='+sys.executable)"
# OR Run 'hiphp-win\config-configure.py'.
cd hiphp-win
❯ run-hiphp-desktop.bat

# OR if you installed it on Ubuntu:
❯ hiphp --dst
```

<br>
<h2>Screenshots:</h2>

<div align="center">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot5.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot5.png" alt="hhiphp-desktop login">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot6.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot6.png" alt="hiphp-desktop">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot7.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot7.png" alt="hiphp-desktop editor">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot8.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot8.png" alt="hiphp-desktop login dark mode">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot9.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot9.png" alt="hiphp-desktop dark mode">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot10.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot10.png" alt="hiphp-desktop editor dark mode">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot11.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot11.png" alt="hiphp-desktop settings">
    </a>
</div>

<br>
<h2>Changelog History:</h2>

<details>
  <summary>Click to See changelog History</summary>

```
## 0.2.2 [18-11-2022][Last Version]
 - Bug fixes & performance improvements.
```

</details>
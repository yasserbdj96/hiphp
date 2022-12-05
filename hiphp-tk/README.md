<h2>Run Hiphp-tk:</h2>

```bash
# Dwonload:
❯ git clone https://github.com/yasserbdj96/hiphp.git
❯ cd hiphp

# install requirements:
❯ pip install -r requirements.txt
❯ pip install -r hiphp-tk/requirements-tk.txt
❯ pip install -r requirements-linux.txt #for linux os.
❯ pip install -r requirements-win.txt #for windows os.
# OR
❯ bash install_all_requirements_linux.sh #for linux os.
# OR
❯ install_all_requirements_win.bat #for windows os.

# run with hiphp-tk tool:
❯ cd hiphp-tk
❯ python3 main.py

# Run with Makefile:
❯ make run arg="tk" url="<URL>" key="<KEY>"

# For Linux:
❯ bash run-hiphp-tk.sh

# For Windows:
# Do not forget to modify the "config.ini" file or use the following command:
# > python -c "import sys; open('config.ini','w+').write('python_default_path='+sys.executable)"
# OR Run 'configure-config-file-for-windows.py'.
❯ run-hiphp-tk.bat

# OR if you installed it on Ubuntu:
❯ hiphp --tk
#OR
❯ hiphp --tk <KEY> <URL>
```

<br>
<h2>Screenshots:</h2>

<div align="center">
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot12.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot12.png" alt="hiphp-tk login">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot13.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot13.png" alt="hiphp-tk">
    </a>
</div>

<br>
<h2>Changelog History:</h2>

<details>
  <summary>Click to See changelog History</summary>

```
## 1.1.9 [18-11-2022][Last Version]
 - Add login window on "hiphp-tk".
 - Bug fixes & performance improvements.
```

</details>
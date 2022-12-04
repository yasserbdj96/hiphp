<h2>Run Hiphp-tk:</h2>

```bash
# Download & install requirements:
❯ git clone https://github.com/yasserbdj96/hiphp.git
❯ cd hiphp
❯ bash install_all_requirements_linux.sh #for linux os.
❯ install_all_requirements_win.bat # for windows os.

# Run with Makefile:
❯ make run arg="tk" url="<URL>" key="<KEY>"

# on linux:
❯ bash run-hiphp-tk.sh

# on windows:
# In case you encounter some errors on Windows os:
# You must enter the installation path of your Python program in the "config.ini" file or use this command -->python -c "import sys; open('config.ini', 'w+').write('python_default_path='+sys.executable)"
❯ run-hiphp-tk.bat

# Or if you install it on Ubuntu:
❯ hiphp --tk
#OR
❯ hiphp --tk <KEY> <URL>
```

<br>
<h2>Screenshots:</h2>

<div align="center">
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot12.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot12.png" alt="hiphp by yasserbdj96">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot13.png">
        <img height="100" src="https://raw.githubusercontent.com/yasserbdj96/hiphp/main/screenshot/screenshot13.png" alt="hiphp by yasserbdj96">
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
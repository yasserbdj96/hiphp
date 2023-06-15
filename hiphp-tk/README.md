<h2>Run Hiphp-tk:</h2>

```bash
# Download hiphp from github:
❯ git clone https://github.com/yasserbdj96/hiphp.git
# OR
# Download hiphp from gitlab:
❯ git clone https://gitlab.com/yasserbdj96/hiphp.git

# Go to downloaded folder:
❯ cd hiphp

# install requirements:
❯ pip install -r requirements.txt
❯ pip install -r hiphp-linux/requirements-linux.txt #for linux os.
❯ pip install -r hiphp-win/requirements-win.txt #for windows os.

# run with hiphp-tk tool:
❯ python main.py --TK

# Run with Makefile:
❯ make ARGUMENTS="--TK" run
# OR
❯ make ARGUMENTS="--TK --KEY='<KEY>' --URL='<URL>'" run

# For Linux:
❯ cd hiphp-linux
❯ bash run-hiphp-tk.sh

# For Windows:
# Do not forget to modify the "config.ini" file or use the following command:
# > python -c "import sys; open('config.ini','w+').write('python_default_path='+sys.executable)"
# OR Run 'hiphp-win\config-configure.py'.
❯ hiphp-win
❯ run-hiphp-tk.bat
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
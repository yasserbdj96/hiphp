<h2>Installation:</h2>
<h4>A- Python Package Installation:</h4>

```bash
# Install from pypi:
❯ pip install hiphp
# OR
❯ python -m pip install hiphp

# Local install:
❯ git clone https://github.com/yasserbdj96/hiphp.git
❯ cd hiphp
❯ pip install -r requirements-pypi.txt
❯ sudo python setup.py install

# Uninstall:
❯ pip uninstall hiphp
```

<h4>B- Ubuntu Installation:</h4>

```bash
# Dwonload:
❯ git clone https://github.com/yasserbdj96/hiphp.git

# Go to Installation folder:
❯ cd hiphp/install

# Install:
❯ bash install.sh -i
❯ hiphp

# Update:
❯ bash install.sh -up

# Usage:
#      hiphp [OPTION]
#      hiphp --help                --> hiphp cli help.
#      hiphp --geth [KEY] [URL]    --> Get the HIPHP_HOLE_CODE Encrypted by your [KEY].
#      hiphp [KEY] [URL]           --> Connect to the victim's website (CLI) Mode.
#      hiphp --tk                  --> Run hiphp with 'hiphp-tk' (GUI) Mode.
#      hiphp --dst                 --> Run hiphp with 'hiphp-desktop' (GUI) Mode.
#      hiphp --version             --> Get the version number you are working with.

# Uninstall:
❯ bash install.sh -u
```

<h4>C- Termux Installation:</h4>

```bash
# Dwonload:
❯ git clone https://github.com/yasserbdj96/hiphp.git

# Go to Installation folder:
❯ cd hiphp/install

# Install:
❯ bash install.sh -ti
❯ hiphp

# Update:
❯ bash install.sh -tup

# Usage:
#      hiphp [OPTION]
#      hiphp --help                --> hiphp cli help.
#      hiphp --geth [KEY] [URL]    --> Get the HIPHP_HOLE_CODE Encrypted by your [KEY].
#      hiphp [KEY] [URL]           --> Connect to the victim's website (CLI) Mode.
#      hiphp --version             --> Get the version number you are working with.

# Uninstall:
❯ bash install.sh -tu
```
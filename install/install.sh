#!/bin/bash
#   |                                                         |   #
# --+---------------------------------------------------------+-- #
#   |    Code by: yasserbdj96                                 |   #
#   |    Email: yasser.bdj96@gmail.com                        |   #
#   |    GitHub: github.com/yasserbdj96                       |   #
#   |    Sponsor: github.com/sponsors/yasserbdj96             |   #
#   |    BTC: bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9      |   #
#   |                                                         |   #
#   |    All posts with #yasserbdj96                          |   #
#   |    All views are my own.                                |   #
# --+---------------------------------------------------------+-- #
#   |                                                         |   #

#START{
# app name:
appname="hiphp"

install() {
    #chmod +x "../$appname"
    chmod +x "$appname.sh";
    #chmod +x "install.sh"
    sudo mkdir "/usr/share/$appname";
    sudo cp -r "../$appname/." "/usr/share/$appname/$appname";
    sudo cp "../main.py" "/usr/share/$appname/$appname.py";
    sudo cp "$appname.png" "/usr/share/$appname/$appname.png";
    sudo cp "$appname.desktop" "/usr/share/applications/$appname.desktop";
    sudo cp "$appname.sh" "/usr/local/bin/$appname";
    #chmod +x "/usr/share/$appname";
    pip install -r "../requirements.txt";
    #sudo cp -r "../src/." "/usr/share/$appname/src";

    # install hiphp-tk script:
    #sudo cp "../hiphp-tk/main.py" "/usr/share/$appname/hiphp_tk.py";
    #sudo cp "../hiphp-tk/favicon.png" "/usr/share/$appname/favicon.png";
    sudo cp -r "../hiphp-tk/." "/usr/share/$appname/hiphp-tk";
    #pip install -r "../hiphp-tk/requirements-tk.txt";

    # install hiphp-desktop script:
    #sudo cp "../hiphp-desktop/main.py" "/usr/share/$appname/hiphp_desktop.py";
    sudo cp -r "../hiphp-desktop/." "/usr/share/$appname/hiphp-desktop";
    #pip install -r "../hiphp-desktop/requirements-dst.txt";

    # install linux requirements:
    pip install -r "../hiphp-linux/requirements-linux.txt"

    # run:
    clear
    hiphp
}

uninstall() {
    sudo rm -r "/usr/share/$appname";
    sudo rm "/usr/share/applications/$appname.desktop";
    sudo rm "/usr/local/bin/$appname";
}

termux_install(){
    #!/data/data/com.termux/files/usr/bin/bash
    #chmod +x ../../hiphp

    # My Termux setup

    # update, upgrade
    pkg update -y && pkg upgrade -y

    # configure storage
    termux-setup-storage

    # INSTALL SOME PROGRAMS
    for each_pac in "git" "python3"; do
        pkg install $each_pac -y
    done

    # if your device is rooted, you can install package 'tsu' to be able to use 'sudo' command, for this uncomment next command:
    #pkg install tsu

    # CONFIGURE SOME PROGRAMS

    # confifure vim
    # install monokai color scheme 
    #git clone https://github.com/sickill/vim-monokai 

    mkdir -p ${PREFIX}/share/hiphp

    cp -r "../hiphp/." "${PREFIX}/share/hiphp/hiphp";
    cp "../main.py" "${PREFIX}/share/hiphp/hiphp.py";
    cp "hiphp-termux.sh" "${PREFIX}/bin/hiphp";

    # install hiphp-desktop script:
    #sudo cp "../hiphp-desktop/main.py" "/usr/share/$appname/hiphp_desktop.py";
    #cp -r "../hiphp-desktop/." "${PREFIX}/share/hiphp/hiphp-desktop";
    #pip install -r "../hiphp-desktop/requirements-dst.txt";

    # install linux requirements:
    pip install -r "../hiphp-linux/requirements-linux.txt"

    #cp -r *.sh ${PREFIX}/bin
    pip install -r "../requirements.txt";

    #mv ../colors/monokai.vim ~/.vim/colors && rm -rf vim-monokai/

    # upgrade pip and install some modules
    #pip install --upgrade pip
    #pip install setuptools
    #pip install requests

    # MORE
    # remove Termux welcome text
    #rm /data/data/com.termux/files/usr/etc/motd

    clear
    echo "Termux setup complete!"
    chmod +x /data/data/com.termux/files/usr/bin/hiphp
    clear
    hiphp
    #exit 0
}

termux_uninstall(){
    rm -rf "${PREFIX}/share/hiphp";
    #rm "${PREFIX}/share/hiphp.py";
    rm "${PREFIX}/bin/hiphp";
}

# Default values
install=false
uninstall=false
update=false
termux=false

# Parse the command-line arguments
for arg in "$@"; do
  case "$arg" in
    --install|--INSTALL|--i|--I)
      install=true
      ;;
    --uninstall|--UNINSTALL|--u|--U)
      uninstall=true
      ;;
    --update|--UPDATE|--up|--UP)
      update=true
      ;;
    --termux|--TERMUX|--t|--T)
      termux=true
      ;;
    *)
      echo "Invalid argument: $arg" >&2
      exit 1
      ;;
  esac
done

# install:
if [ "$install" = true ]; then
    if [ "$termux" = true ]; then
        termux_install
    else
        install
    fi

# uninstall:
elif [ "$uninstall" = true ]; then
    if [ "$termux" = true ]; then
        termux_uninstall
    else
        uninstall
    fi

# update:
elif [ "$update" = true ]; then
    if [ "$termux" = true ]; then
        termux_uninstall
        termux_install
    else
        uninstall
        install
    fi

# usage:
else
    echo "Usage: bash $0 [OPTION]"
    echo "Options:"
    echo "    --install      # Install the program."
    echo "    --uninstall    # Uninstall the program."
    echo "    --update       # Update the program."
    echo "    --termux       # Enable termux operations."
fi
#}END.

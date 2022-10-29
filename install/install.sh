#!/bin/bash
#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

#START{
# app name:
appname="hiphp"

install() {
    chmod +x "$appname.sh";
    sudo mkdir "/usr/share/$appname";
    sudo cp -r "../$appname/." "/usr/share/$appname/$appname";
    sudo cp "$appname.py" "/usr/share/$appname/$appname.py";
    sudo cp "$appname.png" "/usr/share/$appname/$appname.png";
    sudo cp "$appname.desktop" "/usr/share/applications/$appname.desktop";
    sudo cp "$appname.sh" "/usr/local/bin/$appname";
    pip install -r "../requirements.txt";
    #sudo cp -r "../src/." "/usr/share/$appname/src";

    # install hiphp-tk script:
    #sudo cp "../hiphp-tk/main.py" "/usr/share/$appname/hiphp_tk.py";
    #sudo cp "../hiphp-tk/favicon.png" "/usr/share/$appname/favicon.png";
    sudo cp -r "../hiphp-tk/." "/usr/share/$appname/hiphp-tk";
    pip install -r "../hiphp-tk/requirements-tk.txt";

    # install hiphp-desktop script:
    #sudo cp "../hiphp-desktop/main.py" "/usr/share/$appname/hiphp_desktop.py";
    sudo cp -r "../hiphp-desktop/." "/usr/share/$appname/hiphp-desktop";
    pip install -r "../hiphp-desktop/requirements-dst.txt";
}

uninstall() {
    sudo rm -r "/usr/share/$appname";
    sudo rm "/usr/share/applications/$appname.desktop";
    sudo rm "/usr/local/bin/$appname";
}

termux_install(){
    #!/data/data/com.termux/files/usr/bin/bash

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

    cp -r "../hiphp/." "${PREFIX}/share/hiphp";
    cp "hiphp.py" "${PREFIX}/share/";
    cp "hiphp-termux.sh" "${PREFIX}/bin/hiphp";


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
    hiphp
    #exit 0
}

termux_uninstall(){
    rm -rf "${PREFIX}/share/hiphp";
    rm "${PREFIX}/share/hiphp.py";
    rm "${PREFIX}/bin/hiphp";
}

# install:
if [ "$1" == "-i" ] ; then
    install

# uninstall:
elif [ "$1" == "-u" ] ; then
    uninstall

# update:
elif [ "$1" == "-up" ] ; then
    uninstall
    install

# termux_install:
elif [ "$1" == "-ti" ] ; then
    termux_install

# termux_uninstall:
elif [ "$1" == "-tu" ] ; then
    termux_uninstall

# termux_update:
elif [ "$1" == "-tup" ] ; then
    termux_uninstall
    termux_install

# usage:
else
    echo "Usage: bash $0 [OPTION]";
    echo "       -i   | # for install.";
    echo "       -u   | # for uninstall.";
    echo "       -up  | # for update.";
    echo "       -ti  | # for install hiphp on termux.";
    echo "       -tu  | # for uninstall hiphp from termux.";
    echo "       -tup | # for update hiphp on termux.";
fi
#}END.

#!/bin/bash
# code by : yasserbdj96
# email : yasser.bdj96@gmail.com

#START{
# app name:
appname="hiphp"

# install:
if [ "$1" == "-i" ] ; then
    chmod +x "$appname.sh";
    sudo mkdir "/usr/share/$appname";
    sudo cp -r "../$appname/." "/usr/share/$appname/$appname";
    sudo cp "$appname.py" "/usr/share/$appname/$appname.py";
    sudo cp "$appname.png" "/usr/share/$appname/$appname.png";
    sudo cp "$appname.desktop" "/usr/share/applications/$appname.desktop";
    sudo cp "$appname.sh" "/usr/local/bin/$appname";

    # install hiphp_ftp script:
    sudo cp "../scripts/hiphp_ftp/main.py" "/usr/share/$appname/hiphp_ftp.py";
    sudo cp "../scripts/hiphp_ftp/favicon.png" "/usr/share/$appname/favicon.png";
    pip install -r "../scripts/hiphp_ftp/requirements.txt";

    # install hiphp_desktop script:
    sudo cp "../scripts/hiphp_desktop/main.py" "/usr/share/$appname/hiphp_desktop.py";
    sudo cp -r "../scripts/hiphp_desktop/src/." "/usr/share/$appname/src";
    pip install -r "../scripts/hiphp_desktop/requirements.txt";

# uninstall:
elif [ "$1" == "-u" ] ; then
    sudo rm -r "/usr/share/$appname";
    #sudo rm "/usr/share/$appname/$appname.png";
    sudo rm "/usr/share/applications/$appname.desktop";
    sudo rm "/usr/local/bin/$appname";
# usage:
else
    echo "Usage: bash $0 [OPTION]";
    echo "       -i   | # for install.";
    echo "       -u   | # for uninstall.";
fi
#}END.

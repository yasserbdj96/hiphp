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
#help:
if [ -z "$1" ]; then
    python3 "/usr/share/hiphp/hiphp/hiphplogo.py" "ok_view";
    echo "Usage: hiphp [OPTION]";
    echo "";
    echo "ex:  hiphp --help               | # hiphp cli help.";
    echo "     hiphp --geth [KEY] [URL]   | # Get the HIPHP_HOLE_CODE Encrypted by your [KEY].";
    echo "     hiphp [KEY] [URL]          | # Connect to the victim's website (CLI) Mode.";
    echo "     hiphp --tk                 | # Run hiphp with 'hiphp-tk' (GUI) Mode.";
    echo "     hiphp --dst                | # Run hiphp with 'hiphp-desktop' (GUI) Mode.";
    echo "     hiphp --version            | # Get the version number you are working with.";

#cli help:
elif [ "$1" == "--help" ] ; then
    python3 "/usr/share/hiphp/hiphp.py" "--help";

#hiphp_tk:
elif [ "$1" == "--tk" ] ; then
    if [ -z "$2" ]; then 
        python3 "/usr/share/hiphp/hiphp-tk/main.py" "$2" "$3";
    else
        python3 "/usr/share/hiphp/hiphp-tk/main.py";
    fi

#hiphp_desktop:
elif [ "$1" == "--dst" ] ; then
    python3 "/usr/share/hiphp/hiphp-desktop/main.py";

#version:
elif [ "$1" == "--version" ] ; then
    python3 "/usr/share/hiphp/hiphp.py" "--version";

#cli:
else
    if [ "$1" == "--geth" ] ; then
        python3 "/usr/share/hiphp/hiphp.py" $1 $2 $3;
    else
        python3 "/usr/share/hiphp/hiphp.py" $1 $2;
    fi
fi
#}END.

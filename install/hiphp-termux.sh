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
    python3 "${PREFIX}/share/hiphp/hiphplogo.py" "ok_view";
    echo "Usage: hiphp [OPTION]";
    echo "";
    echo "# hiphp --help                      = hiphp cli help.";
    echo "# hiphp --geth [KEY*] [URL*] [LANG] = Get the HIPHP_HOLE_CODE Encrypted by your [KEY].";
    echo "# hiphp [KEY*] [URL*] [LANG]        = Connect to the victim's website (CLI) Mode.";
    echo "# hiphp --version                   = Get the version number you are working with.";
    echo "";
    echo "# *     = All inputs must be entered."
    echo "# KEY   = The password used for encrypt HIPHP_HOLE_CODE."
    echo "# URL   = Victim website link."
    echo "# LANG  = based site language, default LANG='php'."
#cli help:
elif [ "$1" == "--help" ] ; then
    python3 "${PREFIX}/share/hiphp.py" "--help";

#version:
elif [ "$1" == "--version" ] ; then
    python3 "${PREFIX}/share/hiphp.py" "--version";

#geth:
elif [ "$1" == "--geth" ] ; then
    if [ "$4" ] ; then
        python3 "${PREFIX}/share/hiphp.py" $1 $2 $3 $4;
    else
        python3 "${PREFIX}/share/hiphp.py" $1 $2 $3;
    fi
#cli:
else
    if [ "$3" ] ; then
        python3 "${PREFIX}/share/hiphp.py" $1 $2 $3;
    else
        python3 "${PREFIX}/share/hiphp.py" $1 $2;
    fi
fi
#}END.

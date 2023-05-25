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
cd /usr/share/hiphp/

#help:
if [ -z "$1" ]; then
    python3 "/usr/share/hiphp/hiphp/hiphplogo.py" "ok_view";
    echo "Usage: hiphp [OPTION]";
    echo "";
    echo "Examples:";
    echo "         hiphp --help                  # Show CLI help for hiphp.";
    echo "         hiphp --geth [KEY] [URL]      # Retrieve the HIPHP_HOLE_CODE encrypted by your [KEY].";
    echo "         hiphp [KEY] [URL]             # Connect to the victim's website in CLI mode.";
    echo "         hiphp --tk                    # Run hiphp in 'hiphp-tk' (GUI) mode.";
    echo "         hiphp --dst                   # Run hiphp in 'hiphp-desktop' (GUI) mode.";
    echo "         hiphp --version               # Check the current version number.";

#cli help:
elif [ "$1" == "--HELP" ] || [ "$1" == "--help" ]; then
    python3 "/usr/share/hiphp/hiphp.py" --HELP;

#hiphp_tk:
elif [ "$1" == "--TK" ] || [ "$1" == "--tk" ]; then
    python3 "/usr/share/hiphp/hiphp.py" --TK;

#hiphp_desktop:
elif [ "$1" == "--DST" ] || [ "$1" == "--dst" ]; then
    python3 "/usr/share/hiphp/hiphp.py" --DST;

#version:
elif [ "$1" == "--VERSION" ] || [ "$1" == "--version" ]; then
    python3 "/usr/share/hiphp/hiphp.py" --VERSION;

#cli:
else
    if [ "$1" == "--GETH" ] || [ "$1" == "--geth" ]; then
        python3 "/usr/share/hiphp/hiphp.py" --GETH --KEY=$2 --URL=$3;
    else
        python3 "/usr/share/hiphp/hiphp.py" --KEY=$1 --URL=$2;
    fi
fi
#}END.

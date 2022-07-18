#!/bin/bash
# code by : yasserbdj96
# email : yasser.bdj96@gmail.com

#START{
#help:
if [ -z "$1" ]; then
    echo "Usage: hiphp [OPTION]";
    echo "";
    echo "ex:    hiphp --help               | # hiphp cli help.";
    echo "       hiphp --geth [KEY] [URL]   | # Get the hole Code.";
    echo "       hiphp [KEY] [URL]          | # Connect to the victim's website.";
    echo "       hiphp --ftp [KEY] [URL]    | # Run hiphp as GUI in 'hiphp_ftp' script.";
    echo "       hiphp --dst                | # Run hiphp as GUI in 'hiphp_desktop' script.";

#cli help:
elif [ "$1" == "--help" ] ; then
    python "/usr/share/hiphp/hiphp.py" "--help";

#hiphp_ftp:
elif [ "$1" == "--ftp" ] ; then
    python "/usr/share/hiphp/hiphp_ftp.py" "$2" "$3";

#hiphp_desktop:
elif [ "$1" == "--dst" ] ; then
    python "/usr/share/hiphp/hiphp_desktop.py";

#cli:
else
    if [ "$1" == "--geth" ] ; then
        python "/usr/share/hiphp/hiphp.py" $1 $2 $3;
    else
        python "/usr/share/hiphp/hiphp.py" $1 $2;
    fi
fi
#}END.
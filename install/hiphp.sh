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


# Default values
key=""
url=""
help=false
tk=false
dst=false
version=false
geth=false


# Parse the command-line arguments
for arg in "$@"; do
  case "$arg" in
    --key=*|--KEY=*)
      key=--key="${arg#*=}"
      ;;
    --url=*|--URL=*)
      url=--url="${arg#*=}"
      ;;
    --help|--HELP)
      help=true
      ;;
    --tk|--TK)
      tk=true
      ;;
    --dst|--DST)
      dst=true
      ;;
    --version|--VERSION)
      version=true
      ;;
    --geth|--GETH)
      geth=true
      ;;
    --proxies=*|--PROXIES=*)
      proxies=--proxies="${arg#*=}"
      ;;
    --y|--Y)
      y=--y
      ;;
    *)
      echo "Invalid argument: $arg" >&2
      exit 1
      ;;
  esac
done

#cli help:
if [ "$help" = true ]; then
#elif [ "$1" == "--HELP" ] || [ "$1" == "--help" ]; then
    python3 "/usr/share/hiphp/hiphp.py" --HELP;

#hiphp_tk:
elif [ "$tk" = true ]; then
#elif [ "$1" == "--TK" ] || [ "$1" == "--tk" ]; then
    python3 "/usr/share/hiphp/hiphp.py" --TK;

#hiphp_desktop:
elif [ "$dst" = true ]; then
#elif [ "$1" == "--DST" ] || [ "$1" == "--dst" ]; then
    python3 "/usr/share/hiphp/hiphp.py" --DST;

#version:
elif [ "$version" = true ]; then
#elif [ "$1" == "--VERSION" ] || [ "$1" == "--version" ]; then
    python3 "/usr/share/hiphp/hiphp.py" --VERSION;

elif [ "$geth" = true ]; then
    if [ -n "$key" ] || [ -n "$url" ]; then
        python3 "/usr/share/hiphp/hiphp.py" --GETH --KEY=$2 --URL=$3;
    else
        echo "At least one variable is empty"
    fi

#help:
else
    if [ -n "$url" ] && [ -n "$key" ]; then
        python3 "/usr/share/hiphp/hiphp.py" $key $url $y $proxies;
    else
        python3 "/usr/share/hiphp/hiphp.py" --VIEWLOGO;
        echo "Usage: hiphp [OPTION]";
        echo "";
        echo "Examples:";
        echo "hiphp --help                                            # Display CLI help."
        echo "hiphp --geth --key='[KEY]' --url='[URL]'                # Retrieve encrypted HIPHP_HOLE_CODE."
        echo "hiphp --key='[KEY]' --url='[URL]'                       # Connect to the victim's website in CLI mode."
        echo "hiphp --key='[KEY]' --url='[URL]' --proxies='[PROXIES]' # Run as CLI with PROXIES"
        echo "hiphp --key='[KEY]' --url='[URL]' --y                   # Skip the confirmation."
        echo "hiphp --version                                         # Check the version."
        echo "hiphp --tk                                              # Run hiphp as a GUI application.";
        echo "hiphp --dst                                             # Run hiphp as a web application.";
    fi
fi
#}END.

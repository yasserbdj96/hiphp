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
cd ..

# Default values
key=""
url=""

# Parse the command-line arguments
for arg in "$@"; do
  case "$arg" in
    --key=*)
      key="${arg#*=}"
      ;;
    --KEY=*)
      key="${arg#*=}"
      ;;
    --url=*)
      url="${arg#*=}"
      ;;
    --URL=*)
      url="${arg#*=}"
      ;;
    *)
      echo "Invalid argument: $arg" >&2
      exit 1
      ;;
  esac
done

python3 main.py --key="$key" --url="$url"
#}END.

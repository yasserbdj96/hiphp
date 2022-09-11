#!/usr/bin/env python
# coding:utf-8
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
def help(__version__,opt=""):
  #
  spsbar=""""""

  #
  header=f"""hiphp V{__version__} - (C) 2010-2022 yasserbdj96
https://github.com/yasserbdj96/hiphp

  Command                            Description
  -------                            -----------"""

  #
  OPTIONS="""
[OPTIONS]

  --help, help                       ─> # Display this help.
  --help [ACTIONS], help [ACTIONS]   ─> # Help for a specific command.
  --geth, geth                       ─> # Get the hole Code, "HIPHP_HOLE_CODE" It has the same purpose.
  --phpinfo, phpinfo                 ─> # Some information about the server.
  --cls, cls                         ─> # Clear console.
  --exit, exit                       ─> # Exit this console.
"""

  #
  ACTIONS="""
[ACTIONS]
"""

  #
  ls_c="""
  --ls, ls                           ─> # List information about the FILEs (the current directory by default).
  Usage: --ls [OPTION] [PATH], ls [OPTION] [PATH]
  Mandatory arguments to long options:
    --ls                             ─> # Get a list of all files and folders from the current directory.
    --ls [PATH]                      ─> # Get a list of all files and folders from a specified directory.
    --ls -all                        ─> # Get a list of all files, folders and subfolders from the current directory.
    --ls -all [PATH]                 ─> # Get a list of all files, folders and subfolders from a specified directory.
"""

  #
  cat_c="""
  --cat, cat                         ─> # Concatenate FILE to standard output.
  Usage: --cat [FILE_PATH]
"""

  #
  set_c="""
  --set, set                         ─> # Create a code that is always saved on during work.
  Usage: --set [PHP_CODE]
  You can return the initial value with "--dset" or "dset".
"""

  #
  cd_c="""
  --cd, cd                           ─> # Change directory.
  Usage: --cd [PATH]
"""

  #
  rf_c="""
  --rf, rf                           ─> # Run code from file.
  Usage: --rf [FILE_PATH] [VARIABLES]
  Mandatory arguments to long options:
    --rf [FILE_PATH]                 ─> # Run code from file.
    --rf [FILE_PATH] [VARIABLES]     ─> # Run code from file with variables, EX: --rf example.php var==hello
  """

  #
  up_c="""
  --up, up                           ─> # Upload a file.
  Usage: --up [FILE_PATH] [PATH]
  Mandatory arguments to long options:
    --up [FILE_PATH]                 ─> # Upload a file to the current directory.
    --up [FILE_PATH] [PATH]          ─> # Upload a file to a specified directory.
"""

  #
  down_c="""
  --down, down                       ─> # download a file.
  Usage: --down [-f/-d] [FILE/DIR_PATH] [OUT_PATH]
  Mandatory arguments to long options:
    --down -f [FILE_PATH]            ─> # Download a file to the current directory.
    --down -f [FILE_PATH] [OUT_PATH] ─> # Download file to a specified directory.
    --down -d [DIR_PATH]             ─> # Download a folder to the current directory.
    --down -d [DIR_PATH] [OUT_PATH]  ─> # Download folder to a specified directory.
    --down -all                      ─> # Download all files to the current directory.
    --down -all [OUT_PATH]           ─> # Download all files to a specified directory.
"""

  #
  zip_c="""
  --zip, zip                         ─> # Compress a directory.
  Usage: --zip [DIR_PATH]
  Mandatory arguments to long options:
    --zip                            ─> # Compress the current directory.
    --zip [DIR_PATH]                 ─> # Compress a specific directory.
"""
  #
  ABOUT="""
[ABOUT]

  --update, update                   ─> # check for updates.
  --license, license                 ─> # This project license.
  --about, about                     ─> # About this project."""
  if opt=="":
    return header+OPTIONS+ACTIONS+ls_c+spsbar+cat_c+spsbar+set_c+spsbar+cd_c+spsbar+rf_c+spsbar+up_c+spsbar+down_c+spsbar+zip_c+spsbar+ABOUT
  else:
    opt=opt.replace("--","")
    opt=opt+"_c"
    x=""
    exec(f"print({opt})")
#}END.
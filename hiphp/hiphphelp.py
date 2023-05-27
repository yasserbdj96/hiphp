#!/usr/bin/env python
# coding:utf-8
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
def help(__version__,opt=""):
  #
  spsbar=""""""

  #
  header=f"""HIPHP v{__version__} - (C) 2010-2023 yasserbdj96
GitHub: https://github.com/yasserbdj96/hiphp
"""

  #
  OPTIONS="""
Commands:

  --help, help                       # Display this help.
  --help [ACTIONS], help [ACTIONS]   # Help for a specific command.
  --geth, geth                       # Get the HIPHP_HOLE_CODE (same purpose as --geth).
  --phpinfo, phpinfo                 # Display information about the server.
  --cls, cls                         # Clear the console.
  --exit, exit                       # Exit the console.
"""

  #
  ACTIONS="""
Actions:
"""

  #
  ls_c="""
  --ls, ls                           # List files and folders (current directory by default).
  Usage: --ls [OPTION] [PATH], ls [OPTION] [PATH]
    --ls                             # List all files and folders in the current directory.
    --ls [PATH]                      # List all files and folders in the specified directory.
    --ls -all                        # List all files, folders, and subfolders in the current directory.
    --ls -all [PATH]                 # List all files, folders, and subfolders in the specified directory.
"""

  #
  cat_c="""
  --cat, cat                         # Concatenate a file to standard output.
  Usage: --cat [FILE_PATH]
"""

  #
  set_c="""
  --set, set                         # Create a code snippet that is always saved during work.
  Usage: --set [PHP_CODE]
  To reset to the initial value, use "--dset" or "dset".
"""

  #
  cd_c="""
  --cd, cd                           # Change directory.
  Usage: --cd [PATH]
"""

  #
  rf_c="""
  --rf, rf, run                      # Run code from a file.
  Usage: --rf [FILE_PATH] [VARIABLES]
    --rf [FILE_PATH]                 # Run code from a file.
    --rf [FILE_PATH] [VARIABLES]     # Run code from a file with variables (e.g., --rf example.php var==hello).
  """

  #
  up_c="""
  --up, up, upload                   # Upload a file.
  Usage: --up [FILE_PATH] [PATH]
    --up [FILE_PATH]                 # Upload a file to the current directory.
    --up [FILE_PATH] [PATH]          # Upload a file to a specified directory.
"""

  #
  down_c="""
  --down, down, download             # Download a file.
  Usage: --down [-f/-d] [FILE/DIR_PATH] [OUT_PATH]
    --down -f [FILE_PATH]            # Download a file to the current directory.
    --down -f [FILE_PATH] [OUT_PATH] # Download a file to a specified directory.
    --down -d [DIR_PATH]             # Download a folder to the current directory.
    --down -d [DIR_PATH] [OUT_PATH]  # Download a folder to a specified directory.
    --down -all                      # Download all files to the current directory.
    --down -all [OUT_PATH]           # Download all files to a specified directory.
"""

  #
  zip_c="""
  --zip, zip                         # Compress a directory.
  Usage: --zip [DIR_PATH]
    --zip                            # Compress the current directory.
    --zip [DIR_PATH]                 # Compress a specific directory.
"""

#
  edt_c="""
  --edt, edt, edit                   # Edit files.
  Usage: --edt [FILE_PATH]
    CTRL+q                           # Exit the editor.
    CTRL+s                           # Save the changes.
"""

#
  rm_c="""
  --rm, rm, delete                   # Delete files and folders.
  Usage: --rm [-f/-d] [FILE/DIR_PATH]
    --rm -f [FILE_PATH]              # Delete a file.
    --rm -d [DIR_PATH]               # Delete a folder.
"""

#
  mv_c="""
  --mv, mv                           # Move files and folders.
  Usage: --mv [SOURCE] [DESTINATION]
"""

  #
  ABOUT="""
About:

  --update, update                   # Check for updates.
  --license, license                 # View the project license.
  --about, about                     # About this project.
  --version, version                 # Get the current version number."""

  if opt=="":
    return header+OPTIONS+ACTIONS+ls_c+spsbar+cat_c+spsbar+set_c+spsbar+cd_c+spsbar+rf_c+spsbar+up_c+spsbar+down_c+spsbar+zip_c+spsbar+edt_c+spsbar+rm_c+spsbar+mv_c+spsbar+ABOUT
  else:
    opt=opt.replace("--","")
    opt=opt+"_c"
    x=""
    exec(f"print({opt})")
#}END.
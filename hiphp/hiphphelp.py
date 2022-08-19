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
def help():
    help_text="""
hiphp Commands :
════════════════
         Command                    Description
         -------                    -----------
[OPTIONS]─────┐
  ┌───────────┘
  ├─> --help                        ─> # Display this help.
  ├─> --geth                        ─> # Get the hole Code, "HIPHP_HOLE_CODE" It has the same purpose.
  ├─> --phpinfo                     ─> # Some information about the server.
  ├─> --cls                         ─> # Clear console.
  ├─> --exit                        ─> # Exit this console.
┌─┘
└[ACTIONS]────┐
  ┌───────────┘
  ├─> --ls                          ─> # List information about the FILEs (the current directory by default).
  ├─> Usage: --ls [OPTION] [PATH]
  ├┬> Mandatory arguments to long options:
  │├─> --ls                         ─> # Get a list of all files and folders from the current directory.
  │├─> --ls [PATH]                  ─> # Get a list of all files and folders from a specified directory.
  │├─> --ls -all                    ─> # Get a list of all files, folders and subfolders from the current directory.
  │└─> --ls -all [PATH]             ─> # Get a list of all files, folders and subfolders from a specified directory.
  ├─────────────────────────── ─ ─ ─
  ├─> --cat                         ─> # Concatenate FILE to standard output.
  ├─> Usage: --cat [FILE_PATH]
  ├─────────────────────────── ─ ─ ─
  ├─> --set                         ─> # Create a code that is always saved on during work.
  ├─> Usage: --set [PHP_CODE]
  ├─> You can return the initial value with "--dset".
  ├─────────────────────────── ─ ─ ─
  ├─> --rf                          ─> # Run code from file.
  ├─> Usage: --rf [FILE_PATH] [VARIABLES]
  ├┬> Mandatory arguments to long options:
  │├─> --rf [FILE_PATH]             ─> # Run code from file.
  │└─> --rf [FILE_PATH] [VARIABLES] ─> # Run code from file with variables, EX: --rf example.php var==1 var2==hello
  ├─────────────────────────── ─ ─ ─
  ├─> --up                          ─> # Upload a file.
  ├─> Usage: --up [FILE_PATH] [PATH]
  ├┬> Mandatory arguments to long options:
  │├─> --up [FILE_PATH]             ─> # Upload a file to the current directory.
  │└─> --up [FILE_PATH] [PATH]      ─> # Upload a file to a specified directory.
┌─┘
└[ABOUT]─────┐
  ┌──────────┘
  ├─> --update                      ─> # check for updates.
  ├─> --license                     ─> # This project license.
  ├─> --about                       ─> # About this project.
  .
  .
  ."""
    return help_text
#}END.
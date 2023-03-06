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
import curses
import json
import subprocess

def main_menu(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.clear()
    stdscr.refresh()

    with open('menu_options.json', 'r') as f:
        options = json.load(f)

    option_names = list(options.keys())
    selected_option = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        for index, option in enumerate(option_names):
            x = width//2 - len(option)//2
            y = height//2 - len(option_names)//2 + index
            if index == selected_option:
                stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, option)
            stdscr.attroff(curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP and selected_option > 0:
            selected_option -= 1
        elif key == curses.KEY_DOWN and selected_option < len(option_names) - 1:
            selected_option += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            selected_option_name = option_names[selected_option]
            selected_option_command = options[selected_option_name]
            if selected_option_command == "exit()":
                exit()
            elif isinstance(selected_option_command, dict):
                selected_option_names = list(selected_option_command.keys())
                selected_option_names.remove("back") # remove the back option from the list
                selected_submenu_option = 0
                while True:
                    stdscr.clear()
                    height, width = stdscr.getmaxyx()

                    for index, option in enumerate(selected_option_names):
                        x = width//2 - len(option)//2
                        y = height//2 - len(selected_option_names)//2 + index
                        if index == selected_submenu_option:
                            stdscr.attron(curses.color_pair(1))
                        stdscr.addstr(y, x, option)
                        stdscr.attroff(curses.color_pair(1))

                    stdscr.refresh()

                    submenu_key = stdscr.getch()
                    if submenu_key == curses.KEY_UP and selected_submenu_option > 0:
                        selected_submenu_option -= 1
                    elif submenu_key == curses.KEY_DOWN and selected_submenu_option < len(selected_option_names) - 1:
                        selected_submenu_option += 1
                    elif submenu_key in [curses.KEY_ENTER, 10, 13]:
                        selected_submenu_name = selected_option_names[selected_submenu_option]
                        selected_submenu_command = selected_option_command[selected_submenu_name]
                        if selected_submenu_command == "back":
                            break  # break out of the submenu loop and go back to main menu
                        else:
                            stdscr.clear()
                            stdscr.addstr(0, 0, f"Running: {selected_submenu_command}\n")
                            stdscr.refresh()
                            process = subprocess.Popen(selected_submenu_command, stdout=subprocess.PIPE, shell=True)
                            while True:
                                output = process.stdout.readline()
                                if output == b'' and process.poll() is not None:
                                    break
                                if output:
                                    stdscr.addstr(output.decode())
                                    stdscr.refresh()
                            stdscr.addstr("Press any key to continue")
                            stdscr.refresh()
                            stdscr.getch()
                            break
                selected_option = 0

            else:
                stdscr.clear()
                stdscr.addstr(0, 0, f"Running: {selected_option_command}\n")
                stdscr.refresh()
                process = subprocess.Popen(selected_option_command, stdout=subprocess.PIPE, shell=True)
                while True:
                    output = process.stdout.readline()
                    if output == b"":
                        break
                stdscr.addstr(output.decode())
                stdscr.refresh()
                stdscr.addstr("Process completed. Press any key to continue.\n")
                stdscr.refresh()
                stdscr.getch()


curses.wrapper(main_menu)
#}END.
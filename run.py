# ------------------------------------------------------------------------------

import os
import time
import sys
from random import randint


def slowprint(s):
    for c in s + '\n':
        sys. stdout.write(c)
        sys. stdout.flush()
        time.sleep(0.1)


def cls():
    """
    This function will clear the console
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def logo():
    """
    Main logo to be repeated for most screens
    """
    print(" ")
    print("            ______              _     _     _                     ")
    print("           |   _  \            | |   | |   | |                    ")
    print("           |  (_)  |   _____   | |_  | |_  | |    ____            ")
    print("           |   _  <   /  _  \  | __| | __| | |   / _  \           ")
    print("           |  (_)  | |  (_)  | | |_  | |_  | |_ |   __/           ")
    print("           |______/   \___/\_\ \___| \___| \___| \____|           ")
    print(" ")
    print("               _____   __        _                                ")
    print("              /   __) |  |      (_)                               ")
    print("              \   \   |  |___    _     ____      __               ")
    print("               \   \  |   _  \  | |   |  _  \  / __|              ")
    print("              __\   \ |  | |  | | |_  | (_)  | \__ \              ")
    print("             (______/ |__| |__| \___| |   __/  |___/              ")
    print("                                      |__|                        ")
    print(" ")
    print("                                             By Jamie Phelps      ")


def main_menu():
    cls()
    logo()
    print("                    Welcome to Battleships                      \n")
    print("       There are Klingon battleships out there captain!         \n")
    print("  Out smart the Klingon commanders and destory all their ships! \n")
    print("      Commander, please choose one of the following options:    \n")
    
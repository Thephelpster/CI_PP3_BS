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
    print("     Star Trek")
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


cls()
logo()
#print("")
#slowprint("                    Welcome to Battleships")
#slowprint("       There are Klingon battleships out there captain!")
#slowprint("  Out smart the Klingon commanders and destory all their ships!")
#print("")
#slowprint("Engagement Rules:\n")
#slowprint("       First you will need to choose the size of the board.")
#slowprint("  You will have either 4 or 8 attempts to destory the klingons.")
#slowprint("       4 attempts if you choose 5 or less and 8 for more.")
#slowprint("       A hit will be marked as an 'X' and a miss as a 'O'.")
#slowprint("           If you destory all of the ships then you win.")
#slowprint("                         Good Luck.\n")
while True:
    BATTLEFIELD_SIZE = input("Enter the size of the battle field Captain:\n")
    if BATTLEFIELD_SIZE.isdigit():
        BATTLEFIELD_SIZE = int(BATTLEFIELD_SIZE)
        if BATTLEFIELD_SIZE > 1 and BATTLEFIELD_SIZE <= 10:
            print("Good work Captain, lets show the Klingons") 
            print("how we do things in starfleet!\n")
            break
        else:
            print("Captain, you must pick a number bewteen 1 and 10.\n")
    else:
        print("Captain, you selection must be a number and no letters.\n")
        print("It must also be no lower than 1 and no higher than 10.\n")
        continue


def collect_field_choice():
    for x in range(B):
        BATTLEFIELD.append(["~"] * B)
    return B


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def board_printout():
    let = ALPHABET[0: (B)]
    print("         %s%s" % (" ", " ".join(let)))
    row_num = 1
    for row in BATTLEFIELD:
        if row_num <= 9:
            print("        %d|%s|" % (row_num, "|".join(row)))
        else:
            print("       %d|%s|" % (row_num, "|".join(row)))
        row_num += 1
    print("")


def start_game():
    collect_field_choice()
    board_printout()


B = BATTLEFIELD_SIZE
BATTLEFIELD = []

start_game()

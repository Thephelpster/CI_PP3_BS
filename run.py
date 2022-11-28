# ------------------------------------------------------------------------------

import os
import time
import sys
from random import randint


# The orginal code came from StackOverFlow
def slowprint(s):
    """
    This function slows the way the prints are typed out making it look
    as though someone is typing it out. 
    """
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
    print(" ")


cls()
logo()
"""
This is the first part that the player sees and explains the rules, it 
also lets them select the size of the board. The rules arre also printed 
to the console slowly as if they were being type.
"""
print("")
slowprint("                    Welcome to Battleships")
slowprint("       There are Klingon battleships out there Captain!")
slowprint("  Out smart the Klingon commanders and destory all their ships!")
print("")
slowprint("Engagement Rules:\n")
slowprint("       First you will need to choose the size of the board.")
slowprint("     You will have multiple attempts to destory the klingons.")
slowprint("       A hit will be marked as an 'X' and a miss as a 'O'.")
slowprint("           If you destory all of the ships then you win.")
slowprint("                         Good Luck.\n")

while True:
    BATTLEFIELD_SIZE = input("Enter the size of the battlefield Captain:\n")
    if BATTLEFIELD_SIZE.isdigit():
        BATTLEFIELD_SIZE = int(BATTLEFIELD_SIZE)
        if BATTLEFIELD_SIZE > 1 and BATTLEFIELD_SIZE <= 10:
            print("Good work Captain.\n")
            print("Lets show the Klingons how we do things in starfleet!\n")
            break
        else:
            print("Captain, you must pick a number bewteen 1 and 10.\n")
    else:
        print("Captain, you selection must be a number and no letters.\n")
        print("It must also be no lower than 1 and no higher than 10.\n")
        continue


def collect_field_choice():
    cls()
    logo()
    for x in range(B):
        BATTLEFIELD.append([" "] * B)
    return B


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def board_printout():
    """
    This function builds the board size that the player has selected and
    adds space around it to make it easier to see.
    """
    let = ALPHABET[0: (B)]
    print("                        %s%s" % (" ", " ".join(let)))
    row_num = 1
    for row in BATTLEFIELD:
        if row_num <= 9:
            print("                       %d|%s|" % (row_num, "|".join(row)))
        else:
            print("                      %d|%s|" % (row_num, "|".join(row)))
        row_num += 1
    print("")


def add_klingons():
    """
    This function decided how many klingons the player will face and how
    many shots they get depending on the board size.
    """
    klingon_num = 0
    global KLINGONS
    if B <= 3:
        KLINGONS = 1
        while klingon_num != KLINGONS:
            klingon_row = randint(1, (B))
            klingon_column = randint(1, (B))
            klingon_location = [klingon_row, klingon_column]
            KLINGON_PLACE.append(klingon_location)
            klingon_num += 1
    elif B > 4 and B < 7:
        KLINGONS = 5
        while klingon_num != KLINGONS:
            klingon_row = randint(1, (B))
            klingon_column = randint(1, (B))
            klingon_location = [klingon_row, klingon_column]
            KLINGON_PLACE.append(klingon_location)
            klingon_num += 1
    else:
        KLINGONS = 8
        while klingon_num != KLINGONS:
            klingon_row = randint(1, (B))
            klingon_column = randint(1, (B))
            klingon_location = [klingon_row, klingon_column]
            KLINGON_PLACE.append(klingon_location)
            klingon_num += 1


def pick_square():
    """
    This function is the main logic for the game. it will take the inputs
    from the player and add them to the board depending on whether its a hit
    or a miss and giving feedback to the player so they know whats happening
    in the game.
    """
    global KLINGONS_DESTORYED
    for trys in range((B*B) // 2):
        shots = int((B*B) // 2)
        print("")
        print(f"Captain, you've got {shots - trys} shots left.")
        print(f"You've also got {KLINGONS - KLINGONS_DESTORYED} klingon")
        print("ship left.\n")
        print("")
        col_try = None
        while True:
            col_try = input("Captain, please enter a column letter:\n")
            if col_try.isalpha() and len(col_try) == 1:
                col_try = col_try.lower()
                col_try = ord(col_try) - 96
                break
            else:
                board_printout()
                print("Pick and empty spot on the board Captain.\n")
                cls()
                logo()
                continue
        row_try = None
        while True:
            row_try = input("and now a row number:\n")
            if row_try.isdigit():
                row_try = int(row_try)
                cls()
                logo()
                break
            else:
                board_printout()
                print("We can't go there Captain.\n")
                continue
        guess = [row_try, col_try]
        if guess in KLINGON_PLACE:
            print("Good job Captain, you've destroyed a Klingon Battleship!\n")
            BATTLEFIELD[row_try - 1][col_try - 1] = "X"
            KLINGONS_DESTORYED += 1

        elif (trys + 1) - shots == 0:
            print("Seems like the Klingons have out-maneuvered us this")
            print("time Captain, withdraw at once!\n")

        elif (row_try < 1 or row_try > B) or (col_try < 1 or col_try > B):
            print("Captain, we can't shoot there. We can only engage in the")
            print("designated area:\n")
            print(f"Rows: 1-{B} and Columns: A-{ALPHABET [B - 1]}")

        elif (BATTLEFIELD[row_try - 1][col_try - 1]) == "O":
            print("Captain, we've already engaged at that location,")
            print("try another.\n")

        elif (BATTLEFIELD[row_try - 1][col_try - 1]) == "X":
            print("Captain, we've already engaged at that location,")
            print("try another.\n")

        else:
            print("Captain, that was a miss, try again sir.")
            print("")
            BATTLEFIELD[row_try - 1][col_try - 1] = "O"

        if KLINGONS_DESTORYED == KLINGONS:
            board_printout()
            print("Good job Captain, all Klingon targets have been")
            print("destoryed.\n")
            break
        board_printout()
    trys += 1


def start_game():
    """
    This function allows the game to fun in the correct order and gives the
    ability to add more functions easly,
    """
    collect_field_choice()
    board_printout()
    add_klingons()
    pick_square()


B = BATTLEFIELD_SIZE
BATTLEFIELD = []
KLINGON_PLACE = []
KLINGONS = 10
KLINGONS_DESTORYED = 0


start_game()

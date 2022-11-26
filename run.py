# -----------------------------------------------------------------------------
import sys
import time
import os
import gspread
from random import randint
from time import sleep


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
    print(" ")
    print("  ______              _     _     _           ")
    print(" |   _  \            | |   | |   | |          ")
    print(" |  (_)  |   _____   | |_  | |_  | |    ____  ")
    print(" |   _  <   /  _  \  | __| | __| | |   / _  \ ")
    print(" |  (_)  | |  (_)  | | |_  | |_  | |_ |   __/ ")
    print(" |______/   \___/\_\ \___| \___| \___| \____| ")
    print(" ")
    print("     _____   ___       _                      ")
    print("    /   __) |   |     (_)                     ")
    print("    \   \   |   |___   _     ____      __     ")
    print("     \   \  |   _   | | |   |  _  \  / __|    ")
    print("    __\   \ |  | |  | | |_  | (_)  | \__ \    ")
    print("   (______/ |__| |__| \___| |   __/  |___/    ")
    print("                            |__|              ")
    print(" ")


cls()
logo()
"""
Add the welcome screen for the game.
Display game name and creator.
Allows the player to pick the board size.
"""

print(" ")
print("                         By Jamie Phelps      ")
print("")
print("Welcome to Battleships!\n")
print("First things first. Enter the size of board you'd like to play on:\n")
print("A normal size board is 8X8 but a smaller board will be easier.\n")
while True:
    BOARD_SIZE = input("Please enter a board size between 1-10:")
    if BOARD_SIZE.isdigit():
        BOARD_SIZE = int(BOARD_SIZE)
        if BOARD_SIZE > 1 and BOARD_SIZE <= 10:
            print(f"Nice, you've chosen a {BOARD_SIZE} size board.")
            print(" ")
            break
        else:
            print("Please enter a number between 1-10.\n")
    else:
        print("please enter only a number between 1-10")
        continue


def main_menu():
    cls()
    logo()
    """
    This function will appear below the welcome screen and give the
    player the option to either play the game straight away or read the 
    game rules.
    """
    print("Please choose one of the following options:")
    main_menu = "1. Play Battleships with chosen size.\n2. See game rules.\n"
    main_menu_selection = input(main_menu)

    while main_menu_selection not in ("1, 2"):
        print("Please enter a 1 or 2 to continue.\n")
        main_menu = "1. Play Battleships with chosen size.\n2. See game rules.\n"
        main_menu_selection = input(main_menu)

    if main_menu_selection == "1":
        get_board_size()

    elif main_menu_selection == "2":
        game_rules()

    return main_menu_selection


def game_rules():
    """
    This function will explain the rules of Battleships to the player.
    It will also take the player back to the main menu.
    """
    cls()
    logo()
    print("Game Rules:")
    slowprint("Now you have chosen your size of board,")
    slowprint("You will take it in turns to sink each others battleships.\n")
    slowprint("A hit will be marked as an 'X' and a miss as a 'O'.\n")
    slowprint("If you sink all of the ships then you win.\n")
    slowprint("You have 10 shots to win.\n")
    slowprint("Good Luck.\n")

    input("Enter any key to continue...\n")
    
    cls()
    main_menu()


def get_board_size():
    """
    This function will get the custom board size using the global varible 'Y'.
    """
    for x in range(Y):
        BOARD.append(["-"] * Y)
    return Y
    

def play_game():
    """
    This function will play the game in the correct order
    """
    pass


def restart_game():
    """
    This function will allow the player to restart the game from either the
    end of a finshed game or at the begining if they decide to change the 
    size of the board.
    """
    print("Would you like to restart the game?")
    restart_game = "1. Yes.\n2. No.\n"
    restart_game_selection = input(restart_game)

    while restart_game_selection not in ("1, 2"):
        print("Please enter a 1 or 2 to continue.\n")
        restart_game = "1. Yes.\n2. no.\n"
        restart_game_selection = input(restart_game)

        if restart_game_selection == "1":
            print("argv was", sys.argv)
            print("sys.executable was", sys.executable)
            print("restart now")

        elif restart_game_selection == "2":
            break


def main():
    """
    Run all program functions
    """
    main_menu()
    play_game()
    restart_game()


Y = BOARD_SIZE
BOARD = []
SHIPS = 10
APLHABET = "ABCDEFGHIJ"

main()

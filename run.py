import os
import time
import sys
from random import randint
from time import sleep


def logo():
    """
    Main logo to be repeated for most screens
    """
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
    print("                         By Jamie Phelps      ")


def cls():
    """
    This function will clear the console
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def slowprint(s):
    for c in s + '\n':
        sys. stdout.write(c)
        sys. stdout.flush()
        time.sleep(0.1)


def run_game():
    cls()
    logo()
    print("please choose one of the following options:\n")
    run_game = "1. play game and choose board size\n2. read the rules\n"
    run_game_selection = input(run_game)

    while run_game_selection not in ("1, 2"):
        print("please enter a 1 or a 2 to continue")
        run_game = "1. play game and choose board size\n2. read the rules\n"
        run_game_selection = input(run_game)
    
    if run_game_selection == "1":
        board_size()
        
    elif run_game_selection == "2":
        game_rules()

    return run_game_selection


def game_rules():
    """
    This function will explain the rules of Battleships to the player.
    It will also take the player back to the main menu.
    """
    cls()
    logo()
    print("Game Rules:")
    slowprint("First you will need to choose the size of the board.\n")
    slowprint("You will take it in turns to sink each others battleships.\n")
    slowprint("A hit will be marked as an 'X' and a miss as a 'O'.\n")
    slowprint("If you sink all of the ships then you win.\n")
    slowprint("You have 10 shots to win.\n")
    slowprint("Good Luck.\n")

    input("\nEnter any key to continue...\n")

    cls()
    logo()
    run_game()


def board_size():
    cls()
    logo()
    print("please choose the size of board you want to play:\n")
    board_size = "1. 4X4 2. 6X6 3. 8X8\n"
    board_size_selection = input(board_size)

    while board_size_selection not in ("4, 6, 8"):
        print("please choose the size of board you want to play:\n")
        board_size = "1. 4X4 2. 6X6 3. 8X8\n"
        board_size_selection = input(board_size)

    if board_size == "1":
        easy_board()

    elif board_size == "2":
        medium_board()

    elif board_size == "3":
        hard_board()


let_to_num = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

EASY_BOARD_PLAYER = [[' ']*4 for x in range(4)]
EASY_BOARD_COMP = [[' ']*4 for x in range(4)]


def easy_board(board):

    print(' A B C D')
    print(' -------')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


def medium_board(board):
    print(' A B C D E F')
    print(' -----------')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


def hard_board(board):
    print(' A B C D E F G H')
    print(' ---------------')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


def main():
    run_game()


main()

#-------------------------------------------------------------------------------
import sys
import time
import os
import gspread
import random
from google.oauth2.service_account import Credentials
from time import sleep

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('game_difficulty')

def slowprint(s):
    for c in s + '\n':
        sys. stdout.write(c)
        sys. stdout.flush()
        time.sleep(0.1)

def cls():
    """
    This function will clear the console
    """
    os.system('cls' if os.name=='nt' else 'clear')

def welcome():
    """
    Add the welcome screen for the game.
    Display game name and creator.
    """
    print(" ")
    print("  ______              _     _     _           ")
    print(" |   _  \            | |   | |   | |          ")
    print(" |  (_)  |   ____    | |_  | |_  | |    ____  ")
    print(" |   _   <  /  _  \  | __| | __| | |   / _  \ ")
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

def main_menu():
    """
    This function will appear below the welcome screen and give the
    player the option to either play the game straight away or read the 
    game rules.
    """
    print("Please choose one of the following options:")
    main_menu = "1. Play Battleships.\n2. See the game rules.\n"
    main_menu_selection = input(main_menu)

    while main_menu_selection not in ("1, 2"):
        print("Please enter a 1 or 2 to continue.\n")
        main_menu = "1. Play Battleships.\n2. See game rules.\n3. Settings.\n"
        main_menu_selection = input(main_menu)

    if main_menu_selection == "1":
        difficulty_choice()

    elif main_menu_selection == "2":
        game_rules()

    return main_menu_selection

def settings_menu():
    """
    This function will give the player the option to choose the dificulty
    either easy or hard. This will change the size of the board
    """
    pass

def game_rules():
    """
    This function will explain the rules of Battleships to the player.
    It will also take the player back to the main menu.
    """
    cls()
    welcome()
    print("Game Rules:")
    slowprint("You will take it in turns to sink each others battleships.\n")
    slowprint("A hit will be marked as an 'X' and a miss as a '-'.\n")
    slowprint("If you sink more ships than the computer you win.\n")
    slowprint("You have 10 moves to win.\n")
    slowprint("Good Luck.\n")

    input("Enter any key to continue...\n")
    
    cls()
    welcome()
    main_menu()

def play_game():
pass

def main():
    """
    Run all program functions
    """
    welcome()
    main_menu()
main()
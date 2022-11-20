#-------------------------------------------------------------------------------
import sys
import time
from time import sleep

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
    player the option to either play the game straight away, open the settings
    menu or read the game rules.
    """
    print("Please choose one of the following options:")
    main_menu = "1. Play Battleships.\n2. See the game rules.\n3. Settings.\n"
    main_menu_selection = input(main_menu)

    while main_menu_selection not in ("1, 2, 3"):
        print("Please enter a 1, 2 or 3 to continue.\n")
        main_menu = "1. Play Battleships.\n2. See game rules.\n3. Settings.\n"
        main_menu_selection = input(main_menu)

    if main_menu_selection == "1":
        start_game()

    elif main_menu_selection == "2":
        game_rules()

    elif main_menu_selection == "3":
        settings_menu()

    return main_menu_selection

def settings_menu():
    """
    This function will give the player the option to choose the dificulty
    either easy or hard. This will change the size of the board, how many
    ships.
    """
    pass

def game_rules():
    """
    This function will explain the rules of Battleships to the player.
    It will also take the player back to the main menu.
    """
    welcome()
    print("Game Rules:")
    words1 = "You will take it in turns to sink each others battleships.\n"
    words2 = "A hit will be marked as an 'X' and a miss as a '-'.\n"
    words3 = "If you sink more ships than the computer you win.\n"
    words4 = "You have 10 moves to win.\n"
    words5 = "Good Luck.\n"
    for char in words1, words2, words3, words4, words5:
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    input("Enter any key to continue...\n")
    main_menu()

def start_game():
    """
    This function will allow the player to input their name which will be
    saved to a google sheet and accessed in another play through.
    """
    pass

def main():
    """
    Run all program functions
    """
    welcome()
    main_menu()
main()
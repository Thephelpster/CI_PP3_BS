#-------------------------------------------------------------------------------

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
    print("Please choose one of the following options")
    main_menu = "1. Play Battleships.\n2. See the game rules.\n3. Settings."
    main_menu_selection = input(main_menu)

    while main_menu_selection not in ("1, 2, 3"):
        print("Please enter a 1, 2 or 3 to continue./n")
        main_menu = "1. Play Battleships.\n2. See the game rules.\n3. Settings."
        main_menu_selection = input(main_menu)

    if sub_menu_selection == "1":
        start_game()

    elif sub_menu_selection == "2":
        game_rules()

    elif sub_menu_selection == "3":
        settings_menu()

def settings_menu():
    pass

def game_rules():
    pass

def start_game():
    pass

def main():
    """
    Run all program functions
    """
    welcome()
    main_menu()
main()
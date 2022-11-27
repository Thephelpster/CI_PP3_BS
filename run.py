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

    


def main():
    run_game()


main()
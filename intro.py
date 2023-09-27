import sys
from deck import deck
from card_battle import card_battle


def intro():
    print("-------------")
    print("Main Menu")
    print("1. Play ⚔️")
    print("2. View Deck 🎴")
    print("3. Quit ☠️")
    player_menu_choice = input("Select an option: ")
    if player_menu_choice == "1":
        card_battle()
    elif player_menu_choice == "2":
        print(deck)
        intro()
    elif player_menu_choice == "3":
        sys.exit()
    else:
        print("Invalid option.")

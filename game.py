from intro import intro
from cards import choose_cards_to_add_to_deck
from deck import deck


def main():
    print("Welcome to Python Card Game")
    # creating a variable to store the values returned in choose_cards_to_add_to_deck
    selected_cards = choose_cards_to_add_to_deck()

    deck.extend(selected_cards)
    intro()


if __name__ == "__main__":
    main()

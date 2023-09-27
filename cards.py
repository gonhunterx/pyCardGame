# name, health, damage
from card import Card

available_cards = [
    Card("Deth", 4, 4),
    Card("Mona", 5, 3),
    Card("Rampart", 8, 3),
    Card("Jinto", 3, 3),
]


def display_available_cards():
    print("Available Cards: ")
    for i, card in enumerate(available_cards, 1):
        print(
            f"{i}, {card.name} - Health: {card.card_health}, Damage: {card.card_damage}"
        )


def choose_cards_to_add_to_deck():
    selected_cards = []
    while len(selected_cards) < 3:
        display_available_cards()
        try:
            choice = int(
                input(
                    f"Choose card {len(selected_cards) + 1} (1-{len(available_cards)}): "
                )
            )
            if 1 <= choice <= len(available_cards):
                selected_card = available_cards.pop(choice - 1)
                selected_cards.append(selected_card)
            else:
                print("Invalid Choice. Please selected a valid card")
        except ValueError:
            print("Invalid Input. Please enter a number.")
    return selected_cards

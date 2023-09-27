class Card:
    def __init__(self, name, card_health, card_damage):
        self.name = name
        self.card_health = card_health
        self.card_damage = card_damage

    def card_display(self):
        # card_selection = input("Enter a card to view: ")
        print(f"{self.name}")
        print(f"Health: {self.card_health}")
        print(f"Damage: {self.card_damage}")


# to create new cards with the Card() class all you have to do is name the card and then add in the attributes
# like r1 = Robot() (imagine next lines) \n r1.name = "Tom" r1.color = "red" r1.weight = 30
# like this and you will create a new object

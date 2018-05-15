
class Card:
    
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self, value, suit):
        self.set_value(value)
        self.set_suit(suit)

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def set_value(self, value):
        if value not in Card.values:
            raise ValueError
        self.value = value

    def set_suit(self, suit):
        if suit not in Card.suits:
            raise ValueError
        self.suit = suit
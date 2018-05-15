
from random import shuffle

from Card import Card


class Deck:

    _cards = []
    _count = 0

    def __init__(self):
        for suit in Card.suits:
            for value in Card.values:
                card = Card(value, suit)
                self._cards.append(card)

        self._count = len(self._cards)

    def __repr__(self):
        return f"Deck of {self._count} cards"

    def get_cards(self):
        return self._cards

    def get_count(self):
        return self._count

    def set_count(self):
        self._count = len(self._cards)

    def get_max_cards(self):
        return len(Card.values) * len(Card.suits)

    def deal(self, amount):
        if amount > self.get_count():
            raise ValueError
        if amount > self._count:
            amount = self._count
        for _ in range(0, amount):
            print(self._cards.pop())
        self.set_count()

    def shuffle(self):
        if self._count != self.get_max_cards():
            raise ValueError
        shuffle(self._cards)
        return self._cards

    def deal_card(self):
        self.deal(1)

    def deal_hand(self, amount):
        self.deal(amount)


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    deck.deal_hand(3)
    # print(deck.get_count())
    deck.deal_card()
    # print(deck.get_count())
    deck.deal_card()
    # print(deck.get_count())

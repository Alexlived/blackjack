import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    suits = ["spades", "clubs", "diamonds", "hearts"]
    values = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "jack",
        "queen",
        "king",
        "ace",
    ]

    def __init__(self):
        self.cards = []
        self.make_cards()

    def make_cards(self):
        self.cards.clear()
        for suit in Deck.suits:
            for value in Deck.values:
                card = Card(suit, value)
                self.cards.append(card)

    def count_cards(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []

    def take_card(self, card_to_take):
        self.cards.append(card_to_take)

    def remove_card(self, card_to_remove):
        return self.cards.pop(card_to_remove)

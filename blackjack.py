import random

from deck_logic import *

deck = Deck()
deck.shuffle()


class Player:
    def __init__(self, h):
        self.hand = h

    def handle_aces_pls(self):
        list_of_cards = self.hand.cards
        dupe_list_of_cards = list_of_cards[:]
        ace_list = []
        for card in dupe_list_of_cards:
            if card.value == "ace":
                ace_list.append(dupe_list_of_cards.pop(card))
            else:
                pass
            aceless_value = 0
            for card in dupe_list_of_cards:
                try:
                    aceless_value += int(card.value)
                except ValueError:
                    aceless_value += 10

            if len(ace_list) != 0:
                for i in range(len(ace_list)):
                    if aceless_value + 11 > 21:
                        return 1
            else:
                return 11

    def value(self):
        total_value = 0
        for card in self.hand.cards:
            try:
                total_value += int(card.value)
            except ValueError:
                if card.value == "ace":
                    total_value += self.handle_aces_pls()
                else:
                    total_value += 10

        return total_value

    def bust(self):
        total_value = self.value()
        bust_v = total_value > 21
        return bust_v


def hit(hand):
    hand.take_card(deck.deal_card())


def readable_cards(hand):
    cards_in_hand = []
    for card in hand.cards:
        cards_in_hand.append(str(card))
    return cards_in_hand


def game():
    player_hand = Hand()
    computer_hand = Hand()
    for i in range(2):
        player_hand.take_card(deck.deal_card())
        computer_hand.take_card(deck.deal_card())
    computer = Player(computer_hand)
    player = Player(player_hand)
    while True:
        player_cards = readable_cards(player_hand)

        # for card in player_hand.cards:
        #     player_cards.append(str(card))
        print(f"Your cards are {','.join(player_cards)}")
        print()
        print(f"The dealers upcard is {computer_hand.cards[0]}")
        print()
        print("Would you like to hit?")
        player_choice = input("[y/N]").lower()
        if player_choice == "":
            player_choice = "n"
        if player_choice == "y":
            hit(player_hand)
            player_cards.append(str(player_hand.cards[-1]))
            if player.bust():
                print(player_cards)
                print("You busted")
                break
        else:
            break

    while computer_computing(computer_hand, computer):
        hit(computer_hand)

    print()
    print(
        f"Your cards: {','.join(player_cards)} , Dealer cards: {','.join(readable_cards(computer_hand))}"
    )

    print()
    if computer.value() > player.value():
        print("You lost!")
    elif computer.value() == player.value():
        print("Its a tie!")
    else:
        print("You won!")


game()

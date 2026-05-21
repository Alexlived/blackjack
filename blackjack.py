import random

from deck_logic import *

deck = Deck()
deck.shuffle()


class Player:
    def __init__(self, h):
        self.hand = h

    def score(self):
        aces = 0
        t_value = 0
        for card in self.hand.cards:
            if card.value.isdigit():
                t_value += int(card.value)
            elif card.value.lower() in ("king", "jack", "queen"):
                t_value += 10
            else:
                t_value += 11
                aces += 1
        while t_value > 21 and aces > 0:
            t_value -= 10
            aces -= 1

        return t_value


def hit(hand):
    hand.take_card(deck.deal_card())


def readable_cards(hand):
    cards_in_hand = []
    for card in hand.cards:
        cards_in_hand.append(str(card))
    return cards_in_hand


def bust(player):
    if player.score() > 21:
        return True
    return False


def game_1():
    player_hand = Hand()
    computer_hand = Hand()
    player = Player(player_hand)
    computer = Player(computer_hand)
    for i in range(2):
        player_hand.take_card(deck.deal_card())
        computer_hand.take_card(deck.deal_card())
    computer = Player(computer_hand)
    player = Player(player_hand)
    if computer.score == 21:
        if player.score == 21:
            print("Push!")
            quit()
        else:
            print("Dealer wins!")
            quit()
    else:
        pass
    player_cards = readable_cards(player_hand)
    computer_cards = readable_cards(computer_hand)
    while True:
        print(f"Your cards are {','.join(player_cards)}")
        print()
        print(f"The dealers upcard is {computer_cards[0]}")
        print()
        player_choice = str(input("Would you like to hit?[y/n]: ")).lower()[0]
        if player_choice == "y":
            hit(player_hand)
            player_cards.append(str(player_hand.cards[-1]))
            if bust(player):
                print("You busted!")
                quit()
            else:
                pass
        else:
            break
    while True:
        if computer.score() < 17:
            hit(computer_hand)
            if bust(computer):  # Bust Logic
                print("The dealer busted!")
                quit()  # <-- Til here
            else:
                pass
        else:
            ace_count = 0
            for card in computer_hand.cards:
                if card.value == "ace":
                    ace_count += 1
            if ace_count > 0:
                hit(computer_hand)
                if bust(computer):  # Bust Logic
                    print("The dealer busted!")
                    quit()  # <-- Til here
                else:
                    pass
            else:
                break
    print()
    print(f"The dealer's final hand is {','.join(computer_cards)}")
    print()
    print(f"Your final hand is {','.join(player_cards)}")
    if computer.score() > player.score():
        print("The dealer wins!")
    elif computer.score() < player.score():
        print("You win!")
    else:
        print("It's a tie!")


game_1()

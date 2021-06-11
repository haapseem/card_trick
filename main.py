
import random

from collections import namedtuple

Card = namedtuple('Card', 'value land')  # Create card "class"


def print_deck(deck):
    """ Loop through every card on the deck and print it's value and land

        Args:
        - deck: set of card to be printed

    """

    for card in deck:
        card_value, card_land = card

        """ Check if card is jack, queen, king or Ace
            if card is one of them change card_value into corresponding string
        """
        if card_value == 11:
            card_value = 'Jack'
        elif card_value == 12:
            card_value = 'Queen'
        elif card_value == 13:
            card_value = 'King'
        elif card_value == 14:
            card_value = 'Ace'

        print(f'{card_value} of {card_land}')  # print card

def print_deck_content(deck):
    """ Print content of the deck

    exapmle print:
    Two: 4
    Three: 4
    ...
    Queen: 8
    King: 4
    Ace: 0

    Args:
    - deck: set of cards to be printed

    """
    for i in range(2, 15):
        cards = 0
        value = i

        for card in deck:
            card_value, card_land = card
            if card_value == value:
                cards += 1

        """ Check if card is jack, queen, king or Ace
            if card is one of them change card_value into corresponding string
        """
        if i == 11:
            value = 'Jack'
        elif i == 12:
            value = 'Queen'
        elif i == 13:
            value = 'King'
        elif i == 14:
            value = 'Ace'

        print(f'{value}: {cards}')  # print card


"""

First task

"""
# Create deck of cards
deck = [(x, y) for x in range(2, 15) for y in ["Hearts", "Diamonds", "Clubs", "Spades"]]


"""

Second task

"""
deck_copy_0 = deck[:]  # Create copy of the deck
random.shuffle(deck_copy_0)  # Shuffle copy of the deck


"""

Printing of the first and second task

"""
print("Deck after first task:")
print_deck(deck)

print("\nDeck after second task:")
print_deck(deck)
print("\nDeck copy after second task:")
print_deck(deck_copy_0)


"""

Third task

"""
deck = [Card(12 if x == 14 else x, y) for (x, y) in deck]

print("\nDeck after third task:")
print_deck_content(deck)
print("\nDeck copy after third task:")
print_deck_content(deck_copy_0) # I understood that these should not change

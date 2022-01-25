import random
import blackJack_project

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Deck:
    """
    A Deck class to hold all 52 Card objects, and can be shuffled
    """

    def __init__(self):
        self.deck = []
        for s in suits:
            for r in ranks:
                self.deck.append(blackJack_project.card.Card(s, r))

    def __str__(self):
        return "The total amount of cards in the deck is {}".format(len(self.deck))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

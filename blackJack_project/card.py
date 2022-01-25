values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    """
    Card class where each Card object has a suit and a rank
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

    def get_value(self):
        return "Card {} of {} has value {}".format(self.rank, self.suit, self.value)

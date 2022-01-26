class Hand:
    """
    Hand class that holds those Cards that have been dealt to each player from the Deck
    """

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.values = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def __str__(self):
        pass

    def add_card(self, card):
        self.cards.append(card)
        self.values += card.value

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        while self.values > 21 and self.aces:
            self.values -= 10
            self.aces -= 1

    def get_cards(self):
        return self.cards

    def reset_hand(self):
        self.__init__()

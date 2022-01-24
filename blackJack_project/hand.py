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

    def adjust_for_ace(self):
        for card in self.cards:
            if card.rank == 'Ace':
                self.aces += 1

        if self.aces == 2:
            self.values = 21
        elif self.aces == 1 and self.values > 21:
            self.values = self.values - 10

    def get_cards(self):
        return self.cards

    def reset_hand(self):
        self.__init__()

from blackJack_project.hand import Hand
from blackJack_project.chips import Chips


class Dealer:

    # Dealer Class

    def __init__(self, name):
        self.dealer_hand = Hand()
        self.dealer_stuck = Chips(name)
        self.name = name

    def __str__(self):
        return "The dealer is {}".format(self.name)

    def get_hand(self):
        return self.dealer_hand

    def get_chips(self):
        return self.dealer_stuck

import blackJack_project.hand as Hand
import blackJack_project.chips as Chips


class Dealer:

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

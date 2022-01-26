from blackJack_project.hand import Hand
from blackJack_project.chips import Chips


class Player:

    # Player class

    def __init__(self, name):
        self.name = name
        self.player_hand = Hand()
        self.player_chips = Chips(name)

    def __str__(self):
        return "The player is {}".format(self.name)

    def get_hand(self):
        return self.player_hand

    def get_chips(self):
        return self.player_chips

class Chips:

    def __init__(self, name):
        self.bet = 0
        msg = 'Please {} provide how many will be your stuck: '.format(name)
        while True:
            try:
                self.total = int(input(msg))
                if self.total == 0:
                    print("Please provide stuck greater than zero!!")
                    continue
            except Exception:
                print('Please provide an integer number as a stuck!')
                continue
            break

    def __str__(self):
        return "The current total Chips of player is: {}".format(self.total)

    def win_bet(self, other_bet=None):
        if other_bet is not None:
            self.bet = other_bet
        self.total += self.bet

    def lose_bet(self, other_bet=None):
        if other_bet is not None:
            self.bet = other_bet
        self.total -= self.bet

    def take_bet(self):
        invalid_bet = True
        while True:
            try:
                while invalid_bet:
                    self.bet = int(input('Please give your next bet: '))
                    if self.bet > self.total:
                        print("Please give an actual bet given from your stuck!")
                        invalid_bet = True
                    elif self.bet == 0:
                        print("Please give a bet greater than zero!")
                        invalid_bet = True
                    else:
                        invalid_bet = False
            except Exception:
                print('Please provide an integer number as a bet!')
                continue
            break
        return self.bet
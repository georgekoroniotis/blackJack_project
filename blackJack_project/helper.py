
def hit(deck, hand):
    """
    A function for taking hits

    Either player can take hits until they bust. This function will be called during gameplay anytime a Player requests
    a hit, or a Dealer's hand is less than 17. It should take in Deck and Hand objects as arguments, and deal one card
    off the deck and add it to the Hand. You may want it to check for aces in the event that a player's hand exceeds 21.
    :param deck:
    :param hand:
    """
    card = deck.deal()
    hand.add_card(card)
    hand.adjust_for_ace()


# hit(new_deck,new_hand)
# hit(new_deck,new_hand)

# for i in new_hand.get_cards():
#    print(i)

def hit_or_stand(deck, hand):
    """
    A function prompting the Player to Hit or Stand

    This function should accept the deck and the player's hand as arguments, and assign playing as a global variable.
    If the Player Hits, employ the hit() function above. If the Player Stands, set the playing variable to False
    - this will control the behavior of a while loop later on in our code.

    :param deck:
    :param hand:
    :return:
    """
    global playing  # to control an upcoming while loop

    playing = True

    try:
        while True:
            x = input("Type 'h' for hit or 's' for stand: ")
            if x == 's' or x == 'h':
                break
    except Exception:
        print("An error occured")

    if x == 'h':
        hit(deck, hand)
    else:
        playing = False


def show_some(player, dealer):
    """
    Write functions to display cards

    When the game starts, and after each time Player takes a card, the dealer's first card is hidden and all of Player's
    cards are visible. At the end of the hand all cards are shown, and you may want to show each hand's total value.
    Write a function for each of these scenarios.
    :param player:
    :param dealer:
    :return:
    """
    print("Players Cards are: ")
    print("------------------------")
    for p in player.player_hand.get_cards():
        print(p)
    print("\n")

    print("Dealers Card is: ")
    print("------------------------")
    for d in range(len(dealer.dealer_hand.get_cards()) - 1):
        print(dealer.dealer_hand.get_cards()[d])
    print("\n")


# hit(new_deck, new_player.player_hand)
# hit(new_deck, new_player.player_hand)
# hit(new_deck, new_dealer.dealer_hand)
# hit(new_deck, new_dealer.dealer_hand)
# show_some(new_player, new_dealer)


def show_all(player, dealer):
    """
    Write functions to display cards

    When the game starts, and after each time Player takes a card, the dealer's first card is hidden and all of Player's
    cards are visible. At the end of the hand all cards are shown, and you may want to show each hand's total value.
    Write a function for each of these scenarios.
    :param player:
    :param dealer:
    :return:
    """
    print("Players Cards are: ")
    print("------------------------")
    for p in player.player_hand.get_cards():
        print(p)
    print("\n")

    print("Dealers Cards are: ")
    print("------------------------")
    for d in dealer.dealer_hand.get_cards():
        print(d)
    print("\n")


# hit(new_deck, new_player.player_hand)
# hit(new_deck, new_player.player_hand)
# hit(new_deck, new_dealer.dealer_hand)
# hit(new_deck, new_dealer.dealer_hand)
# show_all(new_player, new_dealer)


def player_busts(chips):
    chips.lose_bet()
    return chips.bet


def player_wins(chips):
    chips.win_bet()


def dealer_busts(chips, bet):
    chips.lose_bet(bet)
    return chips.bet


def dealer_wins(chips, bet):
    chips.win_bet(bet)


def push():
    pass
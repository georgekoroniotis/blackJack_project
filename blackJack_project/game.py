from blackJack_project.player import Player
from blackJack_project.dealer import Dealer
from blackJack_project.deck import Deck
from blackJack_project.helper import *


if __name__ == "__main__":
    # Print an opening statement
    print('Welcome to the Black Jack game!')

    # Set up the Player's chips
    new_player = Player('George')
    new_dealer = Dealer('Dealer')

    # Set up the Player's and Dealer's hands
    new_player_hand = new_player.get_hand()
    new_dealer_hand = new_dealer.get_hand()

    while True:
        # Initiate player_busted
        player_busted = False
        playing = True

        # Create & shuffle the deck, deal two cards to each player
        new_deck = Deck()
        new_deck.shuffle()

        new_player_chips = new_player.get_chips()
        new_dealer_chips = new_dealer.get_chips()

        # Reset hand as a new round
        new_player_hand.reset_hand()
        new_dealer_hand.reset_hand()

        # Prompt the Player for their bet
        round_bet = new_player_chips.take_bet()

        # Show cards (but keep one dealer card hidden)
        hit(new_deck, new_dealer_hand)
        hit(new_deck, new_dealer_hand)
        hit(new_deck, new_player_hand)
        hit(new_deck, new_player_hand)
        show_some(new_player, new_dealer)

        if new_player_hand.values == 21:
            print("WOW! Player hits Black Jack 21!")
            player_wins(new_player_chips)
            dealer_busts(new_dealer_chips, round_bet)
            playing = False
            player_busted = True

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            playing = hit_or_stand(new_deck, new_player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(new_player, new_dealer)
#            print("Player card values", new_player_hand.values)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if new_player_hand.values > 21:
                print("Sorry. Player exceeded 21..")
                # print("Dealers values are:", new_dealer_hand.values)
                # print("Players values are:", new_player_hand.values)
                player_busts(new_player_chips)
                dealer_wins(new_dealer_chips, round_bet)
                player_busted = True
                break
            # If player's hand reaches 1, player wins the game!
            if new_player_hand.values == 21:
                print("WOW! Player hits Black Jack 21!")
                # print("Dealers values are:", new_dealer_hand.values)
                # print("Players values are:", new_player_hand.values)
                player_wins(new_player_chips)
                dealer_busts(new_dealer_chips, round_bet)
                player_busted = True
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if not player_busted:
            # Show all cards
            show_all(new_player, new_dealer)
            # print("Dealers card values before loop: ", new_dealer_hand.values)
            while new_dealer_hand.values < 17:
                # print("Dealer hits one more card from the deck!")
                hit(new_deck, new_dealer_hand)

                # Show all cards
                show_all(new_player, new_dealer)
                # print("Player card values", new_player_hand.values)
                # print("Dealers card values", new_dealer_hand.values)

            # Run different winning scenarios
            if new_dealer_hand.values > 21:
                print("Dealer is busted! Exceed 21")
                # print("Dealers values are:", new_dealer_hand.values)
                # print("Players values are:", new_player_hand.values)
                player_wins(new_player_chips)
                dealer_busts(new_dealer_chips, round_bet)

            elif new_dealer_hand.values >= new_player_hand.values:
                print("Dealer wins this round!")
                # print("Dealers values are:", new_dealer_hand.values)
                # print("Players values are:", new_player_hand.values)
                player_bet = player_busts(new_player_chips)
                dealer_wins(new_dealer_chips, round_bet)

            else:
                print("Player wins this round!")
                # print("Dealers values are:", new_dealer_hand.values)
                # print("Players values are:", new_player_hand.values)
                player_wins(new_player_chips)
                dealer_busts(new_dealer_chips, round_bet)

        # Inform Player of their chips total
        print("{}'s pot is {} ".format(new_player.name, new_player_chips.total))
        print("Dealer's pot is ", new_dealer_chips.total)

        # Ask to play again
        if new_player_chips.total > 0:
            play_again = input("Do you want to continue betting (Y/N): ")
            if play_again == 'N':
                break
            else:
                playing = True
        else:
            print("Game Over! You lost all your stuck!")
            break

        # Check if the dealer has no money
        if new_dealer_chips.total <= 0:
            print("Dealer has no other chips! Player wins the game!")
            break

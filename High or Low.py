import random


def main():
    min = 1
    max = 13
    deck = {}
    player_choice = 0
    dealer_card1 = 0
    dealer_card1_value = 0
    dealer_card2 = 0
    dealer_card2_value = 0
    dealer_card_index = 0
    play_again = "yes"

    for x in range(0,14):
        if 11 > x > 0:
            deck['Club-{}'.format(x)] = x + 1
            deck['Diamond-{}'.format(x)] = x + 1
            deck['Heart-{}'.format(x)] = x + 1
            deck['Spade-{}'.format(x)] = x + 1

        elif x == 0:
            deck['Club-A'] = x
            deck['Diamond-A'] = x
            deck['Heart-A'] = x
            deck['Spade-A'] = x

        elif x == 11:
            deck['Club-J'] = x
            deck['Diamond-J'] = x
            deck['Heart-J'] = x
            deck['Spade-J'] = x

        elif x == 12:
            deck['Club-Q'] = x
            deck['Diamond-Q'] = x
            deck['Heart-Q'] = x
            deck['Spade-Q'] = x

        elif x == 13:
            deck['Club-K'] = x
            deck['Diamond-K'] = x
            deck['Heart-K'] = x
            deck['Spade-K'] = x

    print("When the game starts, type \"h\" for higher or \"l\" for lower!")
    print("To play again, type \"y\" or \"yes\" when prompted")

    while play_again == "yes" or play_again == "y":
        print('Deck size is: {}'.format(str(len(deck))))
        dealer_card1 = random.choice(list(deck.keys()))
        dealer_card1_value = deck[dealer_card1]
        print("Dealer's card is: " + dealer_card1)
        del deck[dealer_card1]
        player_choice = input("Player wants higher or lower?")
        dealer_card2 = random.choice(list(deck.keys()))
        dealer_card2_value = deck[dealer_card2]
        del deck[dealer_card2]
        print("The dealer's second card is: " + dealer_card2)

        if player_choice == "h":
            if dealer_card1_value == dealer_card2_value:
                print("It's a tie!, {0} has the same value as {1}.".format(dealer_card1, dealer_card2))
            elif dealer_card1_value < dealer_card2_value:
                print("Congratulations, {0} is higher than {1}. You won! :)".format(
                    dealer_card2, dealer_card1))
            else:
                print("I\'m sorry, {0} is not higher than {1}. You lost this time! :(".format(
                    dealer_card2, dealer_card1))
        elif player_choice == "l":
            if dealer_card1_value > dealer_card2_value:
                print("I\'m sorry, {0} is lower than {1}. You won! :)".format(
                    dealer_card2, dealer_card1))
            else:
                print("Congratulations, {0} is lower than {1}. You lost this time! :(".format(
                    dealer_card2, dealer_card1))

        play_again = input("Do you want to play again?")

main()

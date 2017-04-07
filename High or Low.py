import random

def main():
    min = 1
    max = 13
    player_choice = 0
    dealer_card1 = 0
    dealer_card2 = 0
    play_again = "yes"
    print("When the game starts, type \"h\" for higher or \"l\" for lower!")
    print("To play again, type \"y\" or \"yes\" when prompted")

    while play_again == "yes" or play_again == "y":
        dealer_card1 = random.randint(min, max)
        print("Dealer's card is: " + str(dealer_card1))
        player_choice = input("Player wants higher or lower?")
        dealer_card2 = random.randint(min, max)
        print("The dealer's second card is: " + str(dealer_card2))

        if player_choice == "h":
            if dealer_card1 < dealer_card2:
                print("Congratulations, {0} is higher than {1}. You won! :)".format(
                    dealer_card2, dealer_card1))
            else:
                print("I\'m sorry, {0} is not higher than {1}. You lost this time! :(".format(
                    dealer_card2, dealer_card1))
        elif player_choice == "l":
            if dealer_card1 > dealer_card2:
                print("I\'m sorry, {0} is lower than {1}. You won! :)".format(
                    dealer_card2, dealer_card1))
            else:
                print("Congratulations, {0} is lower than {1}. You lost this time! :(".format(
                    dealer_card2, dealer_card1))

        play_again = input("Do you want to play again?")

main()
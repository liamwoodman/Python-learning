# A Variation of 21
# If you do not know how 21 (AKA Blackjack) is played, reading the first couple of paragraphs of
# this wikipedia article may be beneficial.
#
# In this project, you will make a game similar to Blackjack. In this version:
#
# There is only one player.
# There are two types of scores: the game score and the round score.
# The game score will begin at 100, and the game will last for five rounds.
#
# At the beginning of the round, the player is given two random cards from a deck and they will be added together to
# make the player's round score.
#
# From here, the player has two options - draw another card to try to get their round score closer to 21, or they can
# end the round.
#
# The player can draw as many cards as they want until they end the round or their round score exceeds 21.
#
# At the end of the round, the difference between 21 and the round score is subtracted from the game score,
# and then the next round begins. After the five rounds, the player is given their total score and the game is over.
#
# ---Other Information About The Game---
#
# Aces are only worth 1.
#
# If a player busts, 21 is subtracted from their total score.
#
# All face cards are worth 10.
#
# So the point of your program is to allow the user to play the game described above.
#
# Subgoals:
# At the beginning of each round, print the round number (1 to 5).
#
# Since this is a text base game, tell the user what is happening. For example, tell him/her when he/she draws a
# card, the name of the card, when they bust, etc.
#
# Create a ranking system at the end of the game and tell the user their rank. For example, if the player finishes
# with 50-59 points they get an F, 60-69 is a D, 70-79 is a C, 80-89 is a B, and 90-100 is an A.
#
# At the end of each round, print out the user's total score.
#
# This may be the hardest part of the project, depending on how you wrote it. Make sure the deck has 4 of each type
# of card, and then remove cards as they are drawn. At the end of each round, make the deck have all of the cards
# again.

import const
import random
import time
# todo - fix the drawn pile, can't modify a const. So where would we pull from?


class Card:
    def __init__(self, value: str, suit: str, score: int):
        self.value = value
        self.suit = suit
        self.score = score


class Pile:
    def __init__(self, card_list: list):
        self.card_list = card_list


def list_pile(drawn_pile):
    drawn_list = []
    for card in drawn_pile.card_list:
        val = card.value
        suit = card.suit
        drawn_list.append((val, suit))
    return drawn_list


def deal(drawn_pile):
    while True:
        value = random.choice(const.VALUES)
        suit = random.choice(const.SUITS)
        card_combo = (value, suit)
        drawn_list = list_pile(drawn_pile)

        if card_combo in drawn_list:
            print("dupe found!" + card_combo)
            continue
        else:
            score = const.SCORES[value]
            new_card = Card(value, suit, score)
            drawn_pile.card_list.append(new_card)

            return new_card


def print_hand(hand_list):
    hand = ""
    for card in hand_list:
        card_str = card.value + " of " + card.suit + ", worth " + str(card.score) + ".\n"
        hand += card_str
    print("Your hand is: \n" + hand)


def new_round():
    new_deal = 2
    card_count = 0
    drawn_pile = Pile
    drawn_pile.card_list = []
    hand = []
    for card in range(new_deal):
        new_card = deal(drawn_pile)
        hand.append(new_card)
        card_count += 1
    print_hand(hand)

    current_score = 0
    for card in hand:
        current_score += card.score

    while True:

        if current_score > 21:
            print("You're bust! Your score for this round is 0. \n")
            return 0

        user_choice = input("Your current score is " + str(current_score) +
                            ". Would you like to hit (type H) or stand (type S)?\n")

        if user_choice.lower() == "h":
            new_card = deal(drawn_pile)
            print("The dealer deals you a new card.\n")
            time.sleep(1)
            print("It's " + new_card.value + " of " + new_card.suit + ", worth " + str(new_card.score) + ".\n")
            hand.append(new_card)
            current_score += new_card.score
            card_count += 1
        elif user_choice.lower() == "s":
            return current_score
        else:
            print("I didn't get that. Please try again.\n")
            continue


def rank(total_score):
    for ranking, ranges in const.RANKS.items():
        min_range, max_range = ranges
        if total_score in range(min_range, max_range):
            print("Your ranking is " + ranking + "!")


def play_again():
    while True:
        answer = input("Would you like to play again? Y/N\n")
        if answer.lower() == "y":
            return
        elif answer.lower() == "n":
            exit(0)
        else:
            print("\nI didn't catch that! Please try again\n")


def main():
    while True:
        print("Welcome to the Blackjack game!")
        time.sleep(1)
        round_counter = 0
        total_score = 0
        while round_counter < 5:
            round_score = new_round()
            total_score += round_score
            if round_counter == 4:
                pass
            else:
                print("\nTime for the next round. Your total score so far is " + str(total_score) + ".\n")
            time.sleep(2)
            round_counter += 1
        rank(total_score)
        play_again()


if __name__ == '__main__':
    main()

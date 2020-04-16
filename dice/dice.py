"""
By using the random module, Python can do things like pseudo-random number generation.

Allow the user to input the amount of sides on a dice and how many times it should be rolled.
Your program should simulate dice rolls and keep track of how many times each number comes up (this does not have to be displayed).
Finally, print out how many times each number came up.

Subgoals:
Adjust your program so that if the user does not type in a number when they need to, the program will keep prompting them to type
in a real number until they do so.
Put the program into a loop so that the user can continue to simulate dice rolls without having to restart the entire program.
In addition to printing out how many times each side appeared, also print out the percentage it appeared. If you can,
round the percentage to 4 digits total OR two decimal places.

Bonus:
You are about to play a board game, but you realize you don't have any dice. Fortunately you have this program.
Create a program that opens a new window and draws 2 six-sided dice
Allow the user to quit, or roll again
Allow the user to select the number of dice to be drawn on screen(1-4)
Add up the total of the dice and display it
"""

import random
import time
import pandas as pd
from collections import Counter


def ask():
    bad_input = True
    while bad_input:
        num = input("How many sides of the dice do you need?: \n")
        roll = input("And how many rolls do you need?: \n")
        params = [num, roll]
        for item in params:
            if int(item) == 0:
                print("\nBad entry detected, please try again.\n")
            elif not item.isnumeric():
                print("\n\nBad entry detected, please try again.\n")
            else:
                bad_input = False
    return int(num), int(roll)


def dice_roll(sides, rolls):
    results = []
    x = 0
    while x < rolls:
        new_roll = random.randint(1, sides)
        roll_sim()
        print("Your roll is " + str(new_roll) + ".")
        if rolls > 1:
            time.sleep(3)
        else:
            pass
        results.append(new_roll)
        x += 1
    return(results)


def roll_sim():
    print("\nTime to roll the dice!\n")
    time.sleep(1)
    secs = 3
    while secs > 0:
        print(str(secs) + "...")
        time.sleep(1)
        secs -= 1


def roll_freq(results):
    result_freq = Counter(results).most_common()
    output = {}
    result_dict = {}
    for index, roll in enumerate(result_freq):
        roll_num= roll[0]
        roll_val = roll[1]
        freq = round(float(roll_val / len(results)), 2)
        result_dict = {
            "Roll number": int(roll_num),
            "How many rolls": int(roll_val),
            "Roll frequency": freq
            }
        output[index] = result_dict
    return output


def again():
    check = input("Would you like to roll some more dice? Y/N: ")
    if check.lower() == "y":
        pass
    elif check.lower() == "n":
        exit()
    else:
        print("Please press either Y or N")
        again()


def main():
    print("\nWelcome to the dice rolling sim!\n")
    while True:
        sides, rolls = ask()
        result = dice_roll(sides, rolls)
        output = roll_freq(result)
        df = pd.DataFrame(output)
        df = df.transpose()
        print(df)
        again()


if __name__ == "__main__":
    main()


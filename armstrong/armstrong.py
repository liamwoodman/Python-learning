# Armstrong Number
#Learn about armstrong numbers here.
#Define a function that allows the user to check whether a given number is armstrong number or not.
#Hint: To do this, first determine the number of digits of the given number. Call that n. Then take every digit in the number and raise it to the nth power. Add them, and if your answer is the original number then it is an Armstrong number.
#Example: Take 1634. Four digits. So, 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634. So 1634 is an Armstrong number.
#Tip: All single digit numbers are Armstrong numbers.

import sys
import time

def ask():
    user_num = input("\nWhat number would you like to check?\n\nEnter your number here: ")
    check_num = str(user_num)
    if check_num.isnumeric():
        return int(user_num)
    else:
        print("\nPlease enter only numbers and try again\n")
        ask()

def check(num):
    length = len(str(num))
    digits = [int(x) for x in str(num)]
    power_up = []
    for i in digits:
        add = i**length
        power_up.append(int(add))
    power_sum = sum(power_up)
    if int(num) == int(power_sum):
        print("\nThis is an Armstrong Number!\n")
    else:
        print("\nThis is not an Armstrong Number.\n")

def again():
    check = input("Would you like to check another number? Y/N: ")
    if check.lower() == "y":
        pass
    elif check.lower() == "n":
        exit(1)
    else:
        print("Please press either Y or N")
        again()


def main():
    print("\nWelcome to the Armstrong Number Checker.")
    time.sleep(2)
    while True:
        num = ask()
        check(int(num))
        again()


if __name__ == "__main__":
    main()
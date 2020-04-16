# Countdown Clock
# Create a program that allows the user to choose a time and date, and then prints out a message at given intervals
# (such as every second) that tells the user how much longer there is until the selected time.
#
# Subgoals:
# If the selected time has already passed, have the program tell the user to start over.
# If your program asks for the year, month, day, hour, etc. separately, allow the user to be able to type in either the
# month name or its number.
# TIP: Making use of built in modules such as time and datetime can change this project from a nightmare
# into a much simpler task
import time
from datetime import datetime
from dateutil.parser import *
from dateutil import *


def get_datetime():
    check = True
    while check:
        # asks for current datetime and if this is out of bounds (ie 13th month, will not continue)
        try:
            date_time = input("What date and time (in 24hr time) would you like to count down to? Please follow this format: YYYY-MM-DD HH:MM\n")
        except ValueError:
            print("\n You have entered an out of bounds time and/or date. Please try again. \n")
            time.sleep(1)
            continue
        # parses the date-time to see if its valid
        try:
            datetime_parsed = parse(date_time)
        except ParserError:
            print("\nInvalid input detected, please try again.\n")
            continue
        present_datetime = datetime.now()
        user_check_str = "The date and time you want to count down is " + str(datetime_parsed) + ". Is this correct? Y/N\n"

        # Performs checks checks if date is in the past
        if present_datetime > datetime_parsed:
            print("\nYou have entered a date in the past. Please try again.\n")
            continue
        # something going wonky with this check, is restarting loop regardless, prob to do with if statement
        # elif not input(user_check_str).islower == 'y':
            continue
        else:
            break

        #
        # user_check = input("The date and time you want to count down is " + str(datetime_parsed) + ". Is this "
        #                                                                                                "correct? "
        #                                                                                                "Y/N\n")
        # if not user_check.islower() == 'y':
        #     continue
        # else:
        #     check = False

    print(datetime_parsed)
    return datetime_parsed



def main():
    print("Welcome to the Countdown program!")
    time.sleep(2)
    user_datetime = get_datetime()
    print("Counting down. Press Ctrl + C to end this process")
    while datetime.now() < user_datetime:
        count_delta = user_datetime - datetime.now()
        delta_list = str(count_delta).split(",")
        time_list = delta_list[1].split(":")
        print("There are " + delta_list[0] + " days," + time_list[0] + " hours, "
              + time_list[1] + " minutes and " + time_list[2][:-7] + " seconds to go.")
        time.sleep(5)
    exit(0)


if __name__ == "__main__":
    main()
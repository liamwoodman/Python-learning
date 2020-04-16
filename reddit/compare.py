# Compare Recent reddit Karma
# Since we're all redditors here, let's make something dealing with reddit.
# If you go to a user's profile and add .json to the end of it, you can get the all sorts of Json data about
# the user (think of Json as a giant dictionary of smaller dictionaries and lists).
# For example, if I go to my own profile and view it's Json data, it would look like this[1].
# At first it might look intimidating, but if you break it down, you can see it's just one giant
# dictionary with all sorts of information about my latest posts.
#
# Create a program that gets information about two different users, and then sees whose most recent post
# received the most karma.
# The program should then print out which user received more karma, and what the difference was.
# This is a pretty open project, so I encourage you to take it further by adding more features
# if you find it interesting.

# Remember - Elements in a list are referenced by their index numbers while entries in a
# dictionary are referenced by their keys.

# Subgoals:
# Allow the user to put in the name of two different users when the program first begins.
# If one of the names of the users does not exist (because of a spelling error), print out a message saying so.
# Allow the user to keep comparing other users until the program is closed.
# Display the amount of upvotes and downvotes each user received for their posts.
# Not sure how to turn json data into usable python data? Check this out.

# NB - Using PRAW as JSON isnt the best to pull in

import praw
import time
from dont_include import *


def new_session():
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT,
                         username=USERNAME,
                         password=PASSWORD)
    return reddit


def get_username_url(reddit):
    while True:
        usernames = input("Please enter both usernames you would like to compare, separated by a space.\n")
        names = tuple(usernames.split(" "))
        if not len(names) == 2:
            print("\nPlease try that again.\n")
        else:
            user_one = reddit.redditor(names[0])
            user_two = reddit.redditor(names[1])
            return [user_one, user_two]


# noinspection PyBroadException
def check_user(user):
    check = user.submissions.new(limit=10)
    try:
        if check:
            return True
    except Exception:
        print("There is no user with the name" + user + " or they have not made any posts. Please try again.")
        return False


def check_karma(user):
    user_subs = user.submissions.new(limit=10)
    for sub in user_subs:
        if sub.pinned:
            pass
        else:
            latest_sub = {
                "user": user.name,
                "title": sub.title,
                "karma": sub.ups,
                "url": sub.url
            }
            return latest_sub


def print_comparison(sub_list):
    if sub_list[0]["karma"] > sub_list[1]["karma"]:
        str_user_one = (sub_list[0]["user"] + "'s newest post titled '" + sub_list[0]["title"] + "' got them " +
                        str(sub_list[0]["karma"]) + " karma.\n")
        str_user_two = ("Whereas, " + sub_list[1]["user"] + "'s newest post titled '" + sub_list[1]["title"] +
                        "' got them " + str(sub_list[1]["karma"]) + " karma.\n")
        karma_dif = int(sub_list[0]["karma"]) - int(sub_list[1]["karma"])
        str_dif = ("The difference in karma between " + sub_list[0]["user"] + "'s post and " +
                   sub_list[1]["user"] + "'s post was " + str(karma_dif) + " karma.")
        print(str_user_one + str_user_two + str_dif)
    elif sub_list[1]["karma"] > sub_list[0]["karma"]:
        str_user_one = ("/" + sub_list[1]["user"] + "'s newest post titled '" + sub_list[1]["title"] + "' got them " +
                        str(sub_list[1]["karma"]) + " karma.\n")
        str_user_two = ("Whereas, " + sub_list[0]["user"] + "'s newest post titled '" + sub_list[0]["title"] +
                        "' got them " + str(sub_list[0]["karma"]) + " karma.\n")
        karma_dif = int(sub_list[1]["karma"]) - int(sub_list[0]["karma"])
        str_dif = ("The difference in karma between " + sub_list[1]["user"] + "'s post and " +
                   sub_list[0]["user"] + "'s post was " + str(karma_dif) + " karma.")
        print(str_user_one + str_user_two + str_dif)
    elif sub_list[1]["karma"] == sub_list[0]["karma"]:
        str_user_one = ("" + sub_list[0]["user"] + "'s newest post titled '" + sub_list[0]["title"] + "' got them " +
                        str(sub_list[0]["karma"]) + " karma.\n")
        str_user_two = ("Whereas, " + sub_list[1]["user"] + "'s newest post titled '" + sub_list[1]["title"] +
                        "' got them " + str(sub_list[1]["karma"]) + " karma.\n")
        str_even = ("" + sub_list[1]["user"] + "'s post and " +
                    sub_list[0]["user"] + "'s post have the same amount of karma.\n")
        print(str_user_one + str_user_two + str_even)


def again():
    while True:
        answer = input("\nWould you like to compare more redditors? Y/N\n")
        if answer.lower() == "y":
            return
        elif answer.lower() == "n":
            exit(0)
        else:
            print("\nI didn't catch that! Please try again\n")


def main():
    print("Welcome to the Reddit Karma Checker. This program checks who has the highest amount of upvotes on their" +
          " latest post!\n")
    time.sleep(1)
    reddit = new_session()
    while True:
        user_list = get_username_url(reddit)
        for user in user_list:
            is_user = check_user(user)
            if not is_user:
                continue
        print("\nGathering newest post data, please wait.\n")
        sub_list = []
        for user in user_list:
            sub_info = check_karma(user)
            sub_list.append(sub_info)
        print_comparison(sub_list)
        again()


if __name__ == '__main__':
    main()

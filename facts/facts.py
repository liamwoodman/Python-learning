# Watch for new TIL facts
# If you finished the previous project which compared the karma of two new comments,
# hopefully you learned a thing or two about receiving data from Reddit's API.
# Now you're going to take this a step further, and even have the opportunity to make a basic twitter bot.
#
# Create a program that receives data from the /r/todayilearned subreddit, and looks for new facts that have been
# posted. Each time the program comes across a new fact, the fact should be printed into the command line. However,
# phrases like "TIL ", "TIL that", etc should be removed so the only thing that is printed is the fact. New TIL API
# data here.
#
# There are a couple things to note about this since you'll more than likely be using a loop to check for new posts.
# According to Reddit's API Access Rules Page, the API pages are only updated once every thirty seconds,
# so you'll have to have your code pause for at least thirty seconds before it tries to find more posts. Secondly,
# if for some reason you decide to try to get data sooner than every thirty seconds, make sure to not send more than
# thirty requests per minute. That is the maximum you are allowed to do.
#
# There is actually a lot you can do once your program starts receiving facts. Instead of simply printing the facts,
# here are some ideas for what you can do with them. If you currently do not feel like you can accomplish these
# ideas, feel free to come back later when you have more experience.
#
# Print the link to the source of the fact too.
# Try to further clean up the fact by adding punctuation to the end if it is missing, capitalize the first word, etc.
# Write the facts to a separate text file so you end up with a giant compilation of random facts.
# Create a bot that posts the facts to twitter. This may sound hard, but it's actually pretty simple by using the
# Python Twitter Tools module and following the guide posted here.
# Remember, the maximum  amount of characters you can use in a tweet is only 140, so you'll have to filter out facts
# that are longer than that. By now you should be pretty familiar with python, so if you get ideas for
# improving your program, go for it!

import praw
import time
import datetime
import re
import os
import tweepy as tp

from dont_include import *


def delete_old_files():
    if os.path.isfile("facts.txt"):
        os.remove("facts.txt")
    if os.path.isfile("log.txt"):
        os.remove("log.txt")


def new_reddit_session():
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT,
                         username=USERNAME,
                         password=PASSWORD)
    return reddit


# todo write function that checks /r/TIL for new posts over 100 karma and adds to list (100 magic number, might drop)
def new_check(reddit):
    til = reddit.subreddit('todayilearned').new()
    new_posts = {}
    for post in til:
        if post.score >= 100:
            post_metadata = {
                "title": format_title(post.title),
                "author": post.author.name,
                "author_url": "https://reddit.com/u/" + post.author.name + "/",
                "url": post.url,
                "permalink": post.permalink,
                "unix_time": post.created_utc,
                "utc_time": datetime.datetime.utcfromtimestamp(int(post.created_utc)).strftime('%Y-%m-%d %H:%M:%S'),
                "upvotes": post.score
            }

            new_posts.update({post.name: post_metadata})
    return new_posts


# todo function that strips the 'TIL' out of title -prob need to do regex
def format_title(title):
    clean_title = re.sub("\Atil\s|\Atil\:\s", "", title, flags=re.I)
    clean_that = re.sub("\Athat\s|\Aof\s|\Aabout\s", "", clean_title, flags=re.I)
    if not clean_that[0].isupper():
        clean = clean_that[0].upper() + clean_that[1:]
    else:
        clean = clean_that
    return clean


def log_facts(post_list):
    file = open("facts.txt", "a")
    for item in post_list:
        file.write(item["title"] + ", by " + item["author"] + " for a score of " + str(item["upvotes"]) +
                   ". Links to: " + item["url"] + "\n")
    file.close()


def new_twitter_session():
    # ty to https://github.com/jg-fisher/theModelBot/blob/master/the-model-bot.py for help with this bit
    auth = tp.OAuthHandler(TW_ID, TW_SECRET)
    auth.set_access_token(TW_ACCESS_ID, TW_ACCESS_SECRET)
    twitter = tp.API(auth)
    return twitter


def post_to_twitter(twitter, post_list):
    for post in post_list:
        # todo work out how to format text, to include a link with text, the user profile etc
        # todo also check if this will post to my twitter feed or a new one?
        # noinspection PyBroadException
        try:
            twitter.update_status(post["title"])
            time.sleep(5)
        except Exception as e:
            file = open("log.txt", "a")
            file.write(post["title"] + "raised an error: " + str(e))
            file.close()


def main():
    delete_old_files()
    print("Welcome to the TIL fact finder")
    reddit = new_reddit_session()
    twitter = new_twitter_session()
    big_list = {}
    while True:
        print("checking...")
        new_posts = new_check(reddit)
        file_add_list = []
        for post, values in new_posts.items():
            if post not in big_list.keys():
                big_list.update({post: values})
                file_add_list.append(values)
        print("adding to facts.txt...")
        log_facts(file_add_list)
        print("posting to twitter and waiting for next check....\n")
        post_to_twitter(twitter, file_add_list)
        wait_minus_posting = 60 - (int(len(file_add_list)) * 5)
        if wait_minus_posting < 0:
            pass
        else:
            time.sleep(int(wait_minus_posting))


if __name__ == '__main__':
    main()

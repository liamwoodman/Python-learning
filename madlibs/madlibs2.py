# Mad Libs Story Maker
# Ever played Mad Libs? If you haven't, here are the basics:
#
# "Mad Libs consist of a book that has a short story on each page with many key words replaced with blanks.
# Beneath each blank is specified a lexical or other category, such as "noun," "verb," "place," or "part of the body."
# One player asks the other players, in turn, to contribute some word for the specified type for each blank,
# but without revealing the context for that word. Finally, the completed story is read aloud.
# The result is usually comic, surreal and somewhat nonsensical."
#
# Create a Mad Libs style game, where the program asks the user for certain types of words, and then
# prints out a story with the words that the user inputted.
# The story doesn't have to be too long, but it should have some sort of story line.
# Tip: it's easiest to write out a quick story on a piece of paper or a word document, and then go back
# through and see which words the user should be able to change.

# Subgoals:
# If the user has to put in a name, change the first letter to a capital letter.
# Change the word "a" to "an" when the next word in the sentence begins with a vowel.
#
# SELF CHALLENGE - Make an app that handles 'Madlibs files' or built in set of say 3 madlibs and calls one at random, then asks for the words
# based on the format of the chosen madlib
# Does the trick buy can't do a to an as spec'd. Would have to think of a way to do it outside of the dict mb?
# Or mb do a string checker for a's and an's using a regex search?
import time
import random
import json


def words(num):
    key_fn = "story/key" + str(num) + ".txt"
    key_file = open(key_fn, "r")
    file_read = key_file.read()
    key_list = json.loads(file_read)
    for x in key_list:
        user_value = input(key_list[x] + ": ")
        if x[:-1] == "name":
             if not user_value[0].isupper():
                 user_value.capitalize()
        key_list[x] = user_value
    return key_list


def story(user_words, num):
    story_fn = "story/story" + str(num) + ".txt"
    chosen_story = open(story_fn, "r")
    madlib = str(chosen_story.read())
    for x in user_words:
        print(user_words[x])
        madlib = madlib.replace(str(x), str(user_words[x]))
    return(madlib)


def main():
    print("\nWelcome to the Star Wars Madlibs generator.\n")
    time.sleep(2)
    rng = random.randint(1, 2)
    returned_words = words(rng)
    new_madlib = story(returned_words, rng)
    print("\nHere's your Madlib!\n\n" + new_madlib)


if __name__ == "__main__":
    main()
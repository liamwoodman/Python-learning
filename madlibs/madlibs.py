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
#
import time

VOWELS = ['a', 'e', 'i', 'o', 'u']

def words():
    name1 = input("Please enter a name: ")
    if not name1[0].isupper():
        name1 = name1.capitalize()
    group1 = input("Enter the name of the first group: ")
    group2 = input("Now enter the name of a second group: ")
    if group2[0].lower() in VOWELS:
        prep1 = "an"
    else:
        prep1 = "a"
    adj1 = input("Enter an adjective: ")
    adj2 = input("And another adjective: ")
    adj3 = input("And one more adjective: ")
    noun1 = input("Give me a noun: ")
    noun2 = input("And another noun: ")
    noun3 = input("And another noun: ")
    opp1 = input("Give me a noun that has an opposite: ")
    opp2 = input("Now give me the name of that opposite: ")
    verb1 = input("Give me a past-tense verb: ")
    words_list = {
                "name1": name1, "group1": group1, "group2": group2, "prep1": prep1, "adj1": adj1, "adj2": adj2,
                "adj3": adj3, "noun1": noun1, "noun2": noun2, "noun3": noun3, "opp1": opp1, "opp2":opp2, "verb1": verb1
                }
    print(words_list)
    return words_list

def story(user_words):
    chosen_story = open("story.txt", "r")
    madlib = str(chosen_story.read())
    for x in user_words:
        print(user_words[x])
        madlib = madlib.replace(str(x), str(user_words[x]))
    return(madlib)


def main():
    print("\nWelcome to the Darth Plagueis the Madlibs generator.\n")
    time.sleep(2)
    returned_words = words()
    new_madlib = story(returned_words)
    print("\nHere's your Madlib!\n\n" + new_madlib)


if __name__ == "__main__":
    main()
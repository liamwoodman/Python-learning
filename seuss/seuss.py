"""
Count and Fix Green Eggs and Ham

Some of you may remember the Dr. Suess story "Green Eggs and Ham". For those of you that don't remember it or have never heard of it,
here is the story. However, there is a problem with the story I gave you - every time the word I is used, it is lowercase.
Because of this problem, your job is to do the following:

Copy the story I gave you into a regular text file.

Create a program that reads through the story and makes the letter i uppercase any time it should be. (Make sure to change it when it's used in
sam-I-am's name too.)
Have your program make a new file, and have it write out the story correctly.

Print out how many errors were corrected.

When you're finished, you should have corrected 70 errors.
"""
import sys
import re

def arg_check(args):
    if not len(args) == 2:
        print("Incorrect command. Usage: <textfile.txt>")
        exit(1)
    elif not args[1].endswith('.txt'):
        print("No text file found. Please try again.")
        exit(2)
    else:
        return args[1]


def import_text(fn):
    file = open(fn, "r")
    text = file.readlines()
    file.close()
    return text

def change_replace(text):
    new_text = []
    result_list = []
    total = 0
    for line in text:
        result = re.findall("i | i |-i-", line)
        result_list.append(result)
        total += len(result)
        change = re.sub("i | i |-i-", caps, line)
        new_text.append(change)
    print(str(len(result_list)))
    return(new_text, total)


def caps(matchobj):
    if matchobj.group(0) == "i ":
        return "I "
    elif matchobj.group(0) == " i ":
        return " I "
    elif matchobj.group(0) == "-i-":
        return "-I-"

def export_text(text, fn):
    new_fn = "new_" + fn
    new_file = open(new_fn, "w")
    for line in text:
        new_file.write(line)
    print("The new file has been written and included. It is called " + str(new_fn) + ".")

def main():
    FN = arg_check(sys.argv)
    in_text = import_text(sys.argv[1])
    new_text, total = change_replace(in_text)
    export_text(new_text, FN)
    print("There were " + str(total) + " substitutions in total.")




if __name__ == "__main__":
    main()
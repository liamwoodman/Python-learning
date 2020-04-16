#Mean, Median, and Mode
#In a set of numbers, the mean is the average, the mode is the number that occurs the most, and if you rearrange all the numbers numerically,
#the median is the number in the middle.

#Create three functions that allow the user to find the mean, median, and mode of a list of numbers.
#If you have access or know of functions that already complete these tasks, do not use them.

#Subgoals
#In the mean function, give the user a way to select how many decimal places they want the answer to be rounded to.
#If there is an even number of numbers in the list, return both numbers that could be considered the median.
#If there are multiple modes, return all of them.
#
# Challenge
# Pass all data to a JSON type file and pass to a print function.
# Done - would be interesting to index back into

from collections import Counter
import json

def mean(num_list):
    mean_calc = float(sum(num_list)) / len(num_list)
    d = int(ask())
    rounded = round(mean_calc, int(d))
    return rounded, d

def median(num_list):
    num_list.sort()
    list_len = int(len(num_list))
    if (list_len % 2) == 0:
        even = True
        median = [num_list[int((list_len / 2) - 1)], num_list[int(list_len / 2)]]
    else:
        even = False
        even_calc = int(list_len / 2)
        median = num_list[even_calc]
    return median, even

def mode(num_list):
    mode_calc = Counter(num_list).most_common()
    mode = []
    high_val = mode_calc[0][1]
    multi_mode = False
    for counter, option in enumerate(mode_calc):
        if mode_calc[counter][1] == high_val:
            mode.append(option)
            multi_mode = True

    return mode, multi_mode

def result_print(data):
    # For printing mean
    mean_print = "The mean is " + str(data['mean']['val']) + ", rounded to " + str(data['mean']['rounding']) + " decimal places.\n"
    # For printing median
    if data['median']['is_even'] == True:
        if data['median']['val'][0] == data['median']['val'][1]:
            median_print = "There are two medians. They are both " + str(data['median']['val'][0]) + ".\n"
        else:
            median_print = "There are two medians. They are " + str(data['median']['val'][0]) + " and " + str(data['median']['val'][1]) + ".\n"
    elif data['median']['is_even'] == False:
        median_print = "The median is " + str(data['median']['val']) + ".\n"
    # For printing modes
    if data['mode']['is_many'] == True:
        mode_print = "There are multiple modes, each with a count of " + str(data['mode']['val'][1][1]) + ". These are "
        for count, option in enumerate(data['mode']['val']):
            if count == (len(data['mode']['val']) - 1):
                mode_print += "and " + str(option[0]) + "."
            elif count == 0 and len(data['mode']['val']) == 2:
                mode_print += str(option[0]) + " "
            else:
                mode_print += str(option[0]) + ", "
    else:
        mode_print = "The mode is " + str(data['mode']['val'][0]) + "with a count of " + str(data['mode']['val'][1]) + ".\n"
    print(mean_print + median_print + mode_print)


def get_nums():
    nums = input("Please enter a list of numbers seperated by a comma:\n")
    unformat_list = list(nums.split(","))
    num_list = []
    for x in unformat_list:
        if x.isdigit():
            num_list.append(float(x))
        else:
            print("\nBad entry detected. Please enter your number list again.\n")
            get_nums()
    return num_list

def ask():
    bad_input = True
    while bad_input:
        user_num = input("How many places would you like to round the number to?: ")
        if not user_num.isnumeric():
            print("\nBad entry detected. Please enter your number again.\n")
        else:
            bad_input = False
    return int(user_num)


def main():
    print("\nWelcome to the Averages calculator.\n")
    nums = get_nums()
    mean_val, mean_round = mean(nums)
    median_val, even = median(nums)
    mode_val, multi = mode(nums)
    data = {
            "mean" :{"val": mean_val, "rounding": mean_round},
            "median" : {"val": median_val, "is_even": even},
            "mode" : {"val": mode_val, "is_many": multi}
            }
    result_print(data)

if __name__ == "__main__":
    main()
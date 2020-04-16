# Change Calculator
#Imagine that your friend is a cashier, but has a hard time counting back change to customers.
#Create a program that allows him to input a certain amount of change, and then print how how many quarters,
#dimes, nickels, and pennies are needed to make up the amount needed. Example: if he inputs 1.47,
#the program will say that he needs 5 quarters, 2 dimes, 0 nickels, and 2 pennies.

#Subgoals:
#So your friend doesn't have to calculate how much change is needed, allow him to type in the amount of money given to him
#and the price of the item. The program should then tell him the amount of each coin he needs like usual.
#To make the program even easier to use, loop the program back to the top so your friend can continue to use
#the program without having to close and open it every time he needs to count change.


def change(change_val):
    change_dict = {
        "Quarter": {"val": 0.25, "num": 0},
        "Nickel": {"val": 0.10, "num": 0},
        "Dime": {"val": 0.05, "num": 0},
        "Penny": {"val": 0.01, "num": 0}
        }

    for x in change_dict:
        while change_val >= float(change_dict[x]["val"]):
            change_dict[x]["num"] += 1
            change_val -= float(change_dict[x]["val"])
    return change_dict

def money():
    money_dict = {
        "given": {"prompt" : "How much money was given", "val" : 0.00},
        "total": {"prompt" : "What was the total bill", "val" : 0.00}
    }

    for x in money_dict:
        bad_value = True
        while bad_value == True:
            val = input(money_dict[x]["prompt"] + "?: ")
            if val.isalpha():
                print("\nA non-numeric value was detected, please try again.\n")
                bad_value = True
            elif float(val) <= 0.00:
                print("\nA value less than or equal to zero was dectected, please try again.\n")
                bad_value = True
            else:
                bad_value = False
        money_dict[x]["val"] = float(val)
    if money_dict["total"]["val"] > money_dict["given"]["val"]:
        print("The total is greater than the money given! Check values and try again.\n")
        money()
    return money_dict

def change_print(val):
    message = "\nYou will need to give the following change: \n"
    for x in val:
        if val[x]["num"] <= 0:
            continue
        elif val[x]["num"] == 1:
            change_msg = str(val[x]["num"]) + " " + str(x) + "\n"
            message += change_msg
        elif val[x]["num"] >= 1 and x == "Penny":
            change_msg = str(val[x]["num"]) + " " + str(x)[:-1] + "ies \n"
            message += change_msg
        else:
            change_msg = str(val[x]["num"]) + " " + str(x) + "s\n"
            message += change_msg

    print(message)

def again():
    check = input("Would you like to calculate more change? Y/N: ")
    if check.lower() == "y":
        pass
    elif check.lower() == "n":
        exit(1)
    else:
        print("Please press either Y or N")
        again()

def main():
    print("\nWelcome to the Coin Change Calculator\n")
    while True:
        user_values = money()
        change_needed = float(round((user_values["given"]["val"] - user_values["total"]["val"]), 2))
        change_calc = change(change_needed)
        change_print(change_calc)
        again()

if __name__ == "__main__":
    main()
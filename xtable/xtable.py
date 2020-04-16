#Multiplication Table
#Create a program that prints out a multiplication table for the numbers 1 through 9.
#It should include the numbers 1 through 9 on the top and left axises, and it should be relatively easy to find
# the product of two numbers. Do not simply write out every line manually (ie print('7 14 21 28 35 49 56 63') ).
#Subgoals:
#As your products get larger, your columns will start to get crooked from the number of characters on each line.
#Clean up your table by evenly spacing columns so it is very easy to find the product of two numbers.
#
#Allow the user to choose a number to change the size of the table (so if they type in 12,
#the table printed out should be a 12x12 multiplication table).

def table(num):
    max_len = len(str(num ** 2))
    xtable = ""
    num_range = range(1, num + 1)
    for x in num_range:
        xtable += "\n"
        for y in num_range:
            xtable += formatting(str(y * x), max_len)
    print(xtable)

def formatting(num, max_len):
    num_len = len(str(num))
    str_format = "| " + str(num) + " " + (" " * (max_len - num_len )) + "|"
    return str(str_format)

def ask():
    bad_input = True
    while bad_input:
        user_num = input("Please enter a number for your multiplication table: ")
        if not user_num.isnumeric():
            print("\nNo number entered. Please enter your number again.\n")
        else:
            bad_input = False
    return int(user_num)

def main():
    print("Welcome to the timestable creator.\n\n")
    number = ask()
    table(number)

if __name__ == "__main__":
    main()
#Base Jumper
#Create a program that converts an integer to the specified base.
#The program should ask for 3 inputs. The number to convert. The base the number is in. And the base to convert the number to.
#The program should accept a base that is in the range of 2 to 16 inclusive.
#Display the result to the user and ask if they want to exit or convert another number.
#Subgoals:
#Do not display leading zero's in the result.
#Validate that the number entered is valid for the specified base


# vvv difficult for non mather like me - here's good start https://codeigo.com/python/parse-string-to-int-base
import math

def base_jump(data):
    characters="0123456789abcdefghijklmnopqrstuvwxyz"
    num_ten = int(str(data["val"]), data["old"])

    result = ''
    while num_ten:
        result = characters[num_ten % (data["new"])] + result
        num_ten //= data["new"]

    return result

def ask(question, range_check):
    bad_input = True
    while bad_input:
        user_num = input(question)
        if not user_num.isnumeric():
            print("\nBad entry detected. Please enter your number again.\n")

        if range_check == True:
            if int(user_num) < 2 or int(user_num) > 16:
                print("\nBad entry detected. Please enter your number again. It must be between 2 and 16.\n")
            else:
                bad_input = False
        else:
            bad_input = False
    return int(user_num)

def main():
    print("\nWelcome to the base jumper application.\n")
    number = ask("What is the number to be converted?: ", False)
    current_base = ask("What base is the current number in?: ", True)
    requested_base = ask("What base would you like the number to be in?: ", True)
    data = {
        "val": number,
        "old": current_base,
        "new": requested_base
    }
    result = base_jump(data)
    print(str(number) + " in base " + str(requested_base) + " is " + str(result) + ".")

if __name__ == "__main__":
    main()
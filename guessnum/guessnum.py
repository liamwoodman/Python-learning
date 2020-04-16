"""
What’s My Number?
Between 1 and 1000, there is only 1 number that meets the following criteria:

The number has two or more digits.
The number is prime.
The number does NOT contain a 1 or 7 in it.
The sum of all of the digits is less than or equal to 10.
The first two digits add up to be odd.
The second to last digit is even and greater than 1.
The last digit is equal to how many digits are in the number.
To find out if you have the correct number, click here.
"""

def len_check(num):
    if len(str(num)) < 2:
        return False
    else:
        return True


def prime_check(num):
    #great idea here - https://www.programiz.com/python-programming/examples/prime-number, using modulo :D
    check_list = []
    for x in range(1, num):
        if (num % x) == 0:
            check_list.append(x)
        else:
            pass
    if len(check_list) > 1:
        return True
    else:
        return False

def one_seven_check(num):
    num_list = []
    for number in str(num):
        num_list.append(number)
    #check this
    print(num_list)
    if "1" or "7" in num_list:
       check_state = False
    else:
        check_state = True

    if check_state == True:
        print(num)
        return True
    else:
        return False

def sum_ten(num):
    sum_list = []
    for check in str(num):
        sum_list.append(int(check))
    summed = sum(sum_list)
    if summed > 10:
        return True
    else:
        return False

def first_two_sum(num):
    check = str(num)
    num_check = check[0:2]
    check_list = []
    for number in num_check:
        check_list.append(int(number))
    val = sum(check_list)
    if (val % 2) == 0:
        return False
    else:
        return True

def last_numbers(num):
    num_len = len(str(num))
    num_str = str(num)
    if num_len > 2:
        val = num_str[-num_len:-(num_len - 2)]
        check_num = int(val[0:1])
        check_last_num = int(val[:-1])
    else:
        check_num = num_str[0:1]
        check_last_num = num_str[:-1]

    if not int(check_num) > 1 and (int(check_num) % 2) == 0:
        return False
    elif not check_last_num == num_len:
        return False
    else:
        return True

def main():
    num_list = []
    for num in range(1, 1000):
        num_list.append(num)

# Need to fix this for loop - something strange happening - falses not killing the loop
    answer_list = []
    for check_num in num_list:
        check_one = len_check(check_num)

        if check_one == False:
            continue
        else:
            check_two = prime_check(check_num)
        if check_two == False:
            continue
        else:
            check_three = one_seven_check(check_num)
        if check_three == False:
            continue
        else:
            check_four = sum_ten(check_num)
        if check_four == False:
            continue
        else:
            check_five = first_two_sum(check_num)
        if check_five == False:
            continue
        else:
            check_six = last_numbers(check_num)
        if check_six == False:
            continue
        else:
            answer_list.append(check_num)

    print(answer_list)

    #for num in num_list:
        #while skip:


if __name__ == "__main__":
    main()
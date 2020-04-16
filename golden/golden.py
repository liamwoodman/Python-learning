#Fibonacci Sequence
#If you do not know about the Fibonacci Sequence, read about it here.

#Define a function that allows the user to find the value of the nth term in the sequence.
#To make sure you've written your function correctly, test the first 10 numbers of the sequence.
#You can assume either that the first two terms are 0 and 1 or that they are both 1.
#There are two methods you can employ to solve the problem. One way is to solve it using a loop
#and the other way is to use recursion.
#
#Try implementing a solution using both methods.

def fib_loop(n):
    a = 0
    b = 1
    for x in range(1, n):
        y = a + b
        a = b
        b = y
    return b

def fib_rec(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

def ask():
    bad_input = True
    while bad_input:
        user_num = input("Please the place in the sequence you'd like to find: ")
        if not user_num.isnumeric():
            print("\nBad entry detected. Please enter your number again.\n")
        else:
            bad_input = False
    return int(user_num)

def main():
    print("\nWelcome to the Fibonacci Finder\n")
    num = ask()
    output = str(fib_rec(num))
    print("The number in position " + str(num) + " is " + output)

if __name__ == "__main__":
    main()
#Higher Lower Guessing Game
#
#Create a simple game where the computer randomly selects a number between 1 and 100 and the user has to guess what the number is.
#After every guess, the computer should tell the user if the guess is higher or lower than the answer.
#When the user guesses the correct number, print out a congratulatory message.
#
#Subgoals:
#Add an introductory message that explains to the user how to play your game.
#In addition to the congratulatory message at the end of the game, also print out how many
#guesses were taken before the user arrived at the correct answer.
#At the end of the game, allow the user to decide if they want to play again (without having to restart the program).
import random

def guess(num):
    guess_count = 1
    user_guess = ask(guess_count)
    while not user_guess == num:
        if user_guess < num:
            print("\nMy number is higher...\n")
            guess_count += 1
            user_guess = ask(guess_count)
        elif user_guess > num:
            print("\nMy number is lower...\n")
            guess_count += 1
            user_guess = ask(guess_count)
    print("\nYou are the winner. The number was " + str(num) +
            "! You guessed " + str(guess_count) + " times.\n")

def ask(guesses):
    bad_input = True
    while bad_input:
        if guesses == 1:
            user_guess = input("\nWhat is your guess?: ")
        else:
            user_guess = input("What is your next guess?: ")

        if not user_guess.isnumeric():
            print("\nNo number entered. Please enter your number again.\n")
        else:
            bad_input = False
    return int(user_guess)

def again():
    check = input("Would you like to play again? Y/N: ")
    if check.lower() == "y":
        pass
    elif check.lower() == "n":
        exit(1)
    else:
        print("Please press either Y or N")
        again()

def main():
    print("\nWelcome to the Number Guessing Game!\n\nI will think of a number from 1-100. "
            "Guess the number and I will tell you if it's higher or lower. Guess my number and you win!\n")
    while True:
        rng = random.randint(1, 100)
        guess(rng)
        again()

if __name__ == "__main__":
    main()
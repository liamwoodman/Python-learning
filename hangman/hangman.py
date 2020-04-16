#Hangman Game
#Create a program that selects a random word and then allows the user to guess it in a game of hangman.
#Like the real game, there should be blank spots for each letter in the word, and a part of the body
#should be added each time the user guesses a letter than is not in the answer.
#You may choose how many wrong turns the user can make until the game ends.
#Subgoals:
#If the user loses, print out the word at the end of the game.
#Create a "give up" option.
import random

CPU_WINS = 0
PLA_WINS = 0

def hang(word):
    man = {
        0: "_________",
        1: " |/      |",
        2: " |     (T_T)",
        3: " |      \|/",
        4: " |      / \\",
        5: " |",
        6: "_|___\n  GAME OVER! ",
    }
    blanks = []
    word_list = []

    for x in range(len(word)):
        blanks += "_"
        word_list.append(word[x])

    correct = False
    correct_count = 0
    guess_num = 0
    guesses = []
    while guess_num < (len(man)):
        print("Your word:\n\n" + " ".join(blanks) + "\n")
        guess = ask(guess_num)
        if guess in guesses:
            print("\nYou've guessed this already! Please guess again.\n")
            guess = ask(guess_num)
        for i, x in enumerate(word_list):
            if x == guess:
                blanks[i] = guess
                correct = True
                correct_count += 1
        if correct == True:
            if correct_count == 1:
                print("\nCorrect! " + guess.upper() + " appears " + str(correct_count) + " time.\n")
            else:
                print("\nCorrect! " + guess.upper() + " appears " + str(correct_count) + " times.\n")
            correct_count = 0
            correct = False
            if word_list == blanks:
                return True
            else:
                pass
        else:
            guess_num += 1
            guess_calc = len(man) - guess_num
            if guess_calc == 1:
                print("\nWrong! You have " + str(guess_calc) + " guess left.\n")
            else:
                print("\nWrong! You have " + str(guess_calc) + " guesses left.\n")
            for x in range((guess_num)):
                print(man[x])
            print("\n")
        guesses.append(guess)
    return False

def ask(num):
    bad_input = True
    while bad_input:
        if num == 0:
            guess = input("Guess number " + str(num + 1) + ". What letter would you like to guess?: ")
        else:
            guess = input("Guess number " + str(num + 1) + ". What letter would you like to guess?: ")
        if not guess.isalpha():
            print("\nBad entry detected. Please enter your letter again.\n")
        else:
            bad_input = False
    return str(guess.lower())

def ask_new():
    new_game = input("Would you like to play again? (Y/N): ")
    if new_game.lower() == "y":
        print("\n")
        pass
    elif new_game.lower() == "n":
        exit()
    else:
        print("\nBad entry detected. Please enter your choice again.\n")
        ask_new()

def word_list():
    file = open("words.txt", "r")
    words = file.readlines()
    word = words[random.randint(1, len(words))].rstrip()
    file.close()
    return word


def main():
    global CPU_WINS, PLA_WINS
    print("\nWelcome to Hangman!")
    while True:
        word = word_list()
        winner = hang(word)
        if winner == True:
            PLA_WINS += 1
            print("Congratulations! You win. Your score is: " + str(PLA_WINS) + ". The computer's is: " + str(CPU_WINS) + ".\n")
        else:
            CPU_WINS += 1
            print("Sorry, you lose! The word was" + word + "Your score is: " + str(PLA_WINS) + ". The computer's is: " + str(CPU_WINS) + ".\n")
        ask_new()

if __name__ == "__main__":
    main()
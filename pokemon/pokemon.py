# Write a simple game that allows the user and the computer to take turns selecting moves to use against each other.
# Both the computer and the player should start out at the same amount of health (such as 100), and should be able to
# choose between the three moves:
# The first move should do moderate damage and has a small range (such as 18-25).
# The second move should have a large range of damage and can deal high or low damage (such as 10-35).
# The third move should heal whoever casts it a moderate amount, similar to the first move.
# After each move, a message should be printed out that tells the user what just happened, and how much health the user
# and computer have. Once the user or the computer's health reaches 0, the game should end.

# Subgoals:
# When someone is defeated, make sure the game prints out that their health has reached 0, and not a negative number.
# When the computer's health reaches a set amount (such as 35%), increase it's chance to cast heal.
# Give each move a name

import random
import inquirer
import time


# MOVES = {1: {"name": "Slash", "dmg": random.randint(18, 25)},
#          2: {"name": "Lunge", "dmg": random.randint(10, 35)},
#          3: {"name": "Prayer", "dmg": int(round(random.uniform(-15, -25), 0))}
#          }


class Fighter:
    health = 100
    moves = {1: {"name": "Slash", "dmg": random.randint(18, 25)},
             2: {"name": "Lunge", "dmg": random.randint(10, 35)},
             3: {"name": "Prayer", "dmg": int(round(random.uniform(-15, -25), 0))}
             }


class Player:
    def __init__(self, name: str, order: bool):
        self.name = name
        self.order = order
        self.health = Fighter.health
        self.moves = Fighter.moves

    def mod_health(self, dmg_val):
        self.health -= dmg_val

    def deal_dmg(self, is_cpu):
        if is_cpu and self.health > 35:
            high_hp_choice = random.randint(1, 3)
            rng_choice = MOVES[high_hp_choice]["dmg"]
            return rng_choice
        elif is_cpu and self.health < 35:
            low_hp_choice = random.choices(population=MOVES,
                                           weights=[0.25, 0.25, 0.5], k=1)
            rng_choice = MOVES[low_hp_choice]["dmg"]
            return rng_choice

        else:
            move_choice = [
                inquirer.List('attack',
                              message='Which move would you like to chose?',
                              choices=['1. Slash, 18 - 25 dmg',
                                       '2. Lunge, 10 - 35 dmg',
                                       '3. Prayer, 10 - 20 healed'],
                              ),
            ]
            move_chosen = inquirer.prompt(move_choice)

            move_list = move_chosen['attack'].split(".")
            move_num = move_list[0]
            move_val = MOVES[int(move_num)]["dmg"]
            return move_val


def calc_dmg(move_num):
    if move_num == 1:
        dmg = random.randint(18, 25)
    elif move_num == 2:
        dmg = random.randint(10, 35)
    else:
        dmg = int(round(random.uniform(-15, -25), 0))
    return dmg



def coin_flip():
    side_choice = [
        inquirer.List('side',
                      message="Heads or tails?",
                      choices=['Heads',
                               'Tails']
                      )
    ]
    side_chosen = inquirer.prompt(side_choice)

    if side_chosen['side'] == 'Tails':
        coin_val = 0
    else:
        coin_val = 1
    flip = random.randint(0, 1)

    if flip == coin_val:
        print("You won the coin flip. You will attack first.")
        return True
    else:
        print("You lost the coin flip. You will attack second.")
        return False


def play_again():
    again = input("Would you like to play again? Y/N")
    if again.lower() == 'y':
        pass
    elif again.lower() == 'n':
        exit(1)
    else:
        play_again()


def main():
    print("Welcome to the battle game!")
    user_name = input("\nWhat is your name?\n")
    cpu_name = input("\nAnd what is your enemies name?\n")
    while True:
        user_order = coin_flip()
        user = Player(user_name, user_order)
        cpu_order = not user_order
        cpu = Player(cpu_name, cpu_order)
        user_alive = True
        cpu_alive = True

        while user_alive and cpu_alive:
            user_move = user.deal_dmg(False)
            cpu_move = cpu.deal_dmg(True)
            if user.order:
                if user_move > 0:
                    cpu.mod_health(user_move)
                    print("You attack " + cpu.name + " for " + str(user_move) + " points of damage! " + cpu.name +
                          " now has " + str(cpu.health) + " HP left.")
                else:
                    user.mod_health(user_move)
                    print("You pray to your gods and they grant you a blessing, restoring " + str(abs(user_move)) +
                          " hit points. You now have " + str(user.health) + " HP.")
                time.sleep(2)
                if cpu_move > 0:
                    user.mod_health(cpu_move)
                    print(cpu.name + " attacks you for " + str(user_move) + " points of damage! " + user.name +
                          " now has " + str(cpu.health) + " HP left.")
                else:
                    cpu.mod_health(cpu_move)
                    print(cpu.name + " performs a dark incantation to their Eldridge gods and is granted a vile "
                                     "blessing, restoring them by " + str(abs(cpu_move)) + ". They are now at " +
                          str(cpu.health) + " HP.")
            else:
                if cpu_move > 0:
                    user.mod_health(cpu_move)
                    print(cpu.name + " attacks you for " + str(user_move) + " points of damage! " + user.name +
                          " now has " + str(cpu.health) + " HP left.")
                else:
                    cpu.mod_health(cpu_move)
                    print(cpu.name + " performs a dark incantation to their Eldridge gods and is granted a vile "
                                     "blessing, restoring them by " + str(abs(cpu_move)) + ". They are now at " +
                          str(cpu.health) + " HP.")

                time.sleep(2)
                if user_move > 0:
                    cpu.mod_health(user_move)
                    print("You attack " + cpu.name + " for " + str(user_move) + " points of damage! " + cpu.name +
                          " now has " + str(cpu.health) + " HP left.")
                else:
                    user.mod_health(user_move)
                    print("You pray to your gods and they grant you a blessing, restoring " + str(abs(user_move)) +
                          " hit points. You now have " + str(user.health) + " HP.")

            if user.health < 0:
                user_alive = False
                print("You have sustained critical damage and have fainted on the battlefield! " + user.name +
                      " is no more!")
                break
            elif cpu.health < 0:
                cpu_alive = False
                print(cpu.name + " has sustained critical damage and has fainted on the battlefield! " + user.name +
                      "is victorious")
                break
    play_again()


if __name__ == '__main__':
    main()

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

# TO/DO - 27th March
# Check death watch loop
# Clean up spacing
# if refactoring, combat and vals in a dict

import random
import inquirer
import time


# MOVES = {1: {"name": "Slash", "dmg": random.randint(18, 25)},
#          2: {"name": "Lunge", "dmg": random.randint(10, 35)},
#          3: {"name": "Prayer", "dmg": int(round(random.uniform(-15, -25), 0))}
#          }


class Fighter:
    health = 100
    moves = {1: {"name": "Slash"},
             2: {"name": "Lunge"},
             3: {"name": "Prayer"}
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
        if is_cpu and self.health > 20:
            # print("CPU high health")
            choice = random.choices(population=list(self.moves),
                                    weights=[0.4, 0.4, 0.2], k=1)
            dmg_val = calc_dmg(int(choice[0]))
            return dmg_val, choice

        elif is_cpu and self.health < 20:
            # print("CPU low health")
            choice = random.choices(population=list(self.moves),
                                    weights=[0.25, 0.25, 0.5], k=1)
            dmg_val = calc_dmg(int(choice[0]))
            return dmg_val, choice

        else:
            move_choice = [
                inquirer.List('attack',
                              message='Which move would you like to chose?',
                              choices=['1. Slash, 25 - 30 dmg',
                                       '2. Lunge, 20 - 45 dmg',
                                       '3. Prayer, 15 - 25 healed'],
                              ),
            ]
            move_chosen = inquirer.prompt(move_choice)

            move_list = move_chosen['attack'].split(".")
            move_num = move_list[0]
            dmg_val = calc_dmg(int(move_num))
            return dmg_val, move_num

    def fatal_dmg(self, user: bool):
        print("checking!")
        if self.health <= 0 and user:
            print("You have sustained critical damage and have fainted on the battlefield! " + self.name +
                  " is no more!")
            return True
        elif self.health <= 0 and not user:
            print(self.name + " has sustained critical damage and has fainted on the battlefield! You are victorious")
            return False
        else:
            print('check complete, no-one dead')
            return True


def calc_dmg(move_num):
    if move_num == 1:
        dmg = random.randint(25, 30)
    elif move_num == 2:
        dmg = random.randint(20, 45)
    elif move_num == 3:
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
        print("You won the coin flip. You will attack first.\n")
        return True
    else:
        print("You lost the coin flip. You will attack second.\n")
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
        time.sleep(1)
        user = Player(user_name, user_order)
        cpu_order = not user_order
        cpu = Player(cpu_name, cpu_order)
        combat = True

        while user.health > 0 or cpu.health > 0:

            user_move, user_choice = user.deal_dmg(False)
            cpu_move, cpu_choice = cpu.deal_dmg(True)

            if user.order:
                if user_move > 0:
                    cpu.mod_health(user_move)
                    print("You attack " + cpu.name + " for " + str(user_move) + " points of damage! "
                          + cpu.name + " now has " + str(cpu.health) + " HP left.\n")
                    combat = cpu.fatal_dmg(False)
                else:
                    user.mod_health(user_move)
                    print("You pray to your gods and they grant you a blessing, restoring " + str(abs(user_move)) +
                          " hit points. You now have " + str(user.health) + " HP.\n")
                time.sleep(2)
                if cpu_move > 0:
                    user.mod_health(cpu_move)
                    print(cpu.name + " attacks you for " + str(cpu_move) + " points of damage! " + user.name +
                          " now has " + str(user.health) + " HP left.\n")
                    combat = user.fatal_dmg(True)
                else:
                    cpu.mod_health(cpu_move)
                    print(cpu.name + " performs a dark incantation to their Eldridge gods and is granted a vile "
                                     "blessing, restoring them by " + str(abs(cpu_move)) + ". They are now at " +
                          str(cpu.health) + " HP.")
            else:
                if cpu_move > 0:
                    user.mod_health(cpu_move)
                    print(cpu.name + " attacks you for " + str(cpu_move) + " points of damage! " + user.name +
                          " now has " + str(user.health) + " HP left.\n")
                    combat = user.fatal_dmg(True)
                else:
                    cpu.mod_health(cpu_move)
                    print(cpu.name + " performs a dark incantation to their Eldridge gods and is granted a vile "
                                     "blessing, restoring them by " + str(abs(cpu_move)) + ". They are now at " +
                          str(cpu.health) + " HP.\n")

                time.sleep(2)
                if user_move > 0:
                    cpu.mod_health(user_move)
                    print("You attack " + cpu.name + " for " + str(user_move) + " points of damage! " + cpu.name +
                          " now has " + str(cpu.health) + " HP left.\n")
                    combat = user.fatal_dmg(False)
                else:
                    user.mod_health(user_move)
                    print("You pray to your gods and they grant you a blessing, restoring " + str(abs(user_move)) +
                          " hit points. You now have " + str(user.health) + " HP.\n")

            # if user.health < 0:
            #     user_alive = False
            #     print("You have sustained critical damage and have fainted on the battlefield! " + user.name +
            #           " is no more!")
            #     break
            # elif cpu.health < 0:
            #     cpu_alive = False
            #     print(cpu.name + " has sustained critical damage and has fainted on the battlefield! " + user.name +
            #           "is victorious")
            #     break
        play_again()


if __name__ == '__main__':
    main()

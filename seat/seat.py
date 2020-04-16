"""
Seat Reservation
If you've ever been in a concert, you are aware that you buy tickets to be able to reserve a seat inside
a stadium. The seat you will be on will have a specific number or code that would enable you to know exactly
how far or how close you are to the stage.

Note: if you are kind of uncomfortable with lists, here's a reference to get you started.

Create a simple seat reservation program

Create a list that would store dashes '-' as a symbol that the seat is still available to take.

Define a function that would loop over the list and print out the seats horizontally or in a 3 x 3 position.
Refer to this image for reference. https://image.shutterstock.com/image-vector/stadium-chairs-vector-icon-arenabench-260nw-1056480272.jpg

Define a second function that would check if the seats are occupied. This should check if the list contains
"X" in each element, which is the symbol that we will use if the seat is taken that you will store in a
variable. If the variable is equal to 9 (the total number of seats), return True (and break from the loop),
and False if not.

Create a loop that would have to (1) ask the user for the number of seat he would want to reserve,
(2) print out the chairs, (3) check if all the seats are occupied and
(4) ask the user now if he/she wants to reserve again.

Notes:

This is a bit of a silly problem and I think the writer is playing 'Whats in my head'. You are basically
creating a static file and need to run from that, thereby requiring at least some sort of database. I
might implement with a standard file and try that.

"""

import json

def load_seats():
    file = open("reservations.txt", "r")
    thea_map = file.read()
    THEATRE = json.loads(thea_map)
    file.close()
    return THEATRE

def seat_map(THEATRE):
    occupied = 0
    vacant = 0
    seat_map = "\n"

    for row, seats in THEATRE.items():
        for seat in seats:
            if seat[1] == True:
                seat_map += ("| " + row + str(seat[0]) + " X" + " | ")
                occupied += 1
            else:
                seat_map += ("| " + row +  str(seat[0]) + " -" + " | ")
                vacant += 1
        seat_map += ("\n")
    print(seat_map)
    return(vacant)

"""
def reserve():
    new_map = THEATRE.copy()
    reserved_seats = []
    while num  > 0:
        for row, seats in THEATRE.items():
            print(row, seats)
            for seat in seats:
                print(seat)
                if seat[1] == False:
                    print(THEATRE[row][seats])
                    reserved_seats.append(new_map[row][seats][seat])
                    new_map[row][seats][seat][1] == True
                    num -= 1
    return reserved_seats
"""

def ask():
    bad_input = True
    while bad_input:
        num = input("How many seats would you like to reserve?: ")
        if int(num) == 0:
            print("\nBad entry detected, please try again.\n")
        elif not num.isnumeric():
            print("\n\nBad entry detected, please try again.\n")
        else:
            bad_input = False
    return int(num)

def again():
    check = input("Would you like to request another reservation? Y/N: ")
    if check.lower() == "y":
        pass
    elif check.lower() == "n":
        exit()
    else:
        print("Please press either Y or N")
        again()

def main():
    print("\nWelcome to Seat Reservation\n")
    while True:
        THEATRE = load_seats()
        needed = ask()
        vacant = seat_map(THEATRE)
        if needed > vacant:
            print("Sorry, there are no spare seats for that many people")
            again()
        else:
            print("Yes, there are tickets available for that many people. Please come to the box office to purchase.")
            again()

if __name__ == "__main__":
    main()
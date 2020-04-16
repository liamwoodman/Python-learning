# Pythagorean Triples Checker
# If you do not know how basic right triangles work, or what a Pythagorean Triple is read these articles on Wikipedia¹ ².
# Allows the user to input the sides of any triangle in any order.
# Return whether the triangle is a Pythagorean Triple or not.
# Loop the program so the user can use it more than once without having to restart the program.

# Cheers to aekanshd for this - I def used his code as a basis for mine
# https://github.com/aekanshd/beginner-projects/blob/master/solutions/python/PythagoreanTheorem.py

def is_pi(a,b,c):
    if ((a**2 == (b**2 + c**2))) or ((b**2) == ((a**2 + c**2))) or ((c**2) == ((a**2 + b**2))):
        return "Yes, that is a Pythagorean Triple"
    else:
        return "No that's not a Pythagorean Triple"


def main():
    on_off = "y"
    while True:
        if on_off == 'n':
            break
        elif on_off == 'y':
            a,b,c = input("Enter three numbers seperated by a space: \n").split()
            a,b,c = int(a), int(b), int(c)
            print("Results: " + is_pi(a,b,c))
            on_off = input("Do you want to continue? Y/N: ").lower()
        else:
            print("Please enter only Y or N.")
            on_off = input("Do you want to continue? Y/N: ").lower()


if __name__ == "__main__":
    main()
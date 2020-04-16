#99 Bottles
#Create a program that prints out every line to the song "99 bottles of beer on the wall."
#Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
#Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
#Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

def main():

    bottles = 99
    while bottles > 0:
        if bottles > 1:
            bottle = str(bottles)
            song_line = bottle + " bottles of beer on the wall\n" + bottle + " bottles of beer!\n" + "Take one down, pass it around\n" + bottle + " bottles of beer on the wall!\n"
            print(song_line)
            bottles -= 1
        elif bottles == 1:
            bottle = str(bottles)
            song_line = bottle + " bottle of beer on the wall\n" + bottle + " bottle of beer!\n" + "Take one down, pass it around\n" + bottle + " bottle of beer on the wall!\n"
            print(song_line)
            bottles -=1

if __name__ == "__main__":
    main()

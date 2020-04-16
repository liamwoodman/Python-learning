# From Trebek on GitHub - https://github.com/Trebek/pydealer/blob/master/pydealer/const.py

SUITS = ["Diamonds", "Clubs", "Hearts", "Spades"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9","10",
         "Jack", "Queen", "King", "Ace"]
SCORES = {
        "King": 10,
        "Queen": 10,
        "Jack": 10,
        "10": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "Ace": 1
}

RANKS = {
    "A": (80, 100),
    "B": (60, 79),
    "C": (40, 59),
    "D": (20, 39),
    "E": (1, 19)
}
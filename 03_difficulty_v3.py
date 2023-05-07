"""Take 03_difficulty_v2 code out of a loop and into a function
turned into finished product
"""


def get_difficulty():
    loop = True
    while loop:
        diff = input("From 1-10, 1 being low, how confident are you with Maori numbers: ")

        try:
            diff = int(diff)
            if 6 <= diff <= 10:
                loop = False
                # Tell user what mode they are on
                print("You are playing on advanced mode")
            elif 1 <= diff <= 5:
                loop = False
                # Tell user what mode they are on
                print("You are playing on normal mode")
            else:
                print("Please enter an integer between 1 and 10")
        except ValueError:
            print("Please enter an integer between 1 and 10")


get_difficulty()
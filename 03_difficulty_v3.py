"""Take 03_difficulty_v2 code out of a loop and into a function
turned into finished product
"""


def get_difficulty():
    # Set loop
    loop = True
    while loop:
        # Ask user how confident they are with Maori numbers
        diff = input("From 1-10, 1 being low, how confident are you with Maori numbers: ")
        # Check for errors with "try"
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
                # If it is above or below the range (1-10), ask again
                print("Please enter an integer between 1 and 10")
        # When error detected, ask again
        except ValueError:
            print("Please enter an integer between 1 and 10")


# Test
get_difficulty()

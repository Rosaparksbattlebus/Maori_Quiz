"""Based on 03_difficulty_v1. Solves for invalid input (e.g. 11, 0.5)
and puts into loop for testing
"""


loop = True

while loop:
    diff = input("From 1-10, 1 being low, how confident are you with Maori numbers: ")

    try:
        diff = int(diff)
        if 6 <= diff <= 10:
            hard = True
            print(f"Hard = {hard}")
        elif 1 <= diff <= 5:
            hard = False
            print(f"Hard = {hard}")
        else:
            print("Please enter an integer between 1 and 10")
    except ValueError:
        print("Please enter an integer between 1 and 10")

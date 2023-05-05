"""Based on 03_difficulty_v1. Added output for invalid input and put it into a loop (e.g. 11, 0.5)
"""

loop = True

while loop:
    diff = input("From 1-10, 1 being low, how confident are you with Maori numbers: ")

    # Set difficulty to hard if they entered above 5
    if 6 <= int(diff) <= 10:
        hard = True
        loop = False
    elif 1 <= int(diff) <= 5:
        hard = False
        loop = False
    else:
        print("Please enter an integer between 1 and 10")

print(hard)

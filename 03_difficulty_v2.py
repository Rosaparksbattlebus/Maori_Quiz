"""Based on 03_difficulty_v1. Solves for invalid input (e.g. 11, 0.5)
and puts into loop for testing
"""

# Set loop
loop = True

while loop:
    # Ask user how confident they are with Maori numbers
    diff = input("From 1-10, 1 being low, how confident are you with Maori numbers: ")
    # Check for errors with "try"
    try:
        diff = int(diff)
        if 6 <= diff <= 10:
            hard = True
            # Print difficulty
            print(f"Hard = {hard}")
        elif 1 <= diff <= 5:
            hard = False
            # Print difficulty
            print(f"Hard = {hard}")
        else:
            # If it is above or below the range (1-10), ask again
            print("Please enter an integer between 1 and 10")
    # When error detected, ask again
    except ValueError:
        print("Please enter an integer between 1 and 10")

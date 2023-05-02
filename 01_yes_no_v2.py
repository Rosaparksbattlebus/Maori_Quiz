"""Simplifies the input by converting it into lower case.
 Also accepts 'y' and 'n' as abbreviations. Prints result of user choice."""

# Ask user if they have played before
show_instructions = input("Have you played this quiz before? Enter 'yes' or 'no': ").lower()

# If yes, print 'program continues'
if show_instructions == "yes" or "y":
    print("Program continues")

# If no, print 'Display instructions'
elif show_instructions == "no" or "n":
    print("Display instructions")

# Else, show error
else:
    print("Please answer 'Yes' or 'No'")


print(f"You entered '{show_instructions}'")
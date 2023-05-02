# Ask user if they have played before
show_instructions = input("Have you played this quiz before? Enter 'yes' or 'no': ").lower()

# If yes, print 'program continues'
if show_instructions == "yes":
    print("Program continues")

# If no, print 'Display instructions'
elif show_instructions == "no":
    print("Display instructions")

# Else, show error
else:
    print("Please answer 'Yes' or 'No'")



"""Took function from 01_yes_no_v3 as the base of this new function
which combines yes/no and show instructions"""


# Functions go here...
def yes_no(question_text):
    while True:
        # Ask user if they have played this quiz before
        answer = input(question_text).lower()

        # If yes, print 'program continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If no, print 'Display instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Else, show error
        else:
            print("Please answer 'Yes' or 'No'")


# Applying the function to the instructions
def instructions():
    print("---- How to Play ----")
    print()
    print("The rules of the quiz will go here")
    print()
    print("Program continues")
    print()


# Main routine go here...
played_before = yes_no("Have you played this quiz before? ")

if played_before == "No":
    instructions()
else:
    print("Program continues")

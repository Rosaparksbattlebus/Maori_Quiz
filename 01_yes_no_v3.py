"""Change the yes/no checker into a function"""


def yes_no(question):
    while True:
        # Lowercase the answer
        answer = input(question).lower()

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


# Testing it here
Day = yes_no("Has your day been good? ")
print(f"You entered {Day}")

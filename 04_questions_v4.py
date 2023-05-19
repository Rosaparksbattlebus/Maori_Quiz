"""Based on 04_questions_v3
Added input for hard/easy mode just for testing sake
Added second list of questions and answers for hard mode which includes 11-20 in Maori
Defined questions and answers in a dictionary
Implemented new score system for hard mode
"""


import random

# Define questions and answers in a dictionary
questions = {
    "1": "What is 1 in Maori?",
    "2": "What is 2 in Maori?",
    "3": "What is 3 in Maori?",
    "4": "What is 4 in Maori?",
    "5": "What is 5 in Maori?",
    "6": "What is 6 in Maori?",
    "7": "What is 7 in Maori?",
    "8": "What is 8 in Maori?",
    "9": "What is 9 in Maori?",
    "10": "What is 10 in Maori?"
}

answers = {
    "1": "tahi",
    "2": "rua",
    "3": "toru",
    "4": "wha",
    "5": "rima",
    "6": "ono",
    "7": "whitu",
    "8": "waru",
    "9": "iwa",
    "10": "tekau"
}

# Define the hard questions and answers in a dictionary
hard_questions = {
    "1": "What is 11 in Maori?",
    "2": "What is 12 in Maori?",
    "3": "What is 13 in Maori?",
    "4": "What is 14 in Maori?",
    "5": "What is 15 in Maori?",
    "6": "What is 16 in Maori?",
    "7": "What is 17 in Maori?",
    "8": "What is 18 in Maori?",
    "9": "What is 19 in Maori?",
    "10": "What is 20 in Maori?"
}

hard_answers = {
    "1": "tekau ma tahi",
    "2": "tekau ma rua",
    "3": "tekau ma toru",
    "4": "tekau ma wha",
    "5": "tekau ma rima",
    "6": "tekau ma ono",
    "7": "tekau ma whitu",
    "8": "tekau ma waru",
    "9": "tekau ma iwa",
    "10": "rua tekau"
}


# Get the user's mode selection
mode = ""
while mode.lower() != "easy" and mode.lower() != "hard" and mode.lower() != "e" and mode.lower() != "h":
    mode = input("Do you want to play on easy mode (e) or hard mode (h)? ")

# Make score variable
score = 0

# If selected easy, use easy questions
if mode.lower() == "easy" or mode.lower() == "e":
    # Tell user what mode they are on
    print("You are playing on Easy Mode")
    # Shuffle the order of the questions
    question_order = list(questions.keys())
    random.shuffle(question_order)

    # Loop through each question in the shuffled order
    for question_num in question_order:
        # Ask the question
        print(questions[question_num])

        # Get the user's answer
        user_answer = input("> ")

        # Check the user's answer
        if user_answer.lower() == answers[question_num]:
            # If the user's answer is correct on the first try, add 2 to the score
            score += 2
            print("Correct. Nice job!")
        else:
            # If the user's answer is incorrect, try again
            # Give them a hint, telling them the first letter of the answer
            print("Incorrect. Here's a hint: The first letter of the correct answer is", answers[question_num][0])

            # Give the user another chance to answer the question correctly
            while user_answer.lower() != answers[question_num]:
                user_answer = input("> ")

                # If the user's answer is correct on the subsequent try, break the loop
                if user_answer.lower() == answers[question_num]:
                    print("Correct. Nice job!")
                    break

    # If score is below 0, the score is just 0
    if score < 0:
        score = 0

# If selected hard, use hard questions
elif mode.lower() == "hard" or mode.lower() == "h":
    # Tell user what mode they are on
    print("You are playing on Hard Mode")
    # Shuffle the order of the questions
    hard_questions_order = list(hard_questions.keys())
    random.shuffle(hard_questions_order)

    # Loop through each question in the shuffled order
    for hard_question_num in hard_questions_order:
        # Ask the question
        print(hard_questions[hard_question_num])

        # Get the user's answer
        user_answer = input("> ")

        # Check the user's answer
        if user_answer.lower() == hard_answers[hard_question_num]:
            # If the user's answer is correct on the first try, add 3 to the score
            score += 3
            print("Correct. Nice job!")
        else:
            # If the user's answer is incorrect, try again
            # Give them a hint, telling them the first letter of the answer
            print("Incorrect. Here's a hint: The first letter of the correct answer is",
                  hard_answers[hard_question_num][0])
            # Take away 1 point
            score -= 1

            # Give the user another chance to answer the question correctly
            while user_answer.lower() != hard_answers[hard_question_num]:
                user_answer = input("> ")

                # If the user's answer is correct on the subsequent try, break the loop
                if user_answer.lower() == hard_answers[hard_question_num]:
                    print("Correct. Nice job!")
                    break

    # If score is below 0, the score is just 0
    if score < 0:
        score = 0

# Display the final score
print(f"You finished with a score of {score}")

"""Based on 04_questions_v2
Added score counter
Added hints for the questions
"""

import random

# Questions
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

# Answers to the questions
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

# Shuffle the order of the questions
question_order = list(questions.keys())
random.shuffle(question_order)

# Make score variable
score = 0

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


# Display the final score
print(f"You  finished with a score of {score}")


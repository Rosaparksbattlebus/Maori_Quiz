"""Based on 04_questions_v1
Created a variable for a random order for the questions to be asked in.
Printed each question and change answer to lowercase so uppercase answers are valid.
Ask again when the answer is incorrect.
Continue when answers are correct until all questions have been asked.
Defined question and answers with .keys
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

# Loop through each question in the shuffled order
for question_num in question_order:
    # Ask the question
    print(questions[question_num])

    # Get the user's answer
    user_answer = input("> ")

    # Check the user's answer
    while user_answer.lower() != answers[question_num]:
        # If the user's answer is wrong, re-ask the question
        print("Incorrect. Try again")
        user_answer = input("> ")

    # If the user's answer is correct, move on to the next question
    print("Correct. Nice Job!")

# Congratulate them on achieving their Maori goals
print()
print("Congratulations man/woman you are incredibly beautiful")

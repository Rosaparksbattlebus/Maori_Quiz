import random

# Define the questions and answers for easy mode in a dictionary
easy_questions = {
    "1": "¿Cómo se dice 'one' en español?",
    "2": "¿Cómo se dice 'two' en español?",
    "3": "¿Cómo se dice 'three' en español?",
    "4": "¿Cómo se dice 'four' en español?",
    "5": "¿Cómo se dice 'five' en español?",
    "6": "¿Cómo se dice 'six' en español?",
    "7": "¿Cómo se dice 'seven' en español?",
    "8": "¿Cómo se dice 'eight' en español?",
    "9": "¿Cómo se dice 'nine' en español?",
    "10": "¿Cómo se dice 'ten' en español?"
}

easy_answers = {
    "1": "uno",
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco",
    "6": "seis",
    "7": "siete",
    "8": "ocho",
    "9": "nueve",
    "10": "diez"
}

# Define the questions and answers for hard mode in a dictionary
hard_questions = {
    "1": "¿Cómo se dice 'eleven' en español?",
    "2": "¿Cómo se dice 'twelve' en español?",
    "3": "¿Cómo se dice 'thirteen' en español?",
    "4": "¿Cómo se dice 'fourteen' en español?",
    "5": "¿Cómo se dice 'fifteen' en español?",
    "6": "¿Cómo se dice 'sixteen' en español?",
    "7": "¿Cómo se dice 'seventeen' en español?",
    "8": "¿Cómo se dice 'eighteen' en español?",
    "9": "¿Cómo se dice 'nineteen' en español?",
    "10": "¿Cómo se dice 'twenty' en español?"
}

hard_answers = {
    "1": "once",
    "2": "doce",
    "3": "trece",
    "4": "catorce",
    "5": "quince",
    "6": "dieciséis",
    "7": "diecisiete",
    "8": "dieciocho",
    "9": "diecinueve",
    "10": "veinte"
}

# Get the user's mode selection
mode = input("Seleccione su modo de juego ('easy' o 'hard'): ")

# Check if the user selected easy or hard mode
if mode.lower() == "easy":
    # Shuffle the order of the questions
    question_order = list(easy_questions.keys())
    random.shuffle(question_order)

    # Loop through each question in the shuffled order
    for question_num in question_order:
        # Ask the question
        print(easy_questions[question_num])

        # Get the user's answer
        user_answer = input("> ")

        # Check the user's answer
        while user_answer.lower() != easy_answers[question_num]:
            # If the user's answer is wrong, re-ask the question
            print("Incorrecto. Inténtalo de nuevo.")
            user_answer = input("> ")

        # If the user's answer is correct, move on to the next question
        print("Correcto. Siguiente pregunta.")

else:
    # Shuffle the order of the questions
    question_order = list(hard_questions.keys())
    random

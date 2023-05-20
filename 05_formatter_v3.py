"""Component 5 - Statement formatter v3
Call function 3 times - once for each of the tests
"""


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
print(formatter("-", "Welcome to the Maori Numbers Quiz"))
print()
print(formatter("!", "Nice work. You got it correct"))
print()
print(formatter("*", "You finished with a score of (score)"))


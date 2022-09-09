import random

GAME_RULES = 'What is the result of the expression?'
MIN_NUM_TO_GENERATE = 1
MAX_NUM_TO_GENERATE = 100


def generate_math_operator():
    return random.choice(['+', '-', '*'])


def generate_game_round():
    num1 = random.randint(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE)
    num2 = random.randint(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE)
    math_operator = generate_math_operator()
    question = f'{num1} {math_operator} {num2}'
    if math_operator == '+':
        answer = num1 + num2
    elif math_operator == '-':
        answer = num1 - num2
    elif math_operator == '*':
        answer = num1 * num2
    return (question, answer)

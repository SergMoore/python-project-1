import random
from brain_games.engine import start_game

MIN_NUM_TO_GENERATE = 1
MAX_NUM_TO_GENERATE = 100


def generate_math_operator():
    return random.choice(['+', '-', '*'])


def generate_q_a_pair():
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


def start_brain_calc():
    game_title = 'brain_calc'
    start_game(game_title)

import random
import operator


GAME_DESCRIPTION = 'What is the result of the expression?'
MIN_NUM_TO_GENERATE = 1
MAX_NUM_TO_GENERATE = 100


def generate_math_operator():
    return random.choice(['+', '-', '*'])


def calculate_binary_operation(num1, num2, str_operator):
    get_operator = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul}.get
    op = get_operator(str_operator)
    result = op(num1, num2)
    return result


def generate_game_round():
    num1 = random.randint(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE)
    num2 = random.randint(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE)
    math_operator = generate_math_operator()
    question = f'{num1} {math_operator} {num2}'
    answer = calculate_binary_operation(num1, num2, math_operator)
    return (question, str(answer))

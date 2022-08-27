import random

from brain_games.engine import generate_a_num


def generate_math_operation():
    return random.choice(["+", "-", "*"])


def calc_from_str(str_expression):
    elements = str_expression.split()
    num1 = int(elements[0])
    num2 = int(elements[2])
    math_operation = elements[1]
    if math_operation == "+":
        return num1 + num2
    elif math_operation == "-":
        return num1 - num2
    elif math_operation == "*":
        return num1 * num2


def generate_questions():
    ROUNDS_COUNT = 3
    list_of_questions = []
    for i in range(ROUNDS_COUNT):
        num1 = generate_a_num()
        num2 = generate_a_num()
        math_oper = generate_math_operation()
        math_expression = f"{num1} {math_oper} {num2}"
        list_of_questions.append(math_expression)
    return list_of_questions


def form_answers(list_of_questions):
    list_of_answers = []
    for i in range(len(list_of_questions)):
        list_of_answers.append(calc_from_str(list_of_questions[i]))
    return list_of_answers

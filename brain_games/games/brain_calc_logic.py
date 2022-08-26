import random

from brain_games.engine import generate_a_num, start_game


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
    rounds_number = 3
    list_of_questions = []
    for i in range(rounds_number):
        num1 = generate_a_num()
        num2 = generate_a_num()
        math_oper = generate_math_operation()
        math_expression = f"{num1} {math_oper} {num2}"
        list_of_questions.append(math_expression)
    return list_of_questions


def form_answers_list(list_of_questions):
    list_of_answers = []
    for i in range(len(list_of_questions)):
        list_of_answers.append(calc_from_str(list_of_questions[i]))
    return list_of_answers


def brain_calc_game():
    game_rules = 'What is the result of the expression?'
    questions_list = generate_questions()
    answers_list = form_answers_list(questions_list)
    start_game(game_rules, questions_list, answers_list)

import math

from brain_games.engine import generate_a_num, start_game


def is_prime(natur_num):
    if natur_num == 1 or natur_num % 2 == 0:
        return natur_num == 2
    div = 3
    while div <= math.sqrt(natur_num) and natur_num % div != 0:
        div += 2
    return div * div > natur_num


def is_prime_to_str(natur_num):
    if is_prime(natur_num):
        return "yes"
    else:
        return "no"


def generate_questions():
    ROUNDS_COUNT = 3
    list_of_questions = []
    for i in range(ROUNDS_COUNT):
        num = generate_a_num()
        list_of_questions.append(num)
    return list_of_questions


def form_answers(list_of_questions):
    list_of_answers = []
    for i in range(len(list_of_questions)):
        list_of_answers.append(is_prime_to_str(list_of_questions[i]))
    return list_of_answers


def start_brain_prime():
    game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questions = generate_questions()
    answers = form_answers(questions)
    start_game(game_rules, questions, answers)

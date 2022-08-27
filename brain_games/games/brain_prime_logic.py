import math

from brain_games.engine import generate_a_num, start_game


def is_prime(natur_num):
    if natur_num == 2:
        return "yes"
    elif natur_num == 1 or natur_num % 2 == 0:
        return "no"
    else:
        i = 3
        has_div_found = False
        while i <= math.sqrt(natur_num) and not has_div_found:
            if natur_num % i == 0:
                has_div_found = True
                break
            else:
                i += 2
        if has_div_found:
            return "no"
        else:
            return "yes"


def generate_questions():
    rounds_number = 3
    list_of_questions = []
    for i in range(rounds_number):
        num = generate_a_num()
        list_of_questions.append(num)
    return list_of_questions


def form_answers_list(list_of_questions):
    list_of_answers = []
    for i in range(len(list_of_questions)):
        list_of_answers.append(is_prime(list_of_questions[i]))
    return list_of_answers


def brain_prime_game():
    game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questions_list = generate_questions()
    answers_list = form_answers_list(questions_list)
    start_game(game_rules, questions_list, answers_list)

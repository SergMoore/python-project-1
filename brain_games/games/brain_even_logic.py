from brain_games.engine import generate_a_num, start_game


def is_even(int_num):
    if int(int_num) % 2 == 0:
        return "yes"
    else:
        return "no"


def generate_questions():
    rounds_number = 3
    list_of_questions = []
    for i in range(rounds_number):
        list_of_questions.append(generate_a_num())
    return list_of_questions


def form_answers_list(list_of_questions):
    list_of_answers = []
    for i in range(len(list_of_questions)):
        list_of_answers.append(is_even(int(list_of_questions[i])))
    return list_of_answers


def brain_even_game():
    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions_list = generate_questions()
    answers_list = form_answers_list(questions_list)
    start_game(game_rules, questions_list, answers_list)

from brain_games.engine import generate_a_num


def is_even_to_str(int_num):
    if int(int_num) % 2 == 0:
        return "yes"
    else:
        return "no"


def generate_questions():
    ROUNDS_COUNT = 3
    list_of_questions = []
    for i in range(ROUNDS_COUNT):
        list_of_questions.append(generate_a_num())
    return list_of_questions


def form_answers(list_of_questions):
    list_of_answers = []
    for i in range(len(list_of_questions)):
        list_of_answers.append(is_even_to_str(int(list_of_questions[i])))
    return list_of_answers

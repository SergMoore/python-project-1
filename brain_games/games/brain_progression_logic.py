import random


from brain_games.engine import start_game


def generate_arithmet_progression():
    (MIN_BORDER_FOR_a0_d, MAX_BORDER_FOR_a0_d) = (1, 15)
    (MIN_MEMBERS_COUNT, MAX_MEMBERS_COUNT) = (5, 10)
    a0 = random.randint(MIN_BORDER_FOR_a0_d, MAX_BORDER_FOR_a0_d)
    d = random.randint(MIN_BORDER_FOR_a0_d, MAX_BORDER_FOR_a0_d)
    members_num = random.randint(MIN_MEMBERS_COUNT, MAX_MEMBERS_COUNT)
    HIDDEN_MEMBER = ".."
    hidden_member_index = random.randint(0, members_num - 1)
    progression = ""
    for i in range(members_num):
        if i == hidden_member_index:
            current_element = HIDDEN_MEMBER
        else:
            current_element = str(a0 + i * d)
        progression = f"{progression} {current_element}"
    return progression.strip()


def find_element_of_progr(str_expression):
    series = str_expression.split()
    last_i = len(series) - 1
    HIDDEN_MEMBER = ".."
    hidden_i = series.index(HIDDEN_MEMBER)
    if hidden_i == last_i:
        return int(2 * int(series[last_i - 1]) - int(series[last_i - 2]))
    elif hidden_i == 0:
        return int(2 * int(series[1]) - int(series[2]))
    else:
        return int((int(series[hidden_i - 1]) + int(series[hidden_i + 1])) / 2)


def generate_questions():
    ROUNDS_COUNT = 3
    list_of_questions = []
    for i in range(ROUNDS_COUNT):
        progression = generate_arithmet_progression()
        list_of_questions.append(progression)
    return list_of_questions


def form_answers(list_of_questions):
    list_of_answers = []
    for i in range(len(list_of_questions)):
        list_of_answers.append(find_element_of_progr(list_of_questions[i]))
    return list_of_answers


def start_brain_progression():
    game_rules = 'What number is missing in the progression?'
    questions = generate_questions()
    answers = form_answers(questions)
    start_game(game_rules, questions, answers)

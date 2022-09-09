import random

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM_TO_GENERATE = 1
MAX_NUM_TO_GENERATE = 100


def is_even_to_str(int_num):
    if int_num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_game_round():
    num = random.randint(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE)
    question = str(num)
    answer = is_even_to_str(num)
    return (question, answer)

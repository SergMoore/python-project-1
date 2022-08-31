import random

MIN_NUM_TO_GENERATE = 1
MAX_NUM_TO_GENERATE = 100


def is_even_to_str(int_num):
    if int(int_num) % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_q_a_pair():
    num = random.randint(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE)
    question = str(num)
    answer = is_even_to_str(num)
    return (question, answer)

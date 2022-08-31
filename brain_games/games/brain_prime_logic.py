import math
import random


MIN_NUM_TO_GENERATE = 1
MAX_NUM_TO_GENERATE = 100


def is_prime(natur_num):
    if natur_num == 1 or natur_num % 2 == 0:
        return natur_num == 2
    div = 3
    while div <= math.sqrt(natur_num) and natur_num % div != 0:
        div += 2
    return div * div > natur_num


def generate_q_a_pair():
    question = random.randint(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return (str(question), answer)

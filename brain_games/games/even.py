import random


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM_TO_GENERATE = 1
MAX_NUM_TO_GENERATE = 100


def generate_game_round():
    num = random.randint(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE)
    question = str(num)
    if num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)

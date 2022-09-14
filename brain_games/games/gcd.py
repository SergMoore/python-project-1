import random
import math


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_NUM_TO_GENERATE = 1
MAX_NUM_TO_GENERATE = 100


def generate_game_round():
    num1 = random.randint(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE)
    num2 = random.randint(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE)
    question = f'{num1} {num2}'
    answer = math.gcd(num1, num2)
    return (question, answer)

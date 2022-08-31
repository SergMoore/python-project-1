import random


MIN_NUM_TO_GENERATE = 1
MAX_NUM_TO_GENERATE = 100


def find_gcd(num1, num2):
    gcd_value = 1
    for i in range(2, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd_value = i
    return gcd_value


def generate_q_a_pair():
    num1 = random.randint(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE)
    num2 = random.randint(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE)
    question = f'{num1} {num2}'
    answer = find_gcd(num1, num2)
    return (question, answer)

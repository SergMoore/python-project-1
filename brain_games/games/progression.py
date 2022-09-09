import random


GAME_RULES = 'What number is missing in the progression?'
(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE) = (1, 15)
(MIN_MEMBERS_COUNT, MAX_MEMBERS_COUNT) = (5, 10)
HIDDEN_MEMBER = '..'


def generate_game_round():
    first_member = random.randint(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE)
    diff = random.randint(MIN_NUM_TO_GENERATE, MAX_NUM_TO_GENERATE)
    members_num = random.randint(MIN_MEMBERS_COUNT, MAX_MEMBERS_COUNT)
    hidden_member_index = random.randint(0, members_num - 1)
    answer = first_member + diff * hidden_member_index
    progression = ''
    for i in range(members_num):
        if i == hidden_member_index:
            current_element = HIDDEN_MEMBER
        else:
            current_element = str(first_member + i * diff)
        progression = f'{progression} {current_element}'
    question = progression.strip()
    return (question, answer)

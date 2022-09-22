import random


GAME_DESCRIPTION = 'What number is missing in the progression?'
MIN_NUM_TO_GENERATE_MEMBER = 0
MAX_NUM_TO_GENERATE_MEMBER = 15
MIN_NUM_TO_GENERATE_STEP = 1
MAX_NUM_TO_GENERATE_STEP = 12
MIN_MEMBERS_COUNT = 5
MAX_MEMBERS_COUNT = 10
HIDDEN_MEMBER = '..'


def generate_ar_progression(first_member, step, members_count):
    members = []
    for member_index in range(members_count):
        members.append(str(first_member + step * member_index))
    return members


def generate_game_round():
    first_member = random.randint(MIN_NUM_TO_GENERATE_MEMBER,
                                  MAX_NUM_TO_GENERATE_MEMBER)
    step = random.randint(MIN_NUM_TO_GENERATE_STEP,
                          MAX_NUM_TO_GENERATE_STEP)
    members_count = random.randint(MIN_MEMBERS_COUNT, MAX_MEMBERS_COUNT)
    hidden_member_index = random.randint(0, members_count - 1)
    progression = generate_ar_progression(first_member, step, members_count)
    answer = str(progression[hidden_member_index])
    progression[hidden_member_index] = HIDDEN_MEMBER
    question = ' '.join(progression).strip()
    return (question, answer)

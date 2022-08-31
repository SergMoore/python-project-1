import random

(MIN_BORDER_FOR_a0_d, MAX_BORDER_FOR_a0_d) = (1, 15)
(MIN_MEMBERS_COUNT, MAX_MEMBERS_COUNT) = (5, 10)
HIDDEN_MEMBER = '..'


def generate_q_a_pair():
    a0 = random.randint(MIN_BORDER_FOR_a0_d, MAX_BORDER_FOR_a0_d)
    d = random.randint(MIN_BORDER_FOR_a0_d, MAX_BORDER_FOR_a0_d)
    members_num = random.randint(MIN_MEMBERS_COUNT, MAX_MEMBERS_COUNT)
    hidden_member_index = random.randint(0, members_num - 1)
    answer = a0 + d * hidden_member_index
    progression = ''
    for i in range(members_num):
        if i == hidden_member_index:
            current_element = HIDDEN_MEMBER
        else:
            current_element = str(a0 + i * d)
        progression = f'{progression} {current_element}'
    question = progression.strip()
    return (question, answer)

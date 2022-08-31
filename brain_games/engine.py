import prompt

from brain_games.scripts.brain_games import greet_user
import brain_games.cli
import brain_games.games.brain_calc_logic
import brain_games.games.brain_even_logic
import brain_games.games.brain_gcd_logic
import brain_games.games.brain_prime_logic
import brain_games.games.brain_progression_logic


ROUNDS_COUNT = 3


def print_game_rules(game_title):
    if game_title == 'brain-calc':
        print('What is the result of the expression?')
    elif game_title == 'brain-even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game_title == 'brain-gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game_title == 'brain-prime':
        print('Answer "yes" if given number is prime. Otherwise answer"no".')
    elif game_title == 'brain-progression':
        print('What number is missing in the progression?')


def generate_specific_question_answer_pair(game_title):
    if game_title == 'brain-calc':
        (q, a) = brain_games.games.brain_calc_logic.generate_q_a_pair()
    elif game_title == 'brain-even':
        (q, a) = brain_games.games.brain_even_logic.generate_q_a_pair()
    elif game_title == 'brain-gcd':
        (q, a) = brain_games.games.brain_gcd_logic.generate_q_a_pair()
    elif game_title == 'brain-prime':
        (q, a) = brain_games.games.brain_prime_logic.generate_q_a_pair()
    elif game_title == 'brain-progression':
        (q, a) = brain_games.games.brain_progression_logic.generate_q_a_pair()
    return (q, a)


def ask_game_question(question_body):
    print(f'Question: {str(question_body)}')
    answer = prompt.string('Your answer: ')
    return answer


def is_valid_answer(valid_answer, guess_answer):
    if str(guess_answer) == str(valid_answer):
        return True
    else:
        return False


def define_game_status(is_valid_answer, round_num):
    if is_valid_answer and round_num != ROUNDS_COUNT:
        return 'go_next_round'
    elif is_valid_answer and round_num == ROUNDS_COUNT:
        return 'won'
    else:
        return 'lost'


def message_user(game_status, user_name, guess_answer, correct_answer):
    rounds_iteration = 1
    if game_status == 'go_next_round':
        print('Correct!')
        return rounds_iteration
    elif game_status == 'won':
        print('Correct!')
        print(f'Congratulations, {user_name}!')
        return ROUNDS_COUNT + rounds_iteration
    elif game_status == 'lost':
        print(f"'{guess_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {user_name}!")
        return ROUNDS_COUNT + rounds_iteration
    else:
        return ROUNDS_COUNT + rounds_iteration


def start_game(game_title):
    greet_user()
    user_name = brain_games.cli.welcome_user()
    print_game_rules(game_title)
    round_num = 1
    while round_num <= ROUNDS_COUNT:
        question, answer = generate_specific_question_answer_pair(game_title)
        guess_answer = ask_game_question(question).lower()
        is_correct_answer = is_valid_answer(answer, guess_answer)
        game_state = define_game_status(is_correct_answer, round_num)
        round_num += message_user(game_state, user_name, guess_answer, answer)

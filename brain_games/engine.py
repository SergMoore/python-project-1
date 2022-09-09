import prompt

from brain_games.scripts.brain_games import greet_user
import brain_games.cli


ROUNDS_COUNT = 3


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
        print(f'\'{guess_answer}\' is wrong answer ;(. '
              f'Correct answer was \'{correct_answer}\'.')
        print(f'Let\'s try again, {user_name}!')
        return ROUNDS_COUNT + rounds_iteration
    else:
        return ROUNDS_COUNT + rounds_iteration


def start_game(game):
    greet_user()
    user_name = brain_games.cli.welcome_user()
    print(game.GAME_RULES)
    round_num = 1
    while round_num <= ROUNDS_COUNT:
        question, answer = game.generate_game_round()
        guess_answer = ask_game_question(question).lower()
        is_correct_answer = is_valid_answer(answer, guess_answer)
        game_state = define_game_status(is_correct_answer, round_num)
        round_num += message_user(game_state, user_name, guess_answer, answer)

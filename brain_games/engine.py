import prompt

from brain_games.scripts.brain_games import greet_user
import brain_games.cli


ROUNDS_COUNT = 3


def start_game(game):
    greet_user()
    user_name = brain_games.cli.welcome_user()
    print(game.GAME_DESCRIPTION)
    round_num = 1
    while round_num <= ROUNDS_COUNT:
        question, answer = game.generate_game_round()
        print(f'Question: {str(question)}')
        guess_answer = prompt.string('Your answer: ').lower()
        if guess_answer == str(answer) and round_num < ROUNDS_COUNT:
            print('Correct!')
            round_num += 1
        elif guess_answer == str(answer) and round_num == ROUNDS_COUNT:
            print('Correct!')
            print(f'Congratulations, {user_name}!')
            break
        else:
            print(f'\'{guess_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{answer}\'.')
            print(f'Let\'s try again, {user_name}!')
            break

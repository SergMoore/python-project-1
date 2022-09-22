import prompt


ROUNDS_COUNT = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.GAME_DESCRIPTION)
    round_num = 1
    while round_num <= ROUNDS_COUNT:
        question, answer = game.generate_game_round()
        print(f'Question: {str(question)}')
        guess_answer = prompt.string('Your answer: ').lower()
        if guess_answer == answer:
            print('Correct!')
        else:
            print(f'\'{guess_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{answer}\'.')
            print(f'Let\'s try again, {user_name}!')
            break
        if round_num == ROUNDS_COUNT:
            print(f'Congratulations, {user_name}!')
        round_num += 1

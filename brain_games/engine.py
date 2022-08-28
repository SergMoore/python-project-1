import random
import prompt

from brain_games.scripts.brain_games import main_greeting
import brain_games.cli


def generate_a_num():
    MIN_NUM = 1
    MAX_NUM = 100
    return random.randint(MIN_NUM, MAX_NUM)


def ask_game_question(question_body):
    print(f'Question: {str(question_body)}')
    answer = prompt.string("Your answer: ")
    return answer


def is_correct_answer(valid_answer, guess_answer):
    if str(guess_answer) == str(valid_answer):
        return True
    else:
        return False


def define_game_status(is_valid_answer, round_num):
    ROUNDS_COUNT = 3
    if is_valid_answer and round_num != ROUNDS_COUNT:
        return "go_next_round"
    elif is_valid_answer and round_num == ROUNDS_COUNT:
        return "won"
    else:
        return "lost"


def apply_user(game_status, user_name, guess_answer, correct_answer):
    ROUNDS_COUNT = 3
    ROUNDS_ITERATION = 1
    if game_status == "go_next_round":
        print("Correct!")
        return ROUNDS_ITERATION
    elif game_status == "won":
        print("Correct!")
        print(f"Congratulations, {user_name}!")
        return ROUNDS_COUNT + ROUNDS_ITERATION
    elif game_status == "lost":
        print(f"'{guess_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {user_name}!")
        return ROUNDS_COUNT + ROUNDS_ITERATION
    else:
        return ROUNDS_COUNT + ROUNDS_ITERATION


def start_game(game_rules, questions, valid_answers):
    main_greeting()
    user_name = brain_games.cli.welcome_user()
    print(game_rules)
    ROUNDS_COUNT = 3
    round_num = 1
    while round_num <= ROUNDS_COUNT:
        question = questions[round_num - 1]
        cor_answer = valid_answers[round_num - 1]
        guess_answer = ask_game_question(question).lower()
        is_valid_answer = is_correct_answer(cor_answer, guess_answer)
        game_state = define_game_status(is_valid_answer, round_num)
        round_num += apply_user(game_state, user_name, guess_answer, cor_answer)

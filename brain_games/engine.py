import random
import prompt

from brain_games.scripts.brain_games import main_greeting
import brain_games.cli


def generate_a_num():
    min_num = 1
    max_num = 100
    return random.randint(min_num, max_num)


def ask_game_question(question_body):
    print(f'Question: {str(question_body)}')
    answer = prompt.string("Your answer: ")
    return answer


def is_correct_answer(valid_answer, guess_answer):
    if str(guess_answer) == str(valid_answer):
        return True
    else:
        return False


def start_game(game_rules, questions_list, valid_answers_list):
    main_greeting()
    user_name = brain_games.cli.welcome_user()
    print(game_rules)
    rounds_number = 3
    current_round = 1
    is_last_round = False
    while current_round <= rounds_number:
        if current_round == rounds_number:
            is_last_round = True
        question = questions_list[current_round - 1]
        cor_answer = valid_answers_list[current_round - 1]
        guess_answer = ask_game_question(question).lower()
        if is_correct_answer(cor_answer, guess_answer) and not is_last_round:
            print("Correct!")
            current_round += 1
        elif is_correct_answer(cor_answer, guess_answer) and is_last_round:
            print("Correct!")
            print(f"Congratulations, {user_name}!")
            break
        else:
            print(f"'{guess_answer}' is wrong answer ;(. "
                  f"Correct answer was '{cor_answer}'.")
            print(f"Let's try again, {user_name}!")
            break

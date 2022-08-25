import brain_games.cli
import random
import prompt
from brain_games.scripts.brain_games import main_greeting


def is_even(int_num):
    if int_num % 2 == 0:
        return "yes"
    else:
        return "no"


def brain_even_game():
    main_greeting()
    user_name = brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_of_questions = 3
    current_question_num = 1
    is_last_question = False
    while current_question_num <= number_of_questions:
        if current_question_num == number_of_questions:
            is_last_question = True
        else:
            is_last_question = False
        generated_num = random.randint(1, 100)
        correct_answer = is_even(generated_num)
        print(f'Question: {generated_num}')
        guess_answer = prompt.string("Your answer: ")
        if correct_answer == guess_answer.lower() and not is_last_question:
            print("Correct!")
            current_question_num += 1
        elif correct_answer == guess_answer.lower() and is_last_question:
            print("Correct!")
            print(f"Congratulations, {user_name}!")
            break
        else:
            print(f"'{guess_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break

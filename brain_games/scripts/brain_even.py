#!/usr/bin/env python3
from brain_games.games.brain_even_logic import generate_questions, form_answers
from brain_games.engine import start_game


def main():
    GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions = generate_questions()
    answers = form_answers(questions)
    start_game(GAME_RULES, questions, answers)


if __name__ == '__main__':
    main()

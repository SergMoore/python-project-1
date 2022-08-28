#!/usr/bin/env python3
import brain_games.games.brain_even_logic
from brain_games.engine import start_game as start_brain_even


def main():
    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions = brain_games.games.brain_even_logic.generate_questions()
    answers = brain_games.games.brain_even_logic.form_answers(questions)
    start_brain_even(game_rules, questions, answers)


if __name__ == '__main__':
    main()

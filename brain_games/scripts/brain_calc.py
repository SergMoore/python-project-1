#!/usr/bin/env python3
import brain_games.games.brain_calc_logic
from brain_games.engine import start_game as start_brain_calc


def main():
    game_rules = 'What is the result of the expression?'
    questions = brain_games.games.brain_calc_logic.generate_questions()
    answers = brain_games.games.brain_calc_logic.form_answers(questions)
    start_brain_calc(game_rules, questions, answers)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import brain_games.games.brain_gcd_logic
from brain_games.engine import start_game as start_brain_gcd


def main():
    game_rules = 'Find the greatest common divisor of given numbers.'
    questions = brain_games.games.brain_gcd_logic.generate_questions()
    answers = brain_games.games.brain_gcd_logic.form_answers(questions)
    start_brain_gcd(game_rules, questions, answers)


if __name__ == '__main__':
    main()

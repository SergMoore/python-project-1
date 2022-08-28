#!/usr/bin/env python3
import brain_games.games.brain_prime_logic
from brain_games.engine import start_game as start_brain_prime


def main():
    game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questions = brain_games.games.brain_prime_logic.generate_questions()
    answers = brain_games.games.brain_prime_logic.form_answers(questions)
    start_brain_prime(game_rules, questions, answers)


if __name__ == '__main__':
    main()

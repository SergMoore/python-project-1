#!/usr/bin/env python3
import brain_games.games.brain_progression_logic
from brain_games.engine import start_game as start_brain_progression


def main():
    game_rules = 'What number is missing in the progression?'
    questions = brain_games.games.brain_progression_logic.generate_questions()
    answers = brain_games.games.brain_progression_logic.form_answers(questions)
    start_brain_progression(game_rules, questions, answers)


if __name__ == '__main__':
    main()

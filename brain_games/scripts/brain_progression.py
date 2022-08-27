#!/usr/bin/env python3
from brain_games.games.brain_progression_logic import generate_questions
from brain_games.games.brain_progression_logic import form_answers
from brain_games.engine import start_game


def main():
    GAME_RULES = 'What number is missing in the progression?'
    questions = generate_questions()
    answers = form_answers(questions)
    start_game(GAME_RULES, questions, answers)


if __name__ == '__main__':
    main()

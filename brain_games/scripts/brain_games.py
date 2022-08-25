#!/usr/bin/env python3
from brain_games.cli import welcome_user


def main_greeting():
    print("Welcome to the Brain Games!")


def main():
    main_greeting()
    welcome_user()


if __name__ == '__main__':
    main()

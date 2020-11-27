#!usr/bin/env python3

"""Runs three game episodes."""

import prompt


def run_game(game):
    """
    Runs given game.

    Returns: bool

    """

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    for _ in range(3):
        result = game()
        if result[0]:
            print('Correct!')
        else:
            print(f"'{result[1]}' is wrong anwer ;(. Correct answer was '{result[2]}'.\nLet's try again, {name}!")
            return False
    print(f'Congratulations, {name}')

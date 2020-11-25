"""Welcoming file."""

import prompt
from brain_games.games import brain_even, brain_calc


def run_episode():
    """
    Runs game episode..

    Returns: None

    """

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    user_choice = prompt.string('To choose a game enter a number: \n1. Brain Even\n2. Brain Calculator\n')
    if user_choice == 1:
        brain_even()
    elif user_choice == 2:
        brain_calc

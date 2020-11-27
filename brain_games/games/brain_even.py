#!/usr/bin/env python3

"""Even-odd game."""

import random
import prompt
from brain_games.scripts.run_game import run_game



def game():
    """
    Runs a single game episode.
    Returns: tuple

    """

    num = random.choice(range(0, 101))
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    print(f'Question: {num}')
    user_answer = prompt.string('Your answer: ')
    if user_answer == correct_answer:
        return (True, user_answer, correct_answer)
    else:
        return (False, user_answer, correct_answer)

def main():

    run_game(game)

if __name__ == "__main__":

    main()

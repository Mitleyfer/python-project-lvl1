#!usr/bin/env python3

"""Find missing number in progression."""

import prompt
import random
from brain_games.scripts.run_game import run_game


def game():
    """
    Runs single game episode.

    Returns: tuple

    """

    start = random.choice(range(1, 51))
    step = random.choice(range(1, 11))
    progression = [i for i in range(start, start + step * 11, step)]
    missing_num = random.choice(progression)
    question = ""
    for i in progression:
        if i == missing_num:
            question += ".."
        else:
            question += str(i)
        if i != progression[-1]:
            question += " "
    print('What number is missing in progression?')
    print(f'Question: {question}')
    user_answer = prompt.integer('Your answer: ')
    if user_answer == missing_num:
        return (True, user_answer, missing_num)
    else:
        return (False, user_answer, missing_num)

def main():

    run_game(game)

if __name__ == '__main__':

    main()

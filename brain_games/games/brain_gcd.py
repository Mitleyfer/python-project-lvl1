#!usr/bin/env python3

"""Find Greatest Common Divisor."""

import prompt
import random
from brain_games.scripts.run_game import run_game


def game():
    """
    Runs single game episode.

    Returns: tuple

    """

    num_1 = random.choice(range(1, 101))
    num_2 = random.choice(range(1, 101))
    print('Find the greatest common divisor of given numbers.')
    print(f'Question: {num_1} {num_2}')
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    gcd = num_1 + num_2
    user_answer = prompt.integer('Your answer: ')
    if user_answer == gcd:
        return(True, user_answer, gcd)
    else:
        return(False, user_answer, gcd)

def main():

    run_game(game)

if __name__ == '__main__':

    main()

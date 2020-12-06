#!usr/bin/env python3

"""Guess if prime."""


import prompt
import random
from brain_games.scripts.run_game import run_game


def game():
    """
    Runs a single game episode.

    Returns: tuple

    """

    primes = [2, 3, 5 ,7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211]
    num = random.choice([random.choice(range(1, 500)), random.choice(primes)])
    correct_answer = 'yes' if num in primes else 'no'
    print("""Answer "yes" if given number is prime. Otherwise answer "no".""")
    print(f'Question: {num}')
    user_answer = prompt.string('Your answer: ')
    if user_answer == correct_answer:
        return (True, user_answer, correct_answer)
    return (False, user_answer, correct_answer)

def main():

    run_game(game)

if __name__ == '__main__':

    main()


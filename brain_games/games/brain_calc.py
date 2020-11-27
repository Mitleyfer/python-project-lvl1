#!usr/bin/env python3

"""Calculator."""


import prompt
import random
from brain_games.scripts.run_game import run_game


def game():
    """
    Runs a single episode of a game.

    Returns: tuple

    """

    num_1 = random.choice(range(0, 101))
    num_2 = random.choice(range(0, 101))
    operator = random.choice(['*', '+', '-'])
    print('What is the result of the expression?')
    print(f'Question: {num_1} {operator} {num_2}')
    user_answer = prompt.integer('Your answer: ')
    if operator == '+':
        correct_answer = num_1 + num_2
    elif operator == '-':
        correct_answer = num_1 - num_2
    else:
        correct_answer = num_1 * num_2
    if user_answer == correct_answer:
        return (True, user_answer, correct_answer)
    else:
        return (False, user_answer, correct_answer)

def main():
    """
    Main function.

    Returns: None

    """

    run_game(game)

if __name__ == '__main__':

    main()

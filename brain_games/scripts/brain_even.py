#!/usr/bin/env python3

"""Even-odd game."""

import random
import prompt


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')
print("Answer 'yes' if the number is even, otherwise answer 'no'")

def number():
    """
    Chooses number in range 1-101.

    Returns: random number

    """
    return random.choice(range(1, 101))

def check_number(user_input, n):
    """
    Checks if the number is even.

    Returns: boolean

    """
    if (n % 2 == 0 and user_input == 'yes') or (n % 2 == 1 and user_input == 'no'):
        return True
    return False

def run_episode():
    """
    Runs a single game episode.
    Returns: None

    """

    num = number()
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ')
    if check_number(answer, num):
        print('Correct!')
        return True
    else:
        print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
        return False

def main():

    for e in range(3):
        episode = run_episode()
        if not episode:
            return episode

    print(f'Congratulations, {name}!')

if __name__ == "__main__":

    main()

#!usr/bin/env python3

"""Calculator."""


import prompt
import random


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')

def choose_number():
    """
    Chooses random number in range 0 - 101

    Returns: random number

    """

    return random.choice(range(0, 101))

def operation():
    """
    Chooses arithmetic operation.

    Returns: string

    """

    return random.choice(['+', '*', '-'])

def expression(num_1, num_2, operation):
    """
    Solve expression.

    Return: boolean

    """

    if operation == '+':
        return num_1 + num_2
    elif operation == '-':
        return num_1 - num_2
    elif operation == '*':
        return num_1 * num_2

def run_episode():
    """
    Runs a single episode of a game.

    Returns: None

    """

    num_1 = choose_number()
    num_2 = choose_number()
    operator = operation()
    print('What is the result of the expression?')
    print(f'Question: {num_1} {operator} {num_2}')
    user_answer = prompt.string('Your answer: ')
    correct_answer = expression(num_1, num_2, operator)
    if int(user_answer) == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was {correct_answer}")
        return False

def main():
    """
    Main function.

    Returns: None

    """
    for _ in range(3):
        episode = run_episode()
        if not episode:
            return episode
    print(f'Congratulations, {name}!')

if __name__ == '__main__':

    main()

"""Introduction module."""

import prompt


def welcome_user():
    """
    Greeting function
    Return: user name
    """
    name = prompt.string('Enter your name, please: ')
    print('Hello, {}!'.format(name))
    return name

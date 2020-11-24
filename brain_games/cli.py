
"""Introduction module."""

import prompt


def welcome_user():
    """
    Greeting function.

    Returns: None
    """
    name = prompt.string('Enter your name, please: ')
    print('Hello, {0}!'.format(name))

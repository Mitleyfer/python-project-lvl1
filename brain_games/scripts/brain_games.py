#!/usr/bin/env python3

"""Interface."""

from brain_games.cli import welcome_user


def main():
    """
    Represent game inreface.

    Returns: None

    """
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()

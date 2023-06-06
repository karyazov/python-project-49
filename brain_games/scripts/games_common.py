#!/usr/bin/env python3

import prompt

user_name = ''


def welcome_user(game_question: str) -> str:
    print('Welcome to the Brain Games!')

    user_name = prompt.string('May I have your name? ')
    print('Hello, ' + user_name)
    print(game_question)

    return user_name

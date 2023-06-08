#!/usr/bin/env python3
from brain_games.scripts.games_common import welcome_user
# from games_common import welcome_user
import random

user_name = ''


def a_progression():
    progress_start = random.randint(1, 100)
    progress_len = random.randint(5, 10)
    progress_step = random.randint(1, 10)
    hide_number = random.randint(1, progress_len)

    progression = ''
    i = 1
    user_question = ''

    while i <= progress_len:

        if i > 1:
            val = progress_start + (i - 1) * progress_step
        else:
            val = progress_start

        if i == hide_number:
            user_question = val
            val = '..'

        progression = progression + ' ' + str(val)
        i += 1

    print('Question: ' + progression)

    return str(user_question)


def main():

    task_name = 'What number is missing in the progression?'
    user_name = welcome_user(task_name)

    answer_is_error = False
    correct_answer_count = 0

    while answer_is_error is False and correct_answer_count < 3:

        question_need = a_progression()

        answer = str(input('Your answer: '))
        if question_need == answer:
            correct_answer_count += 1
            print('Correct!')
        else:
            answer_is_error = True
            print('\'' + answer + '\''
                  + ' is wrong answer ;(. Correct answer was '
                  + '\'' + question_need + '\'. \n Let\'s try again, '
                  + user_name + '!')

    if correct_answer_count == 3:
        print('Congratulations, ' + user_name + '!')


if __name__ == '__main__':
    main()

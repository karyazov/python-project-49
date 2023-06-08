#!/usr/bin/env python3
from brain_games.scripts.games_common import welcome_user
# from games_common import welcome_user
import random

user_name = ''


def is_prime():
    number = random.randint(1, 100)

    i = number
    count = 0

    print('Question: ' + str(number))

    while i >= 1:
        if number % i == 0:
            count += 1
        i -= 1

    if count == 2:
        return 'yes'
    else:
        return 'no'


def main():

    task_name = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    user_name = welcome_user(task_name)

    answer_is_error = False
    correct_answer_count = 0

    while answer_is_error is False and correct_answer_count < 3:

        question_need = is_prime()

        answer = str(input('Your answer: '))
        if question_need == answer.lower():
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

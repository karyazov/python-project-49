#!/usr/bin/env python3
from brain_games.scripts.games_common import welcome_user
import random

user_name = ''


def my_gcd(num1: int, num2: int) -> str:

    gcd = min(num1, num2)

    while gcd > 1:
        r1 = num1 % gcd
        r2 = num2 % gcd

        if r1 == r2 and r1 == 0:
            break
        gcd = gcd - 1

    return str(gcd)


def main():

    task_name = 'Find the greatest common divisor of given numbers.'
    user_name = welcome_user(task_name)

    answer_is_error = False
    correct_answer_count = 0

    while answer_is_error is False and correct_answer_count < 3:

        question_num1 = random.randint(0, 99)
        question_num2 = random.randint(0, 99)

        question_need = my_gcd(question_num1, question_num2)

        print('Question: ' + str(question_num1) + ' ' + str(question_num2))

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

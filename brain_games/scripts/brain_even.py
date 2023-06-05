#!/usr/bin/env python3
import prompt
import random

user_name = ''


def welcome_user():
    user_name = prompt.string('May I have your name? ')
    print('Hello, ' + user_name)


def main():
    print('Welcome to the Brain Games!')

    welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    answer_is_error = False
    correct_answer_count = 0

    while answer_is_error is False and correct_answer_count < 3:
        question_num = random.randint(0, 999)
        if question_num % 2 == 0:
            question_need = 'Yes'
        else:
            question_need = 'No'

        print('Question: ' + str(question_num))

        answer = input('Your answer: ')
        if question_need.lower() == answer.lower():
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

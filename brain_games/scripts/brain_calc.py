#!/usr/bin/env python3
from brain_games.scripts.games_common import welcome_user
import random

user_name = ''


def main():

    user_name = welcome_user('What is the result of the expression?')

    answer_is_error = False
    correct_answer_count = 0

    while answer_is_error is False and correct_answer_count < 3:
        question_num1 = random.randint(0, 99)
        question_num2 = random.randint(0, 99)
        operation = random.choice(('+', '-', '*'))
        result = ''
        text_operation = ''

        match operation:
            case '*':
                result = question_num1 * question_num2
                text_operation = str(question_num1) + '*' + str(question_num2)
            case '+':
                result = question_num1 + question_num2
                text_operation = str(question_num1) + '+' + str(question_num2)
            case '-':
                result = question_num1 - question_num2
                text_operation = str(question_num1) + '-' + str(question_num2)

        question_need = str(result)

        print('Question: ' + text_operation)

        answer = input('Your answer: ')
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

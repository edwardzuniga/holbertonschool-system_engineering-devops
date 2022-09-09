#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":

    user_id = int(sys.argv[1])
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    reque_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    reque_user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    print('Employee ', end='')

    for i in reque_user:
        if user_id == i.get('id'):
            EMPLOYEE_NAME = i.get('name')

    for j in reque_todos:
        total_num_task = j.get('userId')
        if total_num_task == user_id:
            TOTAL_NUMBER_OF_TASKS += 1

            num_task = j.get('completed')
            if num_task is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(j.get('title'))

    print('{} is done with tasks({}/{}):'.format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for j in TASK_TITLE:
        print('\t {}'.format(j))

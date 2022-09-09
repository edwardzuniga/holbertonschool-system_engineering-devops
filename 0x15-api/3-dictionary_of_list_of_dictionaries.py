#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":

    reque_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    reque_user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    with open('todo_all_employees.json', mode='w') as file_json:

        filejson = {}

        for i in reque_user:
            USER_ID = i.get('id')
            filejson[USER_ID] = []

            for j in reque_todos:
                if USER_ID == j.get('userId'):
                    USERNAME = i.get('username')
                    TASK_COMPLETED_S = j.get('completed')
                    TASK_TITLE = j.get('title')

                    filejson[USER_ID].append({'task': TASK_TITLE,
                                              'completed': TASK_COMPLETED_S,
                                              'username': USERNAME})

        json.dump(filejson, file_json)

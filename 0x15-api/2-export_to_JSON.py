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

    user_id = int(sys.argv[1])

    reque_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    reque_user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    js_file = sys.argv[1] + '.json'

    with open(js_file, mode='w') as file_json:

        filejson = {}

        for i in reque_user:
            if user_id == i.get('id'):
                USERNAME = i.get('username')

        listas = []

        for j in reque_todos:
            TASK_COMPLETED_STATUS = j.get('completed')
            TASK_TITLE = j.get('title')
            if user_id == j.get('userId'):
                listas.append({'task': TASK_TITLE,
                              'completed': TASK_COMPLETED_STATUS,
                              'username': USERNAME})
                filejson = {user_id: listas}

        json.dump(filejson, file_json)

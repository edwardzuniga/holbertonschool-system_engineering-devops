#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":

    user_id = int(sys.argv[1])

    reque_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    reque_user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    csv_file = sys.argv[1] + '.csv'

    with open(csv_file, mode='w') as export_file_csv:
        file_to_export = csv.writer(
            export_file_csv, delimiter=',',
            quotechar='"', quoting=csv.QUOTE_ALL)

        for i in reque_user:
            if user_id == i.get('id'):
                USERNAME = i.get('username')

        for j in reque_todos:
            USER_ID = j.get('userId')
            TASK_COMPLETED_STATUS = j.get('completed')
            TASK_TITLE = j.get('title')
            if user_id == j.get('userId'):
                file_to_export.writerow([
                     USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])

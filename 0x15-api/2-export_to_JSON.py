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
    id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        id)

    with requests.session() as session:
        tasks = session.get(todos_url).json()
        users = session.get(user_url).json()

        list_data = []
        for record in tasks:
            completed = record["completed"]
            title = record["title"]
            username = users["username"]
            data = {
                "task": title,
                "completed": completed,
                "username": username
            }
            list_data.append(data)

        text_file = "{}.json".format(id)
        with open(text_file, mode="w+", encoding="utf-8") as file:
            data_id = {id: list_data}
            json.dump(data_id, file)

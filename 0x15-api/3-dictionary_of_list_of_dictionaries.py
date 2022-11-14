#!/usr/bin/python3
"""Python script to export data in the JSON format."""


API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    import requests
    import sys
    import json

    users = requests.get("{}/users".format(API_URL))
    users_json = users.json()

    todos = requests.get('{}/todos'.format(API_URL))
    todos_json = todos.json()

    todo_general = {}

    for user in users_json:
        task_list = []
        for task in todos_json:
            if task.get('userId') == user.get('id'):
                task_dict = {"username": user.get('username'),
                             "task": task.get('title'),
                             "completed": task.get('completed')}
                task_list.append(task_dict)
        todo_general[user.get('id')] = task_list

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(todo_general, file)

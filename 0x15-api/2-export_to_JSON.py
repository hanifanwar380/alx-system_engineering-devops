#!/usr/bin/python3
"""Python script to export data in the JSON format."""


API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    import requests
    import sys
    import json

    userId = sys.argv[1]
    user = requests.get("{}/users/{}".format(API_URL, userId))

    name = user.json().get('name')
    todos = requests.get('{}/todos'.format(API_URL))

    todos_json = todos.json()

    user_todo = {}
    task_list = []

    for task in todos_json:
        if task.get('userId') == int(userId):
            task_dict = {"task": task.get('title'),
                         "completed": task.get('completed'),
                         "username": user.json().get('username')}
            task_list.append(task_dict)
    user_todo[userId] = task_list

    file_name = userId + '.json'
    with open(file_name, mode='w') as file:
        json.dump(user_todo, file)
#!/usr/bin/python3
'''A python script for an employee, returns information
about his/her To-do list progress.
'''

API_URL = 'https://jsonplaceholder.typicode.com'


if __name__ == "__main__":
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get
    ("{}/users/{}"
     .format(API_URL, userId))

    name = user.json().get('name')

    todos = requests.get('{}/todos'.format(API_URL))
    totalTasks = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
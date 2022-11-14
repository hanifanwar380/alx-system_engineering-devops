#!/usr/bin/python3
"""Python script to export data in the CSV format."""


API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    import csv
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("{}/users/{}".format(API_URL, userId))

    name = user.json().get('name')
    todos = requests.get('{}/todos'.format(API_URL))

    file_name = userId + '.csv'
    with open(file_name, mode='w') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL, lineterminator='\n')

        for task in todos.json():
            if task.get('userId') == int(userId):
                csv_writer.writerow([userId, name, str(task.get('completed')),
                                     task.get('title')])

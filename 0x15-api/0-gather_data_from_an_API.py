#!/usr/bin/python3
""" API from Placeholdder """
import requests
from sys import argv


if __name__ == '__main__':
    todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos?user_Id={}".format(
                int(argv[1]))
            ).json()
    users = requests.get(
            "https://jsonplaceholder.typicode.com/users").json()
    tasks_done = []

    for todo in todos:
        if todo['completed'] is True:
            tasks_done.append(todo['title'])
    for user in users:
        if user['id'] == int(argv[1]):
            name = user['name']
    print("Employee {} is done with tasks({}/{}):".format(
            name, len(tasks_done), len(todos)))
    for task in tasks_done:
        print("\t {}".format(task))

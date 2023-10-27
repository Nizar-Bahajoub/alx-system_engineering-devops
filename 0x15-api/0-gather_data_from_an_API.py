#!/usr/bin/python3
""" API from Placeholdder """
import requests
from sys import argv


if __name__ == '__main__':
    todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos?user_Id={}".format(
                int(argv[1]))
            ).json()
    user = requests.get(
            "https://jsonplaceholder.typicode.com/users?id={}".format(
                int(argv[1]))
            ).json()
    tasks_done = []

    for todo in todos:
        if todo['completed'] is True:
            tasks_done.append(todo['title'])

    print("Employee {} is done with tasks({}/{}):".format(
            user[0]['name'], len(tasks_done), len(todos)))
    for task in tasks_done:
        print("\t {}".format(task))

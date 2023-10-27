#!/usr/bin/python3
""" API from Placeholdder """
import requests
from sys import argv


if __name__ == '__main__':
    todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos?user_Id={}".format(
                int(argv[1]))
            )
    user = requests.get(
            "https://jsonplaceholder.typicode.com/users?id={}".format(
                int(argv[1]))
            )
    done = 0
    total = 0
    tasks_done = []
    for todo in todos.json():
        if todo['completed'] is True:
            tasks_done.append(todo['title'])
            done += 1
        total += 1

    print("Employee {} is done with tasks({}/{}):".format(
            user.json()[0]['name'], done, total))
    for task in tasks_done:
        print("\t {}".format(task))

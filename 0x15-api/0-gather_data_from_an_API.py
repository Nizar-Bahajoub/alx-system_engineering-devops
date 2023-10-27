#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def get_todo(id):
    """ Fetch user name """

    resp = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    name = None
    for i in resp:
        if i['id'] == id:
            name = i['name']

    complete = []
    count = 0
    for todo in todos:
        if todo['userId'] == id:
            if todo['completed'] is True:
                complete.append(todo['title'])
            count += 1

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(complete), count))
    for done in complete:
        print("\t {}".format(done))


if __name__ == "__main__":
    get_todo(int(sys.argv[1]))

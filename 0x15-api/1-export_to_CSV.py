#!/usr/bin/python3
""" Gathering Data using API + Exporting to CSV """

from requests import *
from sys import argv


if __name__ == "__main__":
    user = get("https://jsonplaceholder.typicode.com/users/{}".format(
                argv[1])).json()
    user_tasks = get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                    argv[1])).json()

    user_id = str(argv[1])
    user_name = str(user.get("username"))
    file_name = user_id + ".csv"
    with open(file_name, mode='w') as f:
        for task in user_tasks:
            task = '"{}","{}","{}","{}"\n'.format(
                    user_id, user_name,
                    str(task["completed"]),
                    str(task["title"]))
            f.write(task)

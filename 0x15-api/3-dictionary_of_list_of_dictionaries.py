#!/usr/bin/python3
""" Gathering Data of all employees using API + Exporting to JSON """

import json
from requests import *
from sys import argv


if __name__ == "__main__":
    tasks = get(
            "https://jsonplaceholder.typicode.com/todos").json()

    users_id = set([todo["userId"] for todo in tasks])

    my_dict = {}
    for user_id in users_id:
        user_tasks = [task for task in tasks if task["userId"] == user_id]
        user_data = get(
            "https://jsonplaceholder.typicode.com/users/{}".format(
                user_id)).json()

        my_dict[user_id] = []
        for task in user_tasks:
            my_dict[user_id].append(
                    {
                        "username": user_data.get("username"),
                        "task": task.get("title"),
                        "completed": task.get("completed")
                    }
            )

    with open("todo_all_employees.json", mode='w') as f:
        json.dump(my_dict, f)

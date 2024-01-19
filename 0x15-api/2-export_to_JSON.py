#!/usr/bin/python3
""" Gathering Data using API + Exporting to JSON """

import json
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
    file_name = user_id + ".json"
    with open(file_name, mode='w') as f:
        my_dict = {
                user_id: [
                    {
                        "task": task["title"],
                        "completed": task["completed"],
                        "username": user_name
                    }
                    for task in user_tasks
                ]
        }
        json.dump(my_dict, f)

    print(my_dict)

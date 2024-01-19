#!/usr/bin/python3
""" Gathering Data using API """

from requests import *
from sys import argv


user = get("https://jsonplaceholder.typicode.com/users/{}".format(
            argv[1])).json()
user_tasks = get("https://jsonplaceholder.typicode.com/todos?userId={}".format(
                    argv[1])).json()
done_tasks = [task for task in user_tasks if task["completed"]]
all_tasks = get("https://jsonplaceholder.typicode.com/todos").json()

print("Employee {} is done with done with tasks({}/{})".format(
        user.get("name"), len(done_tasks), len(user_tasks)))

for i in done_tasks:
    print("\t {}".format(i["title"]))

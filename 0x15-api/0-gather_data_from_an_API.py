#!/usr/bin/python3
""" First API """
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    response = requests.get(todos_url)

    if response.status_code != 200:
        print("Failed to retrieve data for employee ID {}.".format(
            employee_id))
        return

    todos = response.json()

    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos)

    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name', 'Unknown')

    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name, num_completed_tasks, total_tasks)
        )
    for task in completed_tasks:
        print("\t{}".format(task['title']))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

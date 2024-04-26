#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her To Do list progress.
"""
import requests
import sys


def TODO_PROGRESS():
    user_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos_url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        user_id)
    name = requests.get(user_url).json().get('name')
    todo_response = requests.get(todos_url).json()
    tasks = [task.get('title')
             for task in todo_response if task.get('completed')]

    print('Employee {} is done with tasks({}/{}):'.format(name,
          len(tasks), len(todo_response)))
    print('\n'.join('\t {}'.format(task) for task in tasks))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        TODO_PROGRESS()

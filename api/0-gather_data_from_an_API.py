#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given
"""

import requests
from sys import argv

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'

    todos_url = main_url + "/todos?userId={}".format(argv[1])
    employee_url = main_url + "/users/{}".format(argv[1])

    todos_result = requests.get(todos_url).json()
    employee_result = requests.get(employee_url).json()

    todo_num = len(todos_result)
    todo_complete = len([todo for todo in todos_result
                         if todo.get("completed")])
    employee = employee_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(employee, todo_complete, todo_num))
    for todo in todos_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))

#!/usr/bin/python3
import requests
import sys


def employed_todo(employee_id):
    """Retrieve and print the TODO list progress of an employee given their ID.

    Args:
        employee_id (int): The ID of the employee.

    """
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{employee_id}"
    todo_url = f"{base_url}todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        # Check if responses are successful
        if user_response.status_code != 200 or todo_response.status_code != 200:
            print("Failed to retrieve data from the API.")
            return

        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_name = user_data["name"]
        total_number_of_tasks = len(todo_data)
        number_of_done_tasks = sum(1 for task in todo_data if task["completed"])

        completed_tasks_titles = [task["title"] for task in todo_data if task["completed"]]

        print(
            f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):"
        )
        for task_title in completed_tasks_titles:
            print(f"\t {task_title}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Check if the employee ID is provided
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            employed_todo(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")

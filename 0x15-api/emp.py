import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    # Fetching employee data
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    # Fetching TODO list of the employee
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Counting completed tasks
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    # Displaying employee's TODO list progress
    print("Employee {} is done with tasks ({}/{}):".format(employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task['title']))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

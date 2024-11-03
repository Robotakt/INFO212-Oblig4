# Initialize an empty dictionary to store employee information
employees = {}

# Function to create a new employee entry
def create_employee(employee_id, name, address, branch):
    employees[employee_id] = {
        "name": name,
        "address": address,
        "branch": branch
    }
    print(f"Employee with ID {employee_id} created successfully.")

# Function to read an employee entry by their ID
def read_employee(employee_id):
    if employee_id in employees:
        print(f"Details for Employee ID {employee_id}:")
        for key, value in employees[employee_id].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print(f"Employee with ID {employee_id} not found.")

# Function to update an employee entry
def update_employee(employee_id, name=None, address=None, branch=None):
    if employee_id in employees:
        if name:
            employees[employee_id]["name"] = name
        if address:
            employees[employee_id]["address"] = address
        if branch:
            employees[employee_id]["branch"] = branch
        print(f"Employee with ID {employee_id} updated successfully.")
    else:
        print(f"Employee with ID {employee_id} not found.")

# Function to delete an employee entry
def delete_employee(employee_id):
    if employee_id in employees:
        del employees[employee_id]
        print(f"Employee with ID {employee_id} deleted successfully.")
    else:
        print(f"Employee with ID {employee_id} not found.")
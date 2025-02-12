import random
from file_handler import read_csv, write_csv

def assign_secret_santa(employees, previous_assignments):
    """Assigns Secret Santa pairs with error handling."""
    if not employees:
        print("Error: Employee list is empty. Cannot assign Secret Santa.")
        return None

    employees_list = employees[:]  # Copy the list to avoid modifying the original
    random.shuffle(employees_list)  # Shuffle for randomness

    assignments = []
    assigned_children = set()
    
    for employee in employees:
        possible_children = [e for e in employees_list 
                             if e["Employee_EmailID"] != employee["Employee_EmailID"] and
                             e["Employee_EmailID"] not in assigned_children and
                             not was_assigned_last_year(employee, e, previous_assignments)]

        if not possible_children:
            print("Error: Failed to assign unique Secret Santa. Retrying...")
            return None  # Instead of infinite retrying, return None for handling in `main.py`

        secret_child = random.choice(possible_children)
        assigned_children.add(secret_child["Employee_EmailID"])

        assignments.append({
            "Employee_Name": employee["Employee_Name"],
            "Employee_EmailID": employee["Employee_EmailID"],
            "Secret_Child_Name": secret_child["Employee_Name"],
            "Secret_Child_EmailID": secret_child["Employee_EmailID"]
        })

    return assignments

def was_assigned_last_year(employee, potential_child, previous_assignments):
    """Check if the employee had the same secret child last year."""
    for assignment in previous_assignments:
        if (assignment["Employee_EmailID"] == employee["Employee_EmailID"] and
            assignment["Secret_Child_EmailID"] == potential_child["Employee_EmailID"]):
            return True
    return False

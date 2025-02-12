from file_handler import read_csv, write_csv
from secret_santa import assign_secret_santa

# Read input CSV files
employees = read_csv("employee.csv")
previous_assignments = read_csv("previous_assignment.csv")

# Check if employee list is empty
if not employees:
    print("Error: No employees found. Please check 'employees.csv'.")
else:
    assignments = assign_secret_santa(employees, previous_assignments)

    # Handle failed assignment
    if assignments:
        write_csv("output.csv", assignments, 
                  ["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"])
        print("Secret Santa assignments saved to output.csv!")
    else:
        print("Error: Could not generate Secret Santa assignments.")

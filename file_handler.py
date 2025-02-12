import csv
import os  # Add this at the beginning of the file
import csv  # Assuming CSV module is also needed

def read_csv(file_path):
    """Reads a CSV file and returns a list of dictionaries."""
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []

def write_csv(file_path, data, fieldnames):
    """Writes data to a CSV file."""
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")
def read_csv(filename):
    """Reads a CSV file and returns a list of dictionaries."""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return []

    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if reader.fieldnames is None:
                print(f"Error: File '{filename}' is empty or improperly formatted.")
                return []

            employees = [row for row in reader if row.get("Employee_EmailID")]
            
            # Check for duplicate email IDs
            emails = set()
            for emp in employees:
                if emp["Employee_EmailID"] in emails:
                    print(f"Warning: Duplicate employee '{emp['Employee_Name']}' found.")
                emails.add(emp["Employee_EmailID"])

            return employees
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return []

def write_csv(filename, data, fieldnames):
    """Writes data to a CSV file."""
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Successfully wrote data to '{filename}'.")
    except Exception as e:
        print(f"Error writing to file '{filename}': {e}")
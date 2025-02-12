import unittest
from secret_santa import assign_secret_santa, was_assigned_last_year

class TestSecretSanta(unittest.TestCase):

    def setUp(self):
        """Setup sample employee data and previous assignments"""
        self.employees = [
            {"Employee_Name": "Alice", "Employee_EmailID": "alice@example.com"},
            {"Employee_Name": "Bob", "Employee_EmailID": "bob@example.com"},
            {"Employee_Name": "Charlie", "Employee_EmailID": "charlie@example.com"}
        ]

        self.previous_assignments = [
            {"Employee_Name": "Alice", "Employee_EmailID": "alice@example.com",
             "Secret_Child_Name": "Bob", "Secret_Child_EmailID": "bob@example.com"},
            {"Employee_Name": "Bob", "Employee_EmailID": "bob@example.com",
             "Secret_Child_Name": "Charlie", "Secret_Child_EmailID": "charlie@example.com"},
            {"Employee_Name": "Charlie", "Employee_EmailID": "charlie@example.com",
             "Secret_Child_Name": "Alice", "Secret_Child_EmailID": "alice@example.com"}
        ]

    def test_no_self_assignment(self):
        """Test that no employee is assigned to themselves"""
        assignments = assign_secret_santa(self.employees, self.previous_assignments)
        for assignment in assignments:
            self.assertNotEqual(assignment["Employee_EmailID"], assignment["Secret_Child_EmailID"])

    def test_unique_assignments(self):
        """Test that each employee is assigned a unique secret child"""
        assignments = assign_secret_santa(self.employees, self.previous_assignments)
        assigned_children = {a["Secret_Child_EmailID"] for a in assignments}
        self.assertEqual(len(assigned_children), len(self.employees))

    def test_no_repeat_from_last_year(self):
        """Test that no one is assigned the same secret child as last year"""
        assignments = assign_secret_santa(self.employees, self.previous_assignments)
        for assignment in assignments:
            self.assertFalse(was_assigned_last_year(assignment, 
                                                    {"Employee_EmailID": assignment["Secret_Child_EmailID"]},
                                                    self.previous_assignments))

if __name__ == '__main__':
    unittest.main()

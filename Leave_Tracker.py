class Employee:
    def _init_(self, employee_id, employee_name):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.leaves = []

class LeaveTracker:
    def _init_(self, company_name):
        self.company_name = company_name
        self.employees = {}

    def add_employee(self, employee_id, employee_name):
        if employee_id not in self.employees:
            self.employees[employee_id] = Employee(employee_id, employee_name)
            print(f"Employee {employee_name} added successfully.")

    def add_leave(self, employee_id, start_date, end_date, leave_type):
        if employee_id in self.employees:
            employee = self.employees[employee_id]
            employee.leaves.append((start_date, end_date, leave_type))
            print("Leave added successfully.")
        else:
            print("Employee not found.")

    def list_leaves(self, employee_id):
        if employee_id in self.employees:
            employee = self.employees[employee_id]
            print(f"Leaves for Employee {employee.employee_name}:")
            for idx, leave in enumerate(employee.leaves, start=1):
                print(f"Leave {idx}:")
                print(f"Start Date: {leave[0]}")
                print(f"End Date: {leave[1]}")
                print(f"Leave Type: {leave[2]}")
                print("-----------")
        else:
            print("Employee not found.")

def main():
    company_name = "TCOER"
    tracker = LeaveTracker(company_name)

    while True:
        print(f"Welcome to {company_name} Leave Tracker")
        print("1. Add Employee")
        print("2. Add Leave")
        print("3. List Leaves")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            employee_id = input("Enter Employee ID: ")
            employee_name = input("Enter Employee Name: ")
            tracker.add_employee(employee_id, employee_name)

        elif choice == "2":
            employee_id = input("Enter Employee ID: ")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
            leave_type = input("Enter Leave Type: ")
            tracker.add_leave(employee_id, start_date, end_date, leave_type)

        elif choice == "3":
            employee_id = input("Enter Employee ID: ")
            tracker.list_leaves(employee_id)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please select again.")

if _name_ == "_main_":
    main()

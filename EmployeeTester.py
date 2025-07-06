class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, basic_salary):
        hra = 0.2 * basic_salary
        da = 0.1 * basic_salary
        tax = 0.15 * basic_salary
        gross_salary = basic_salary + hra + da - tax
        self.employees.append({
            "Employee ID": emp_id,
            "Employee Name": name,
            "Basic Salary": basic_salary,
            "Gross Salary": gross_salary
        })

    def display_report(self):
        print("\nEmployee Report:")
        print("ID\tName\t\tBasic Salary\tGross Salary")
        for emp in self.employees:
            print(f"{emp['Employee ID']}\t{emp['Employee Name']}\t{emp['Basic Salary']}\t\t{emp['Gross Salary']:.2f}")

    def search_employee(self, emp_id):
        for emp in self.employees:
            if emp["Employee ID"] == emp_id:
                return emp
        return None

    def menu(self):
        while True:
            print("\nEmployee Management System")
            print("1. Add Employee")
            print("2. Display Employee Report")
            print("3. Search Employee")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Employee Name: ")
                try:
                    basic_salary = float(input("Enter Basic Salary: "))
                    self.add_employee(emp_id, name, basic_salary)
                except ValueError:
                    print("Invalid input for salary. Please enter a number.")
            elif choice == "2":
                self.display_report()
            elif choice == "3":
                emp_id = input("Enter Employee ID to search: ")
                emp = self.search_employee(emp_id)
                if emp:
                    print("\nEmployee Found:")
                    print(f"ID: {emp['Employee ID']}\nName: {emp['Employee Name']}\nBasic Salary: {emp['Basic Salary']}\nGross Salary: {emp['Gross Salary']:.2f}")
                else:
                    print("Employee not found.")
            elif choice == "4":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Test cases
def test_employee_management_system():
    system = EmployeeManagementSystem()

    # Unit Testing
    system.add_employee("E001", "Alice", 50000)
    assert system.employees[0]["Gross Salary"] == 57500.0

    system.add_employee("E002", "Bob", 60000)
    assert system.employees[1]["Gross Salary"] == 69000.0

    # Conditional Testing
    assert system.search_employee("E001") is not None
    assert system.search_employee("E003") is None

    # Decision Coverage Testing
    assert len(system.employees) == 2
    system.display_report()

    # Loop Testing (3 iterations)
    system.add_employee("E003", "Charlie", 70000)
    assert len(system.employees) == 3
    path_iteration = [
        {"Employee ID": "E001", "Gross Salary": 57500.0},
        {"Employee ID": "E002", "Gross Salary": 69000.0},
        {"Employee ID": "E003", "Gross Salary": 80500.0}
    ]
    for i, emp in enumerate(system.employees):
        assert emp["Employee ID"] == path_iteration[i]["Employee ID"]
        assert emp["Gross Salary"] == path_iteration[i]["Gross Salary"]

if __name__ == "__main__":
    system = EmployeeManagementSystem()
    system.menu()

# Run test cases
test_employee_management_system()

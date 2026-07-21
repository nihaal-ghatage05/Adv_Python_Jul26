class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def calculate_salary(self):
        pass



class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, monthly_salary):
        super().__init__(employee_id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary



class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, hours_worked, hourly_rate):
        super().__init__(employee_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate



class ContractEmployee(Employee):
    def __init__(self, employee_id, name, project_amount, bonus):
        super().__init__(employee_id, name)
        self.project_amount = project_amount
        self.bonus = bonus

    def calculate_salary(self):
        return self.project_amount + self.bonus



class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def generate_payroll(self):
        total_payroll = 0

        for employee in self.employees:
            salary = employee.calculate_salary()   # Polymorphism

            print("Employee ID :", employee.employee_id)
            print("Name :", employee.name)
            print("Salary : ₹", salary)
            print()

            total_payroll += salary

        print("Total Payroll = ₹", total_payroll)




# Full Time Employee
emp1 = FullTimeEmployee("E101", "Nihaal", 60000)

# Part Time Employee
emp2 = PartTimeEmployee("E102", "Om", 120, 400)

# Contract Employee
emp3 = ContractEmployee("E103", "Anish", 45000, 5000)

# Payroll Object
payroll = Payroll()

# Add Employees
payroll.add_employee(emp1)
payroll.add_employee(emp2)
payroll.add_employee(emp3)

# Generate Payroll
payroll.generate_payroll()
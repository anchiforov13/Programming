from datetime import datetime
from validator import Validator

class Employee:
    def __init__(self, name, salary, firstWorkingDate, lastWorkingDate):
        self.name = name
        self.salary = salary
        self.firstWorkingDate = firstWorkingDate
        self.lastWorkingDate = lastWorkingDate

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}, First Working Date: {self.firstWorkingDate}, Last Working Date: {self.lastWorkingDate}"
    
class EmployeeCollection:
    def __init__(self):
        self.collection = []
    
    def addEmployee(self, emp):
        self.collection.append(emp)

    def calculate_total_salary(self):
        total_salary = 0
        today = datetime.today()

        for emp in self.collection:
            firstWD = datetime.strptime(emp.firstWorkingDate, "%Y-%m-%d")
            working_days = (today - firstWD).days
            working_months = working_days // 30
            salary = float(emp.salary)

            for i in range(working_months // 6):
                salary *= 1.15

            total_salary += salary

        return total_salary
    
    def write_employees_by_years(self, filename):
        today = datetime.today()
        with open(filename, 'w') as file:
            for emp in self.collection:
                firstWD = datetime.strptime(emp.firstWorkingDate, "%Y-%m-%d")
                working_days = (today - firstWD).days
                working_years = working_days / 365
                if 1 <= working_years <= 20:
                    file.write(f"{emp.name}, {int(working_years)} year{'s' if working_years > 1 else ''}\n")

def read_collection_from_file(filename):
    collection = EmployeeCollection()
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(', ')
                name, salary, firstWorkingDate, lastWorkingDate = data
                employee = Employee(name, salary, firstWorkingDate, lastWorkingDate)
                collection.addEmployee(employee)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    return collection
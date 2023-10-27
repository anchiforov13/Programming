from datetime import datetime, timedelta
from employee import Employee, EmployeeCollection, read_collection_from_file
from validator import Validator

def menu():
    while True:
            filename = input("Enter the file name: ")
            emp_collection = read_collection_from_file(filename)
            if emp_collection is not None:
                break

    while True:
        choice = input("1 to add new employee, 2 to count spendings on salaries, 3 to write employees to file by year, 4 to print all employees, 0 to exit: ")

        match(choice):
            case "1":
                name = input("Enter employee name: ")
                salary = input("Enter salary: ")
                firstWorkingDate = input("Enter first working date in format YYYY-MM-DD ")

                if not Validator.is_valid_name(name) or not Validator.is_valid_price(salary) or not Validator.is_valid_date(firstWorkingDate):
                    continue

                firstWorkingDate = datetime.strptime(firstWorkingDate, "%Y-%m-%d")

                min_last_working_date = firstWorkingDate + timedelta(days=90)

                lastWorkingDate = input(f"Enter last working date(first working date: {min_last_working_date.strftime('%Y-%m-%d')}), or 'Null' if the employee still works): ")
                if lastWorkingDate.lower() != "Null":
                    if not Validator.is_valid_date(lastWorkingDate, min_last_working_date):
                        continue
                    lastWorkingDate = datetime.strptime(lastWorkingDate, "%Y-%m-%d")
                else:
                    lastWorkingDate = None

                new_employee = Employee(name, float(salary), firstWorkingDate, lastWorkingDate)
                emp_collection.addEmployee(new_employee)

            case "2":
                total_salary = emp_collection.calculate_total_salary()
                print(f"Overall company spendings on salary: ${total_salary:.2f}")

            case "3":
                filename_by_years = "employees_by_years.txt"
                emp_collection.write_employees_by_years(filename_by_years)
                print(f"Employees added to file {filename_by_years}")

            case "4":
                print("All employees:")
                for employee in emp_collection.collection:
                    print(employee)

            case "0":
                break

if __name__ == "__main__":
    menu()
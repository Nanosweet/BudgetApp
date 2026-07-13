
class EmployeeService():
    def __init__(self, employees):
        self.employees = employees
    def filter_department(self, department):
        return [
            f"{employee['imie']}, {employee['nazwisko']}"          
            for employee in self.employees
            if employee['dzial'] == department
        ]
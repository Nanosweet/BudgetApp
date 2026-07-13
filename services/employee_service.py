class EmployeeService:
    def __init__(self, employees):
        self.employees = employees
        self._pensja = []
    def filter_department(self, department):
        return [
            f"{employee['imie']}, {employee['nazwisko']}, - {employee['dzial']}"          
            for employee in self.employees
            if employee['dzial'] == department
        ]
    def get_employees(self):
        return [
            f"{employee['imie']} {employee['nazwisko']} - {employee['pensja']}"          
            for employee in self.employees
        ]
    def get_avarage_salary(self):
        suma = 0
        for s in self.employees:
            s['pensja'] = float(s['pensja'])
            suma += s['pensja']
        return f"Średnia pensja w firmie = {round(suma/len(self.employees))}"
    def get_lowest_salary(self):
        return min(self.pensja)
    def get_highest_salary(self):
        return max(self.pensja)
    def get_avg_salary_by_department(self, department):
        salary_department = [row for row in self.employees if row['dzial'] == department]
        suma = 0
        for s in salary_department:
            s['pensja'] = float(s['pensja'])
            suma += s['pensja']
        return round(suma/len(salary_department))
    
    @property
    def pensja(self):
        return [float(p['pensja']) for p in self.employees]


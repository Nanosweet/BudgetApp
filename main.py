from config import files
from repositories.csv_repository import CsvRepository
from report import Report
from services.employee_service import EmployeeService


repo = CsvRepository()
report = Report()
pracownicy = files['pracownicy']
data = repo.load(pracownicy)
sort_naziwsko = sorted(data, key=lambda x: x['nazwisko'])

pracownicy_z_klasy = EmployeeService(data)

report.print_result(pracownicy_z_klasy.filter_department('HR'))

numbers = [3, 8, 1, 10, 15, 6]

n = [number for number in numbers if number % 2 == 0]



print(n)
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
#for p in pracownicy_z_klasy.filter_department('IT')

#for p in sort_naziwsko:
#    if p['dzial'] == 'IT':
#        report.print_result(p)
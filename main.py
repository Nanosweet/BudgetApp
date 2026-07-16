from config import files
from repositories.csv_repository import CsvRepository
from report import Report
from services.employee_service import EmployeeService
from services.products_service import ProductsService
from services.grade_service import GradeService
from services.sales_service import SalesService

repo = CsvRepository()
report = Report()
data_employees = repo.load(files['pracownicy'])
sort_naziwsko = sorted(data_employees, key=lambda x: x['nazwisko'])
pracownicy = EmployeeService(data_employees)
produkty = ProductsService(repo.load(files['produkty']))
oceny = GradeService(repo.load(files['oceny_uczniow']))
sprzedaz = SalesService(repo.load(files['sprzedaz']))

def zadanie1_1():  
    report.print_result(pracownicy.get_employees())

def zadanie1_2():
    report.print_result(pracownicy.filter_department('IT'))

def zadanie1_3():
    report.print_result(produkty.get_available_products())

def zadanie2_1a():
    report.result(pracownicy.get_avarage_salary())
    
def zadanie2_1b():
    report.result(pracownicy.get_lowest_salary())
    
def zadanie2_1b2():
    report.result(pracownicy.get_highest_salary())
    
def zadanie2_1c():
    report.result(pracownicy.get_avg_salary_by_department('HR'))
    
def zadanie2_2a():
    report.print_result(oceny.get_avg_grade())

def zadanie2_2c():
    report.result(oceny.get_empty_grade())
def zadanie3_1a():
    report.result(sprzedaz.overall_earnings())
zadanie3_1a()

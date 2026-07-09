from config import files
from repositories.csv_repository import CsvRepository


repo = CsvRepository()
pracownicy = files['pracownicy']
data = repo.load(pracownicy)


for row in data:
    print (row)
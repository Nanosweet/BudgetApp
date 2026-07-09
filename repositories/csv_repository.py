# Zadaniem tego skryptu jest tylko odczyt i zapis danych (moze później)
import csv
class CsvRepository():
    def load(self, filename):
        with open(filename, 'r', encoding='utf-8') as csv_data:
            reader = csv.DictReader(csv_data)
            return list(reader)

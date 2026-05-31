# Czyta CSV i zwraca liste slownikowa

import csv
import utils


def wczytaj_dane(path):
    # Czytaj dane CSV i zwroc liste slownikow
    transakcje = []
    with open(path, newline='', encoding ='utf-8') as f:
        reader_dict = csv.DictReader(f)
        for row in reader_dict:
            print(utils.waliduj_wiersz(row))
            #print(f'{row} - ')



    #try:
      #  with open(path, newline='') as csvfile:
            #reader = csv.DictReader(csvfile)
        #    csv_f = csv.reader(csvfile, delimiter=' ', quotechar='|')
            #for row in csv_f:
                #print(', '.join(row))
                # waliduj wiersz
                #print(transakcje)
                #utils.waliduj_wiersz(row)
    #except FileNotFoundError:
        #print('File not found')


wczytaj_dane('wydatki.csv')

def read_single_line(path):
    with open(path, newline='') as csvfile:
         csv_f = csv.reader(csvfile, delimiter=' ', quotechar='|')
         print(next(csv_f))

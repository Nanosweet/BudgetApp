# Czyta CSV i zwraca liste slownikowa

import csv
import utils


def wczytaj_dane(path):
    # Czytaj dane CSV i zwroc liste slownikow
    transakcje = []
    with open(path, newline='', encoding ='utf-8') as f:
        reader_dict = csv.DictReader(f)
        for row in reader_dict:
            utils.waliduj_wiersz(row)
            transakcje.append(row)

        return transakcje

x = wczytaj_dane('wydatki.csv')
suma = ''
for a in x:
    if float(a['kwota']) < 0:
        a["xyz"] = True
    print (a)

# Co mozna zrobic z dictionary -> lista
'''
    Podlicz liczbe wydatkow
    podlicz sume kazdej kategorii
    znajdz najwiekszy wydatek
    znajdz najmniejszy wydatek
    wyswietl 3 najdrozsze wydatki
    oblicz sredni wydatek
    pokaz liczbe transakcji w kazdej kategorii

'''


    #suma += float(a['kwota'])
    
#print (x)
#print(type(x))
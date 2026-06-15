# Poziom 1 Zadanie 1.1


import csv
from pathlib import Path # OOP sprawdzanie pliku i sciezek

files = {
    "oceny_uczniow":Path("files/oceny_uczniow.csv"),
    "pracownicy": Path("files/pracownicy.csv"),
    "produkty": Path("files/produkty.csv"),
    "sprzedaz" : Path("files/sprzedaz_2024.csv"),
    }

pracownicy_csv_path = Path('files/pracownicy.csv')

def validate_files(files):
    for file, path in files.items():
        if not path.exists():
            raise FileNotFoundError(f"File <{file}> does not exists")
    return True  

def zadanie1_1():
    # wczytaj plik pracownicy.csv
    try:
        validate_files(files) # walidacja
        # otwieranie newline bo Windows, encoding bo polskie znaki
        with open(files['pracownicy'], newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"{row['imie']} {row['nazwisko']} - {row['pensja']}")

    except FileNotFoundError as e:
        print (e)



def zadanie1_2():
    try:
        validate_files(files)
        with open(files['pracownicy'], newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            dzial_IT = []
            for row in reader:
                if row['dzial'] == 'IT':
                    dzial_IT.append(row)
            for p in sorted(dzial_IT, key=lambda x: x["nazwisko"]):
                print(p["imie"], p["nazwisko"])
    except FileNotFoundError as e:
        print(e)

def zadanie1_2x():
    try:
        validate_files(files)
        with open(files['pracownicy'], newline='', encoding='utf-8') as pracownicy:
            reader = csv.DictReader(pracownicy)
            pracownicy_it = [row for row in reader if row['dzial'] == 'IT']
            for p in sorted(pracownicy_it, key=lambda x: x['nazwisko']):
                print(p['imie'], p['nazwisko'])
    except FileNotFoundError as e:
        print(e)

# Zadanie 1.3 - Produkty dostępne('produkty.csv')
# Wypisz nazwy i ceny wszystkich produktów, które są dostępne
# ('dostępny == "tak"') = posortowane od nadroższego do najtańszego

def zadanie1_3():
    try:
        validate_files(files)
        with open(files['produkty'], newline='', encoding='utf-8') as produkty:
            reader = csv.DictReader(produkty)
            for row in reader:
                dostepne_produkty = [row for row in reader if row['dostepny'] == 'tak']
            for p in sorted(dostepne_produkty, key= lambda x: float(x['cena']), reverse=True):
                print(p['nazwa'],(p['cena']))

    except FileNotFoundError as e:
        print(e)

def zadanie1_4():
    try:
        validate_files(files)
        with open(files['pracownicy'], newline='', encoding='utf-8') as p:
            reader = csv.DictReader(p)
            pensje_pracownikow = []
            tylko_pensje = []
            #dzial_it = [row for row in reader if row['dzial'] == 'IT']

            for row in reader:
                #srednia_pensja = [row ]\
                row['pensja'] = float(row['pensja'])
                pensje_pracownikow.append(row)
                tylko_pensje.append(row['pensja'])
            #print (max(pensje_pracownikow))
            #print (pensje_pracownikow['pensja'])
            #print (min(pensje_pracownikow))

            # Funkcja lamda pozwalaja filtrowac slowniki klucz wartosc
            max_pensja = max(pensje_pracownikow, key=lambda x: x['pensja'])
            min_pensja = min(pensje_pracownikow, key=lambda x: x['pensja'])
            #print(pensje_pracownikow['dzial'])
            


            print (f"Najlepiej zarabia: {max_pensja['imie']} - {max_pensja['pensja']}")
            print (f"Najlepiej zarabia: {min_pensja['imie']} - {min_pensja['pensja']}")
            

            print (round(sum(tylko_pensje)/len(tylko_pensje),2))
            
            suma = 0
            dzial_it = []
            for p in pensje_pracownikow:
                if p['dzial'] == 'IT':
                    dzial_it.append(p)
                    suma += p['pensja']
            print(f"Średnia zarobków w dziale IT wynosi: {suma/len(dzial_it)}")
            print()  
                    #print (sum(p['pensja'])/len(pensje_pracownikow))
                #pass
            #print(dzial_it)



    except FileNotFoundError as e:
        print (e)

# Zadanie 2.2
# srednia p




print (zadanie1_4())
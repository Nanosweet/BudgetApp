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

# Poziom 2 - średni
# Zadanie 2.1 Statystyki pensji ('pracownicy.csv')
# Oblicz i wypisz:
# - średnią pensję w calej firmie
# - najwyższą i najniższą pensję ( wraz z imieniem i nazwiskiem )
def zadanie2_1():
    srednia_pensja = 0
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
            
            srednia_pensja = round(sum(tylko_pensje)/len(tylko_pensje),2)

            for p in pensje_pracownikow:
                print (p['dzial'])
            
            
            suma_it = 0
            suma_hr = 0
            suma_zaz = 0
            suma_sprz = 0
            dzial_it = []
            dzial_it2 = [x for x in pensje_pracownikow if x['dzial'] == 'IT']
            dzial_hr = []
            dzial_zaz = []
            dzial_sprz = []
            for p in pensje_pracownikow:
                match p['dzial']:
                    case 'IT':
                        dzial_it.append(p)
                        suma_it += p['pensja']
                    case 'HR':
                        dzial_hr.append(p)
                        suma_hr += p['pensja']
                    case 'Zarząd':
                        dzial_zaz.append(p)
                        suma_zaz += p['pensja']
                    case 'Sprzedaż':
                        dzial_sprz.append(p)
                        suma_sprz += p['pensja']
            
                    #print (sum(p['pensja'])/len(pensje_pracownikow))
                #pass
            #print(dzial_it)


            print(f"2.1 a) Średnia pensja z całej firmie wynosi {srednia_pensja}")
            
            print (f"2.1 b) Najwicej zarabia: {max_pensja['imie']} - {max_pensja['pensja']}")
            print (f"2.1 b) Najmniej zarabia: {min_pensja['imie']} - {min_pensja['pensja']}")
            print("2.1 c)" )
            print(f"    Średnia zarobków w dziale IT wynosi: {suma_it/len(dzial_it)}")
            
            print(f"    Średnia zarobków w dziale ZARZAD wynosi: {suma_zaz/len(dzial_zaz)}") 
            
            print(f"    Średnia zarobków w dziale HR wynosi: {suma_hr/len(dzial_hr)}") 

            suma_it2 = sum(person['pensja'] for person in dzial_it2)
            #suma += [dzial_it2, key=lambda x: x['pensja']]
            print(suma_it2, "#######")

    except FileNotFoundError as e:
        print (e)

# Zadanie 2.2
# srednia p




print (zadanie2_1())
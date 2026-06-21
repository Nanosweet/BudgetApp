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
# - średnią pensję osobno dla każdego działu
def zadanie2_1():
    srednia_pensja = 0
    try:
        validate_files(files)
        with open(files['pracownicy'], newline='', encoding='utf-8') as p:
            reader = csv.DictReader(p)
            pensje_pracownikow = []
            tylko_pensje = []

            for row in reader:
                row['pensja'] = float(row['pensja'])
                pensje_pracownikow.append(row)
                tylko_pensje.append(row['pensja'])
                
            max_pensja = max(pensje_pracownikow, key=lambda x: x['pensja'])
            min_pensja = min(pensje_pracownikow, key=lambda x: x['pensja'])
            
            srednia_pensja_w_firmie = round(sum(tylko_pensje)/len(tylko_pensje),2)
            
            
            suma_it = 0
            suma_hr = 0
            suma_zaz = 0
            suma_sprz = 0
            dzial_it = []
            
            # Mozna dodac do dzialu w petli for - dluzsza wersja
            # Tutaj dwie linijki zalatwiaja sprawe
            dzial_it2 = [dzial for dzial in pensje_pracownikow if dzial['dzial'] == 'IT']
            suma_it2 = sum(person['pensja'] for person in dzial_it2)
            
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


            print(f"""
            2.1 a) Średnia pensja z całej firmie wynosi - {srednia_pensja_w_firmie}
            2.1 b) Najwicej zarabia: {max_pensja['imie']} - {max_pensja['pensja']}
            2.1 b) Najmniej zarabia: {min_pensja['imie']} - {min_pensja['pensja']}
            2.1 c) 
                Średnia zarobków w dziale IT wynosi: {suma_it/len(dzial_it)}
                Średnia zarobków w dziale ZARZAD wynosi: {suma_zaz/len(dzial_zaz)}
                Średnia zarobków w dziale HR wynosi: {suma_hr/len(dzial_hr)}
                Średnia zarobków w dziale SPRZEDAŻY wynosi: {suma_sprz/len(dzial_sprz)}
                """) 


    except FileNotFoundError as e:
        print (e)

# Zadanie 2.2 - Brak danych ('oceny_uczniow.csv')
# oblicz srednia tylko z dostepnych ocen ( pomijaj puste )
# 


def zadanie2_2():
    try:
        validate_files(files)
        
        with open(files['oceny_uczniow'], newline='', encoding='utf-8') as oceny:
            oceny_uczniow = csv.DictReader(oceny)
            przedmioty = [
                "matematyka",
                "fizyka",
                "historia",
                "jezyk_angielski",
            ]
        
        for row in oceny_uczniow:

            suma = 0
            licznik = 0

            for przedmiot in przedmioty:
                if row[przedmiot] != "":
                    ocena = int(row[przedmiot])
                    suma += ocena
                    licznik += 1
                    row[przedmiot] = ocena  # opcjonalnie: zamiana na int

            if licznik > 0:
                srednia = suma / licznik
            else:
                srednia = 0
            
            print(f"{row['imie']} -> średnia: {srednia:.2f} | dane: {row}")
            
           # suma_przedmiotow = {przedmiot: 0 for przedmiot in przedmioty}
           # licznik_przedmiotow = {przedmiot: 0 for przedmiot in przedmioty}
            
           # for row in oceny_uczniow:   # for po {}
              # for przedmiot in przedmioty:  # for po przedmiotach
               #     if row[przedmiot] != "":    # jesli puste to zostaje ""
                        #row[przedmiot] = int(row[przedmiot])
                        
                  #      wartosc = int(row[przedmiot])
                 #       suma_przedmiotow[przedmiot] += wartosc
               #         licznik_przedmiotow[przedmiot] += 1
           #     print (row)
    # wypisanie średnich
        print("\nŚrednie z przedmiotów:")

       # for przedmiot in przedmioty:
       #     if licznik_przedmiotow[przedmiot] > 0:
        #        srednia = suma_przedmiotow[przedmiot] / licznik_przedmiotow[przedmiot]
       ##         print(f"{przedmiot}: {srednia:.2f}")
        #else:
            #print(f"{przedmiot}: brak danych")
        
    except FileNotFoundError as e:
        print (e)


def powtorka():
    try:
        validate_files(files)
        with open(files['pracownicy'], newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            pracownicy = [
                {**row, 'pensja': float(row['pensja'])}
                for row in reader
                ]
            #print(type(reader))
            print(max(pracownicy, key=lambda x: x['pensja']))


    except FileNotFoundError as e:
        print(e)


print (powtorka())
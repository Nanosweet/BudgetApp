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
'''
suma = ''
for a in x:
    if float(a['kwota']) < 0:
        a["xyz"] = True
    print (a)
'''
# Co mozna zrobic z dictionary -> lista
# csv.DictReader(f) jest iteratorem, kazdy wiersz to slownik
# Jesli chcesz miec wszystkie dane w pamieci to zamieniasz na liste list(reader)
def otworz_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            return row

content = otworz_csv('wydatki.csv')
print(type(content.keys()))
'''
    otworz plik csv zrob na dict
    Są dwie ważne zasady przy otwieraniu pliku CSV:

1. 1. Czym jest csv.DictReader?
csv.DictReader to klasa w Pythonie, która czyta plik CSV i zwraca każdy wiersz jako słownik (dict). Klucze słownika to nagłówki kolumn z pierwszego wiersza CSV.

Dzięki temu zamiast odwoływać się do danych przez indeks (np. row[0]), używasz nazwy kolumny (np. row["imie"]) — kod jest czytelniejszy i odporniejszy na zmiany.

import csv

# Plik data.csv zawiera:
# imie,wiek,miasto
# Anna,25,Kraków
# Piotr,30,Warszawa

with open("data.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["imie"], row["wiek"])

# Wynik:
# Anna 25
# Piotr 30

Tak! Każdy wiersz to dict, gdzie klucz = nazwa kolumny, wartość = zawartość komórki. To główna zaleta DictReader nad zwykłym csv.reader.

2. Otwieranie pliku poprawnie
    a. Zawsze używaj encoding="utf-8" (lub innego odpowiedniego) — inaczej polskie znaki mogą się sypać.
    b. Dodaj newline="" — zapobiega podwójnym pustym liniom na Windowsie (oficjalna rekomendacja z dokumentacji Pythona).
import csv

# Zalecany sposób otwierania:
with open("dane.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# Jeśli plik ma polskie znaki z Windows:
# encoding="cp1250" lub encoding="windows-1250"

3. Atrybut fieldnames

Po stworzeniu readera możesz sprawdzić nazwy kolumn przez reader.fieldnames. Uwaga: jest dostępne dopiero po odczytaniu pierwszego wiersza!

Możesz też podać własne nazwy kolumn ręcznie — przydatne gdy plik CSV nie ma nagłówka.

import csv

with open("dane.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    # Sprawdź nagłówki (dostępne po pierwszej iteracji):
    print(reader.fieldnames)  # None — jeszcze nie czytano!
    
    rows = list(reader)       # teraz czyta wszystko
    print(reader.fieldnames)  # ['imie', 'wiek', 'miasto']

# Plik BEZ nagłówka — podajemy własne:
with open("bez_naglowka.csv", newline="") as f:
    reader = csv.DictReader(f, fieldnames=["imie", "wiek"])
    
    
reader.fieldnames zwraca listę nazw kolumn, np. ['imie', 'wiek', 'miasto']. Pamiętaj: przed iteracją wartość to None!
    
Możesz przefiltrować wiersze używając zwykłego if w pętli lub list comprehension. 
Pamiętaj, że wartości z CSV to zawsze stringi — musisz je konwertować np. przez int() lub float(),
jeśli chcesz porównywać liczby.

4.  Możesz przefiltrować wiersze używając zwykłego if w pętli lub list comprehension.
    Pamiętaj, że wartości z CSV to zawsze stringi — musisz je konwertować np. przez int() lub float(), jeśli chcesz porównywać liczby.

with open("pracownicy.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    # Uwaga: row["wiek"] to STRING "25", nie int 25!
    dorośli = [
        row for row in reader
        if int(row["wiek"]) >= 18
    ]

# Filtr po kilku warunkach:
with open("pracownicy.csv", newline="") as f:
    reader = csv.DictReader(f)
    wynik = [
        row["imie"] for row in reader
        if int(row["wiek"]) > 25
        and row["miasto"] == "Warszawa"
    ]

row["cena"] to string np. "150.99" — Python porównuje stringi leksykograficznie, więc "9" > "100" jest True (błąd!). Zawsze konwertuj: float(row["cena"]) > 100.


import csv

with open("pracownicy.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    # Uwaga: row["wiek"] to STRING "25", nie int 25!
    dorośli = [
        row for row in reader
        if int(row["wiek"]) >= 18
    ]

# Filtr po kilku warunkach:
with open("pracownicy.csv", newline="") as f:
    reader = csv.DictReader(f)
    wynik = [
        row["imie"] for row in reader
        if int(row["wiek"]) > 25
        and row["miasto"] == "Warszawa"
    ]
    Zawsze konwertuj: float(row["cena"]) > 100.
    
    Reader to generator — można go przejść tylko raz! Żeby móc wielokrotnie używać danych,
    zamień na listę przez list(reader).
    Możesz też od razu przetworzyć dane przy wczytywaniu — np. skonwertować typy.
    
    import csv

def wczytaj_pracownikow(sciezka):
    with open(sciezka, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [
            {
                "imie": row["imie"],
                "wiek": int(row["wiek"]),       # konwersja!
                "pensja": float(row["pensja"]),  # konwersja!
                "miasto": row["miasto"].strip()  # usuń spacje
            }
            for row in reader
        ]
        
        reader.fieldnames zwraca listę nazw kolumn, np. ['imie', 'wiek', 'miasto']. Pamiętaj: przed iteracją wartość to None!

pracownicy = wczytaj_pracownikow("dane.csv")
# Teraz można używać wielokrotnie, typy są poprawne:
print(max(pracownicy, key=lambda p: p["pensja"]))


Reader to generator — można go przejść tylko raz! Żeby móc wielokrotnie używać danych,
zamień na listę przez list(reader).
Możesz też od razu przetworzyć dane przy wczytywaniu — np. skonwertować typy.

import csv

def wczytaj_pracownikow(sciezka):
    with open(sciezka, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [
            {
                "imie": row["imie"],
                "wiek": int(row["wiek"]),       # konwersja!
                "pensja": float(row["pensja"]),  # konwersja!
                "miasto": row["miasto"].strip()  # usuń spacje
            }
            for row in reader
        ]

pracownicy = wczytaj_pracownikow("dane.csv")
# Teraz można używać wielokrotnie, typy są poprawne:
print(max(pracownicy, key=lambda p: p["pensja"]))


Dlaczego reader to generator, a nie lista?
 Świetnie! Generator jest pamięciooszczędny — pliki CSV mogą mieć miliony wierszy.
 Jeśli plik jest mały lub potrzebujesz wielokrotnego dostępu, użyj list(reader) wewnątrz bloku with.


Nie każdy plik "CSV" używa przecinka. Pliki mogą używać średnika (;), tabulatora (\t), czy pionowej kreski (|). Parametr delimiter pozwala to ustawić.

Plik TSV (tab-separated) to częsty format eksportu z Excela i baz danych.

import csv

# Plik z średnikiem (typowy eksport z polskiego Excela):
with open("dane.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        print(row)

# Plik TSV (tabulatory):
with open("dane.tsv", newline="") as f:
    reader = csv.DictReader(f, delimiter="	")
    for row in reader:
        print(row["imie"])

# Automatyczne wykrywanie separatora:
import csv
with open("dane.csv") as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    f.seek(0)
    reader = csv.DictReader(f, dialect=dialect)
    
✅ Poprawnie! delimiter=";" ustawia średnik jako separator.

7. Brakujące dane i wartości domyślne
Domyślnie Python zakłada przecinek. Pamiętaj też o encoding przy plikach z polskimi znakami.
W prawdziwych danych często brakuje wartości. DictReader zwraca None dla brakujących kolumn, a pusty string "" dla pustych komórek. Parametr restval pozwala ustawić wartość domyślną dla brakujących pól.

✅ DictReader zwraca None dla brakujących pól — chyba że ustawisz restval. Zawsze warto używać row.get('klucz', domyślna) dla kluczy, które mogą nie istnieć.
8.
Para do DictReader to csv.DictWriter — zapisuje listę słowników do pliku CSV. Musisz podać fieldnames i wywołać writeheader() żeby zapisać nagłówki.

import csv

pracownicy = [
    {"imie": "Anna", "wiek": 25, "miasto": "Kraków"},
    {"imie": "Piotr", "wiek": 30, "miasto": "Warszawa"},
]

with open("wynik.csv", "w", newline="", encoding="utf-8") as f:
    pola = ["imie", "wiek", "miasto"]
    writer = csv.DictWriter(f, fieldnames=pola)
    
    writer.writeheader()       # zapisz nagłówki
    writer.writerows(pracownicy)  # zapisz wszystkie wiersze
    
# Wynik w wynik.csv:
# imie,wiek,miasto
# Anna,25,Kraków
# Piotr,30,Warszawa


Chcesz zapisać CSV ale słowniki mają dodatkowy klucz 'notatka' którego nie chcesz w pliku. Co zrobić?
extrasaction='ignore' jest wygodniejsze przy tworzeniu DictWriter

 Obie metody działają! extrasaction='ignore' jest wygodniejsze. Alternatywnie: {k: v for k, v in row.items() if k in fieldnames}. Domyślnie DictWriter rzuca ValueError przy nieznanym kluczu.
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
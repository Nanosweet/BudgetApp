# Zadania praktyczne — csv.DictReader

Pliki do zadań znajdziesz w tym samym folderze.

---

## 🟢 Poziom 1 — Podstawy

### Zadanie 1.1 — Czytanie i wypisywanie (`pracownicy.csv`)
Wczytaj plik `pracownicy.csv` i wypisz imię, nazwisko i pensję każdego pracownika
w formacie:
```
Anna Kowalska — 7500.00 zł
```

### Zadanie 1.2 — Filtrowanie (`pracownicy.csv`)
Wypisz tylko pracowników z działu **IT**, posortowanych alfabetycznie po nazwisku.

### Zadanie 1.3 — Produkty dostępne (`produkty.csv`)
Wypisz nazwy i ceny wszystkich produktów, które są dostępne (`dostepny == "tak"`),
posortowane od najdroższego do najtańszego.

---

## 🟡 Poziom 2 — Średni

### Zadanie 2.1 — Statystyki pensji (`pracownicy.csv`)
Oblicz i wypisz:
- średnią pensję w całej firmie
- najwyższą i najniższą pensję (wraz z imieniem i nazwiskiem pracownika)
- średnią pensję osobno dla każdego działu

### Zadanie 2.2 — Braki danych (`oceny_uczniow.csv`)
Plik zawiera puste komórki. Dla każdego ucznia:
- oblicz średnią tylko z dostępnych ocen (pomijaj puste)
- wypisz uczniów z obliczoną średnią, posortowanych od najlepszej do najgorszej
- wypisz ilu uczniom brakuje co najmniej jednej oceny

### Zadanie 2.3 — Raport kategorii (`produkty.csv`)
Dla każdej kategorii produktów oblicz:
- liczbę produktów
- łączną wartość magazynową (cena × stan_magazynowy)
- średnią ocenę produktów w tej kategorii

---

## 🔴 Poziom 3 — Zaawansowany

### Zadanie 3.1 — Analiza sprzedaży (`sprzedaz_2024.csv`)
Oblicz:
- całkowity przychód każdego sprzedawcy (ilość × cena_jednostkowa)
- który sprzedawca miał najwyższy przychód w każdym miesiącu?
- który region generuje największe przychody?

### Zadanie 3.2 — Łączenie plików (`pracownicy.csv` + `sprzedaz_2024.csv`)
Kolumna `sprzedawca` w pliku sprzedaży zawiera "imie nazwisko".
- Połącz dane: dla każdego sprzedawcy z `pracownicy.csv` dodaj jego łączny przychód ze sprzedaży
- Wypisz: imię, nazwisko, dział, pensja, łączna sprzedaż
- Posortuj po łącznej sprzedaży malejąco

### Zadanie 3.3 — Zapis wyników (`sprzedaz_2024.csv`)
Wczytaj dane sprzedażowe, oblicz dla każdego wiersza pole `wartosc` (ilość × cena),
a następnie zapisz NOWY plik `sprzedaz_z_wartoscia.csv` zawierający wszystkie
oryginalne kolumny plus dodatkową kolumnę `wartosc`.
Użyj `csv.DictWriter`.

---

## 💡 Wskazówki

- Wszystkie wartości liczbowe w CSV są stringami — pamiętaj o `int()` / `float()`
- Puste komórki to pusty string `""` — sprawdzaj `if row["kolumna"]:`
- Do grupowania użyj słownika: `slownik[klucz] = slownik.get(klucz, 0) + wartosc`
- Do sortowania listy słowników: `sorted(lista, key=lambda x: x["pole"])`


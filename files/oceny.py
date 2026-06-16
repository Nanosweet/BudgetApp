import csv

przedmioty = [
    "matematyka",
    "fizyka",
    "historia",
    "jezyk_angielski",
]

wyniki = []

with open("oceny_uczniow.csv", newline="", encoding="utf-8") as plik:
    reader = csv.DictReader(plik)

    for row in reader:
        suma = 0
        licznik = 0

        for p in przedmioty:
            if row[p] != "":
                suma += int(row[p])
                licznik += 1

        srednia = suma / licznik if licznik > 0 else 0

        wyniki.append((row["imie"], srednia))

# sortowanie od najlepszej średniej
wyniki.sort(key=lambda x: x[1], reverse=True)

# wypisanie
print("Ranking uczniów:\n")

for imie, srednia in wyniki:
    print(f"{imie} -> {srednia:.2f}")
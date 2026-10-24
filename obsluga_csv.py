import csv
from pathlib import Path
import random

def losuj_csv():
    modele = ["A", "B", "C"]
    m = random.choice(modele)
    w = random.randint(0, 1000)
    c = random.randint(0, 1000)
    
    return [['Model', 'Wynik', 'Czas'], [{m}, {w}, {c} + 's']]

def zapisz_csv(sciezka_do_katalogu):
    sciezka_do_pliku = Path(sciezka_do_katalogu) / "Dane.csv"

    if not sciezka_do_pliku.is_file():
        print ("Błąd- próba zapisu do nieistniejącego pliku.")
        return

    dane = losuj_csv()
    with open(sciezka_do_pliku, mode = "w", newline = "", encoding = "utf-8") as plik:
        pisarz = csv.writer(plik, delimiter = ";")
        pisarz.writerows(dane)

def odczytaj_csv(sciezka_do_katalogu):
    sciezka_do_pliku = Path(sciezka_do_katalogu) / "Dane.csv"

    if not sciezka_do_pliku.is_file():
        print ("Błąd- próba odczytu nieistniejącego pliku")
        return 0

    with open (sciezka_do_pliku, mode = "r", encoding = "utf-8") as plik:
        czytnik = csv.reader(plik, delimiter = ";")
        next(czytnik, None)
        wiersz = next(czytnik, None)

        if wiersz and len(wiersz) >= 3:
            model = wiersz[0].strip()
            czas = wiersz[2].strip()

            if model == "A":
                return int(czas.replace("s", ""))
        return 0
    
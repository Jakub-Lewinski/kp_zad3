
import json
from pathlib import Path
import random


def losuj_json():
    modele = ["A", "B", "C"]
    m = random.choice(modele)
    w = random.randint(0, 1000)
    c = random.randint(0, 1000)

    return {
        "Model": m,
        "Wynik": w,
        "Czas": str(c) + "s"
    }


def zapisz_json(sciezka_do_katalogu):
    sciezka_do_pliku = Path(sciezka_do_katalogu) / "Dane.json"

    if not sciezka_do_pliku.is_file():
        print("Błąd - próba zapisu do nieistniejącego pliku.")
        return

    dane = losuj_json()

    with open(sciezka_do_pliku, mode="w", encoding="utf-8") as plik:
        json.dump(dane, plik, indent=4)


def odczytaj_json(sciezka_do_katalogu):
    sciezka_do_pliku = Path(sciezka_do_katalogu) / "Dane.json"

    if not sciezka_do_pliku.is_file():
        print("Błąd - próba odczytu nieistniejącego pliku.")
        return 0

    with open(sciezka_do_pliku, mode="r", encoding="utf-8") as plik:
        dane = json.load(plik)

    if dane["Model"] == "A":
        return int(dane["Czas"].removesuffix("s"))

    return 0

import csv
import json
from datetime import datetime

from rich.console import Console
from rich.table import Table


def nacti_casy(nazev_souboru):
    zamestnanci = []

    with open(nazev_souboru, "r", encoding="utf-8") as f:
        data = csv.reader(f, delimiter=";")
        for row in data:
            zamestnanci.append(row)

    return zamestnanci


def vypis_json(data, nazev_souboru):
    try:
        with open(nazev_souboru, "w", encoding="utf-8", newline="") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"Data byla uložena do {nazev_souboru}")

    except OSError as error:
        print(f"Chyba při zápisu souboru: {error}")


def delka_smeny(zamestnanci):
    delky_smen = []

    for row in zamestnanci:
        prichod = datetime.strptime(row[2], "%Y-%m-%d %H:%M")
        odchod = datetime.strptime(row[3], "%Y-%m-%d %H:%M")
        delka = (odchod - prichod).total_seconds() / 3600
        delky_smen.append(delka)

    if not delky_smen:
        print("Nejsou k dispozici žádná data o směnách.")
        return

    nejkratsi = min(delky_smen)
    nejdelsi = max(delky_smen)

    print(f"Nejkratší směna: {nejkratsi:.2f} hodin")
    print(f"Nejdelší směna: {nejdelsi:.2f} hodin")


def vypis_zamestnance(zamestnanci):
    table = Table(title="Seznam zaměstnanců")
    table.add_column("Číslo čipu")
    table.add_column("Zaměstnanec")
    table.add_column("Příchod")
    table.add_column("Odchod")

    for row in zamestnanci:
        table.add_row(row[0], row[1], row[2], row[3])

    Console().print(table)


def menu():
    print("========================================")
    print("           ANALÝZA DOCHÁZKY")
    print("========================================")
    print("0 - konec")
    print("1 - zobrazit všechny zaměstnance")
    print("2 - ulož do json")
    print("3 - Jak dlouhá byla nejkratší a nejdelší směna")


def main():
    zamestnanci = nacti_casy("dochazka.csv")
    zamestnanci.pop(0)  # zahodi hlavicku CSV

    while True:
        menu()
        volba = input("\nVolba: ").strip()

        if volba == "0":
            break
        elif volba == "1":
            vypis_zamestnance(zamestnanci)
        elif volba == "2":
            vypis_json(zamestnanci, "vysledek.json")
        elif volba == "3":
            delka_smeny(zamestnanci)
        else:
            print("Neplatná volba, zkus to znovu.")


if __name__ == "__main__":
    main()

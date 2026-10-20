import csv
import json
import sys
import os
from datetime import datetime
from rich.table import Table


def nacti_casy(nazev_souboru):
    
    zamestnanci=[]

    with open(nazev_souboru, "r", encoding="utf-8") as f:
        data = csv.reader(f,delimiter=";")
        for row in data:
            zamestnanci.append(row)
        
    return zamestnanci


def vypis_json(data,nazev_souboru):
    try:
        with open(nazev_souboru, "w",encoding="utf-8", newline="") as f:
            json.dump(data,f,indent=4,ensure_ascii=False)
            
        print("Data byla ulozena do {nazev_souboru}")


    except OSError as error:
        print("Error")

def delka_smeny(zamestnanci):
    delky_smen = [float(row[2]) for row in zamestnanci]

    nejkratsi = min(delky_smen)
    nejdelsi = max(delky_smen)
    
    print(f"Nejkratší směna: {nejkratsi} hodin")
    print(f"Nejdelší směna: {nejdelsi} hodin")


def vypis_zamestnance(zamestnanci):
   table = Table(title="Seznam knih")
   table.add_column("Číslo čipu")
   table.add_column("Jméno")
   table.add_column("Příjmení")
    

def menu():
    print("========================================")
    print("           ANALÝZA DOCHÁZKY") 
    print("========================================")
    print("0 - konec") 
    print("1 - zobrazit vsechny zamestnance")    
    print("2 - uloz do json")
    print("3 - Jak dlouhá byla nejkratší a nejdelší směna")
    




def main():
    zamestnanci = nacti_casy("dochazka.csv")
    zamestnanci.pop(0)
    
    menu()
    vypis_json(zamestnanci,"vysledek.json")
    
    
    while True:
        menu()
        volba = input("\nVolba ").strip()
        if volba == "0":
            break
        elif volba == "1":
            vypis_zamestnance
        elif volba == "2":
            vypis_json
        


if __name__ == "__main__":
    main()
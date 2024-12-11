import pandas as pd

with open("gry.txt", "r") as file:
    dgry = file.read().split("\n")[1:-1]
with open("gracze.txt", "r") as file:
    dgracze = file.read().split("\n")[1:-1]
with open("oceny.txt", "r") as file:
    doceny = file.read().split("\n")[1:-1]

gry = {}
for gra in dgry:
    id_gry, nazwa, kat = gra.split("\t")
    gry[id_gry] = {"nazwa": nazwa, "kategoria": kat}

gracze = {}
for gracz in dgracze:
    id_gracza, imie, nazw, wiek = gracz.split("\t")
    gracze[id_gracza] = {"imie": imie, "nazwisko": nazw, "wiek": wiek}
    
licznik_gier = {}
imprezowe = {}
imprezowe_cnt = {}
for ocena in doceny:
    id_gry, id_gracza, stan, ocen = ocena.split("\t")
    
    nazwa = gry[id_gry]["nazwa"]
    kategoria = gry[id_gry]["kategoria"]
    if nazwa not in licznik_gier.keys():
        licznik_gier[nazwa] = 0 
    licznik_gier[nazwa] += 1
    
    if kategoria == "imprezowa":
        if nazwa not in imprezowe.keys():
            imprezowe[nazwa] = 0
            imprezowe_cnt[nazwa] = 0
        imprezowe[nazwa] += int(ocen)
        imprezowe_cnt[nazwa] += 1

ans = [0, ""] 
for nazwa, ilosc in licznik_gier.items():
    if ilosc > ans[0]:
        ans = [ilosc, nazwa]
print(f"Zadanie 7.1: {ans[1]}")  

for suma, licznik in zip(imprezowe.values(), imprezowe_cnt.values()):
    suma /= licznik
print(f"Zadanie 7.2:")
df = pd.DataFrame.from_dict(imprezowe, orient='index')
df.columns = ["nazwa", "srednia"]
print(df)
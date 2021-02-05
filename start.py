#wczytanie pliku z adresami
import csv

seperator=';'
plik = "csv/lud_utf8.csv"

f = open(plik , 'r', encoding="utf-8", newline='')
reader = csv.reader(f, delimiter=seperator, quotechar='|')
slownik = {}
adres = ''
czlowiek = 0
for row in reader:
    if row[2].replace('"','')+'--'+row[3].replace('"','') == adres:
        
        slownik[adres]={row[4]:int(row[5])}
    else:
        adres = row[2].replace('"','')+'--'+row[3].replace('"','')
        slownik[adres]={}
        slownik[adres].add(row[4],int(row[5]))
    #slownik[slownik_z_kodami_teryt[row[kol_ulica].lower().strip()]+"--"+row[kol_numer].strip()]=float(row[kol_wartosc])
    # print(adres)
    # return slownik
print(slownik)





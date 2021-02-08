#wczytanie pliku z adresami
import csv

seperator=';'
plik = "csv/lud_utf8.csv"

f = open(plik , 'r', encoding="utf-8", newline='')
reader = csv.reader(f, delimiter=seperator, quotechar='|')
slownik_sum = {}
slownik = {}
adres = ''
czlowiek = 0
for row in reader:
    if row[2].replace('"','')+'--'+row[3].replace('"','') == adres:
        
        slownik[adres][row[4].replace('"','')]=int(row[5])
    else:
        adres = row[2].replace('"','')+'--'+row[3].replace('"','')
        slownik[adres]={}
        slownik[adres][row[4].replace('"','')] = int(row[5])

for key, item in slownik.items():
    slownik[key]['suma_M-K'] = item.get("Ż", 0) + item.get("M", 0) 
for adres in slownik:
    slownik_sum[adres] = slownik[adres]['suma_M-K']





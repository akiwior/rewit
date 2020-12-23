import csv
plik = 'e:ulice_kod.csv'
f = open(plik , 'r', encoding="utf-8")
reader = csv.reader(f)
slownik = {}
for row in reader:
    slownik[row[1]] = row[0]


    

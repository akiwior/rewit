# import json
import csv
# filename = "E:\\rewit\\pkt_adresowe.json" 
# slownik = {}
# with open(filename, encoding = 'utf-8') as f:
#     slownik = json.load(f)
# print(slownik)
# from slownik_kody import *
# adresy = load_json_dict("E:\\rewit\\pkt_adresowe.geojson")
# print(adresy)
plik = r"E:\rewit\ULIC_SIMC(0977278)_TERC(2263011)_31-12-2020.csv"
f = open(plik , 'r', encoding="utf-8", newline='')
reader = csv.reader(f, delimiter=';', quotechar='|')
slownik = {}
for row in reader:
    print(row)
    slownik[row[7]] = row[5]
# return slownik
print(slownik)
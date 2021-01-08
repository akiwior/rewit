import json
import csv
from funkcje_kody import *
# filename = "pkt_adresowe.geojson" 
# slownik1 = {}
# with open(filename, encoding = 'utf-8') as f:
#     slownik1 = json.load(f)
# print(slownik1)

# adresy = load_json_dict("E:\\rewit\\pkt_adresowe.geojson")
# slownik_feat = adresy['features']
# print(adresy)
plik = r"ULIC_SIMC(0977278)_TERC(2263011)_31-12-2020.csv"
f = open(plik , 'r', encoding="utf-8", newline='')
reader = csv.reader(f, delimiter=';', quotechar='|')
slownik = {}
for row in reader:
    if row[8].isalpha():
    # print(row)
        slownik[row[7]+' '+ row[8]] = row[5]
    else:
        pass
# return slownik
print(len(slownik))
# slownik_UPDATE = {'1':'11', '2': '22'}
# convert_to_json(slownik_UPDATE, './slowniki/dodatkowy.json')


# for rekord in slownik_feat:
    # rekord_num = rekord['properties']
    # ulica = (rekord_num['ulica'])
    # print(f"{ulica} {slownik[ulica]}")
    # rekord_num['teryt'] = slownik[ulica]
    # # print(rekord_num)
    # # print(rekord['properties'])
    # rekord_num['nowsze'] = kod
    # imie = rekord_num['IMIE']
    # # print(imie)
    # insert = slownik3[imie]
    # print(f" to jest watrość wstawiona do pliku json {insert}")
    # rekord_num['nowsze'] = insert 
    # kod = kod + 1
    # print(rekord_num)
# for key, value in slownik.items():
#     print(key,'->', value)
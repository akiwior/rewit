import csv
from funkcje_kody import *

teryt = teryt_load('csv/ulice_kod_full_change.csv', 1, 0, ',')
adresy = load_json_dict('input_file_dir/pkt_adresowe.geojson')
dane = meldunki_do_slownik('csv/lud_utf8.csv',';')
adres_teryt = add_teryt_to_adresy_geojson(adresy, teryt)
convert_to_json(adres_teryt, 'nowe_adresy/punty_adresowe_teryty.geojson')

with open('csv/ludziki.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file) 
    for klucz, value in dane.items():
        writer.writerow([klucz, value])
        print(f"dodano {klucz}, {value}")

def wyrownanie(string):
    while len(string)<5:
        string = '0'+string
    return string
a = '1234'
a = wyrownanie(a)
print(a)

# lista= ['ad', 'a', 'b', 'cccc', 'ddddddd', '12345', '123']
# for string in lista:
#     wyrownanie(string)
# # for adres in dane:
# #     wyrownanie(adres)      

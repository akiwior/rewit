from funkcje_kody import *

slownik_teryt = load_json_dict('slowniki/pelny_slownik.json')

plik_csv = 'input_file_dir/wejscie.csv'

dane_csv = ulice_dane_load_csv(plik_csv, 0, 1, 2,',', slownik_teryt )

punkty_adresy = load_json_dict('output_file_dir/nowy.json')

print(dane_csv)
lista_adresow = []
for adres in punkty_adresy['features']:
    lista_adresow.append(adres['properties']['teryt'])
print(dane_csv)
# print(lista_adresow)
for punkt in punkty_adresy['features']:
    # print(punkt['properties']['teryt'])
    punkt['properties']['dane'] = dane_csv.get(punkt['properties']['teryt'])
    # if punkt['properties']['teryt'] == dane_csv[punkt['properties']['teryt']]:
    #     punkt['properties']['dane'] = dane_csv[punkt['properties']['teryt']]
    # else:
    #     punkt['properties']['dane'] = None
    # print(punkty_adresy)
convert_to_json(punkty_adresy, 'output_file_dir/nowy_dane.json')



#     else:
#         adres['properties']['dane']= None





from json import *

# punkt = {"wartosci": {"wartosc1":"1", "wartosc2": "2"},"punkt": 22}
# listaA1 = ['11', '22', '33', '44', '55']
# listaA2 = ['333', 22 ]
# listy = [listaA1, listaA2]
# slownik ={'pierwszy':'tekst', 'drugi': 'tekst2'}
# for lista in listy:
#     if punkt["punkt"] in lista:
#         print('jest')
#         punkt["wartosci"]["wartosc3"]= "3"
# print(punkt)
file = "siatka_slupsk_1000.geojson"
with open(file) as json_file:
    siatka = load(json_file)
print(siatka)
for obiekt in siatka['features']:
    obiekt['properties']['punkty']=f" komórka {obiekt['properties']['id']+2}"
with open(file, 'w', encoding='utf-8') as json_out:
    dump(siatka,json_out, ensure_ascii=False)
print(siatka)
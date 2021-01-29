from json import *
# punkt = {'pole1': {'wartosc1':'pierwsza', 'wartosc2':'druga'}, 'wsp': [ 6432067.891743338666856, 6040458.540591625496745 ] } 

# polig1 = [[6440990.61, 6033373.94], [6441990.61, 6033373.94], [6441990.61, 6032373.94], [6440990.61, 6032373.94], [6440990.61, 6033373.94]]
# pk = punkt['wsp']
# print(pk[1] > polig1[0][1])
# # print(pk)

# if pk[0] > polig1[0][0] and pk[0] < polig1[2][0] and pk[1] > polig1[0][1] and pk[1] < polig1[2][1]:
#     print('jest')
    
# else:
#     print('nie jest')
# print(punkt)
# for pk in pk:
#     if pk[0] > polig1[0][0] and pk[0] < polig1[2][0] and pk[1] > polig1[0][1] and pk[1] < polig1[2][1]:
#         print('jest')
#     else:
#         print('nie jest')


# A1 = {'wartosc':[1, 2, 3, 100]}
# print(sum(A1['wartosc']))

lista = []
#lista zawierajaca wsporzedne punktu
tabelka = {}
#slownik z {id: [wspolrzedne pola]}

file_siatka = "siatka_slupsk_1000.geojson"
with open(file_siatka, encoding='utf-8') as json_file:
    siatka = load(json_file)

# print(siatka)
#wgranie punktów adresowych do zmiennej {adresy} - slownik 
file_adres = "punkty_adres.geojson"
with open(file_adres, encoding='utf-8') as json_file:
    adresy = load(json_file)
for adres in adresy["features"]:
    pk = adres["geometry"]["coordinates"]
    ms_link = adres['properties']['mslink']
    # print(f"sprawdzam dla {ms_link} wspolrzedne to {pk}")
    for grid_cell in siatka['features']:
        polig1 = grid_cell['geometry']['coordinates'][0]
        # print(pk)
        # print(f"sprawdzam dla {ms_link} wspolrzedne to {pk} porowniuje je z {grid_cell['properties']['id']}")
        # print(f"x1 { polig1[0][0]} and x3 {polig1[2][0]} and y1 {polig1[0][1]} and y3 {polig1[2][1]}")
        
        if pk[0] > polig1[0][0] and pk[0] < polig1[2][0] and pk[1] < polig1[0][1] and pk[1] > polig1[2][1]:
            # print(f"{adres['properties']['mslink']} zawarty jest w {grid_cell['properties']['id']}")
            adres['properties']['grid_id']= grid_cell['properties']['id']
        else:
            # print('nie zawiera się')
            continue
        # print(grid_cell['geometry']['coordinates'])
 
#     adres["properties"]["komorka_id"] = adres["geometry"]["coordinates"]
# print(lista[:10])
# # for adres in adresy["features"][:10]:
# #     print(adres)
# #wgranie siatki do zmiennej {siatka}-slownik 
# file_siatka = "siatka_slupsk_1000.geojson"
# with open(file_siatka, encoding='utf-8') as json_file:
#     siatka = load(json_file)
# for cell in siatka["features"]:
#     tabelka[cell['properties']['id']] = cell['geometry']['coordinates'][0]
# for id, lista in tabelka.items():
#     print(f"{id}: {lista}")
file_out = "punkty_adres_cell.geojson"
with open(file_out, 'w', encoding='utf-8') as json_out:
    dump(adresy, json_out, ensure_ascii=False)
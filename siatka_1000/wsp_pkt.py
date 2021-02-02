from json import *


lista = []
#lista zawierajaca wsporzedne punktu
tabelka = {}
#slownik z {id: [wspolrzedne pola]}

file_siatka = "E:\\slownik-git\\rewit\siatka_1000\\siatka_slupsk_1000.geojson"
with open(file_siatka, encoding='utf-8') as json_file:
    siatka = load(json_file)

# print(siatka)
#wgranie punktów adresowych do zmiennej {adresy} - slownik 
file_adres = "E:\\slownik-git\\rewit\\siatka_1000\\dzialki.geojson"
with open(file_adres, encoding='utf-8') as json_file:
    adresy = load(json_file)
for adres in adresy["features"][:10]:
    pk = adres["geometry"]["coordinates"][0][0]
    print(pk)
    ms_link = adres['properties']['mslink']
    # print(f"sprawdzam dla {ms_link} wspolrzedne to {pk}")
    for grid_cell in siatka['features']:
        polig1 = grid_cell['geometry']['coordinates'][0]
        #sprawdzenie przynaleznosci kazdego punktu do siatki grid pobierane sa wspolzedne pierwszego naroznika
        #oraz trzeciego i porownywane do wspołrzędnuch x,y każdego punktu.
        if pk[0] > polig1[0][0] and pk[0] < polig1[2][0] and pk[1] < polig1[0][1] and pk[1] > polig1[2][1]:
            #  dodaje do karzdego punktu przynaleznosc do siatki ppoligonu grid
            adres['properties']['grid_id']= grid_cell['properties']['id']
            grid_cell['properties']['lista_pkt']= [ms_link]
        else:
            continue
print(siatka)
file_out = "punkty_adres_cell_III.geojson"
with open(file_out, 'w', encoding='utf-8') as json_out:
    dump(adresy, json_out, ensure_ascii=False)



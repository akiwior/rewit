from funkcje_kody import *

adresy = load_json_dict('E:\\slownik-git\\rewit\\input_file_dir\\pkt_adresowe.geojson')
grid = load_json_dict('E:/slownik-git/rewit/siatka_1000/siatka_slupsk_1000.geojson')
adresy_grid = dod_do_adres_grid_id(adresy=adresy, siatka=grid)

for kom in grid['features']:
    kom['properties']['sum_dana'] = [1,2]
    kom['properties']['sum_dana'].append(kom['properties']['id']+sum(kom['properties']['sum_dana']))

print(grid)
# for grid_cell in siatka['features']:
#         polig1 = grid_cell['geometry']['coordinates'][0]
#         #sprawdzenie przynaleznosci kazdego punktu do siatki grid pobierane sa wspolzedne pierwszego naroznika
#         #oraz trzeciego i porownywane do wspołrzędnuch x,y każdego punktu.
#         if pk[0] > polig1[0][0] and pk[0] < polig1[2][0] and pk[1] < polig1[0][1] and pk[1] > polig1[2][1]:
#             #  dodaje do karzdego punktu przynaleznosc do siatki ppoligonu grid
#             adres['properties']['grid_id']= grid_cell['properties']['id']
#         else:
#             continue

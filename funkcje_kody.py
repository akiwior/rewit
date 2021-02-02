import csv
import json
def teryt_load(plik, kol_ulic, kol_teryt, seperator):
    #function import data from csv file to dictionary plik csv z gus
    f = open(plik , 'r', encoding="utf-8", newline='')
    reader = csv.reader(f, delimiter=seperator, quotechar='|')
    slownik = {}
    for row in reader:
        slownik[row[kol_ulic].lower()] = row[kol_teryt]
    return slownik

def ulice_dane_load_csv(plik, kol_ulica, kol_numer, kol_wartosc, seperator, slownik_z_kodami_teryt):
    #funkcja importujaca z pliku csv do slownika python, 
    # zamieniajaca nazwe ulicy i adres na teryt-numer: wartosc
    f = open(plik , 'r', encoding="utf-8", newline='')
    reader = csv.reader(f, delimiter=seperator, quotechar='|')
    slownik = {}
    for row in reader:
        slownik[slownik_z_kodami_teryt[row[kol_ulica].lower().strip()]+"--"+row[kol_numer].strip()]=row[kol_wartosc]
    return slownik

def add_data_to_ulice(punkty_adresy, slown_dane, dana=None):
    #dodaje do slownika z punktami adresowymi , pole zawierajace dane ze slownia
    #slownik powinien miec format ulica:dana
    for punkt in punkty_adresy['features']:
    # print(punkt['properties']['teryt'])
        punkt['properties']['dane'] = slown_dane.get(punkt['properties']['teryt'], dana)
    return punkty_adresy

def convert_to_json(in_slownik, out_json):
    #function create a dictionary in jsonfile wrom dict in python
    filename = out_json
    slownik = in_slownik
    with open(filename, 'w', encoding="utf-8",) as f:
        json.dump(slownik, f, ensure_ascii=False)
        #ensure_ascii false jest zeby mie wgrywal kodawania znakow z windowsa

def load_json_dict(in_json_dic):
    #function load json dict jsonfile
    filename = in_json_dic 
    slownik = {}
    with open(filename, encoding="utf-8") as f:
        slownik = json.load(f)
    return slownik

def teryt_load_pelne_nazwy(plik, kol_ulic, kol_ulicy_dodatk, kol_teryt, seperator):
    #function import data from csv file to dictionary plik csv comes from gus - GLOWNY 
    # URZAD STATYSTYCZNY 
    f = open(plik , 'r', encoding="utf-8", newline='')
    reader = csv.reader(f, delimiter=seperator, quotechar='|')
    slownik = {}
    for row in reader:
        if row[kol_ulicy_dodatk].isalpha():
    # print(row)
            slownik[row[kol_ulic].lower() + ' ' + row[kol_ulicy_dodatk].lower()] = row[kol_teryt]
            slownik[row[kol_ulicy_dodatk].lower() + ' ' + row[kol_ulic].lower()] = row[kol_teryt]
        else:
            pass
    return slownik

def dod_do_adres_grid_id(adresy, siatka):
    #funkcja dodajaca do kazdego adresu id poligonu grid
    for adres in adresy["features"]:
        pk = adres["geometry"]["coordinates"]
        ms_link = adres['properties']['mslink']
    # print(f"sprawdzam dla {ms_link} wspolrzedne to {pk}")
        for grid_cell in siatka['features']:
            polig1 = grid_cell['geometry']['coordinates'][0]
        #sprawdzenie przynaleznosci kazdego punktu do siatki grid pobierane sa wspolzedne pierwszego naroznika
        #oraz trzeciego i porownywane do wspołrzędnuch x,y każdego punktu.
            if pk[0] > polig1[0][0] and pk[0] < polig1[2][0] and pk[1] < polig1[0][1] and pk[1] > polig1[2][1]:
            #  dodaje do karzdego punktu przynaleznosc do siatki ppoligonu grid
                adres['properties']['grid_id']= grid_cell['properties']['id']
            else:
                continue
    return adresy





    

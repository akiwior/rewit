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

def teryt_load_pelne_nazwy(plik, kol_ulic, kol_ulicy_dodatk,  kol_teryt, seperator):
    #function import data from csv file to dictionary plik csv z gus
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





    

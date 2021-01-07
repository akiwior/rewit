import csv
import json
def teryt_load(plik):
    #function import data from csv file to dictionary
    f = open(plik , 'r', encoding="utf-8")
    reader = csv.reader(f)
    slownik = {}
    for row in reader:
        slownik[row[1]] = row[0]
    return slownik
def convert_to_json(in_slownik, out_json):
    #function create a dictionary in jsonfile wrom dict in python
    filename = out_json
    slownik = in_slownik
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(slownik, f)
def load_json_dict(in_json_dic):
    #function load json dict jsonfile
    filename = in_json_dic 
    slownik = {}
    with open(filename, encoding="utf-8") as f:
        slownik = json.load(f)
    return slownik





    

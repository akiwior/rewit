def teryt_load(plik):
    #function import data from csv file to dictionary
    import csv
    f = open(plik , 'r', encoding="utf-8")
    reader = csv.reader(f)
    slownik = {}
    for row in reader:
        slownik[row[1]] = row[0]
    return slownik
def convert_to_json(in_slownik, out_json):
    #function create a dictionary in jsonfile
    import json
    filename = 'out_json.json'
    slownik = in_slownik
    with open(filename, 'w') as f:
        json.dump(slownik, f)






    

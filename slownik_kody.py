def teryt_load(plik):
    #function import data from csv file to dictionary
    import csv
    f = open(plik , 'r', encoding="utf-8")
    reader = csv.reader(f)
    slownik = {}
    for row in reader:
        slownik[row[1]] = row[0]
    return slownik





    

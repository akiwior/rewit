import csv
 
plik_o = 'csv/ulice_kod_full.csv'
plik_w = 'csv/ulice_kod_full_change.csv'
seperator = ','

fz = open(plik_w , 'w', encoding="utf-8", newline='')
writer = csv.writer(fz, delimiter=seperator, quotechar='|')

f = open(plik_o , 'r', encoding="utf-8", newline='')
reader = csv.reader(f, delimiter=seperator, quotechar='|')
for row in reader:
    while len(row[0])<5:
        row[0]='0'+row[0]
    else:
        print(row[0])
        writer.writerow(row)

f.close()
fz.close()
    


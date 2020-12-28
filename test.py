import slownik_kody as sl
slownik = sl.teryt_load('slownik.csv')
sl.convert_to_json(slownik, 'new.json')
slownik2 = sl.load_json_dict('new.json')
print(slownik2)


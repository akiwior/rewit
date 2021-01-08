from funkcje_kody import * 
teryt = teryt_load('./csv/ULIC_SIMC(0977278)_TERC(2263011)_31-12-2020.csv', 7, 5,';')
teryt_pel = teryt_load_pelne_nazwy('./csv/ULIC_SIMC(0977278)_TERC(2263011)_31-12-2020.csv', 7, 8, 5,';')

# for key, value in teryt.items():
#     print(key, '->', value)
print(len(teryt))
print(len(teryt_pel))
convert_to_json(teryt, './slowniki/gus_teryt.json')
convert_to_json(teryt_pel, './slowniki/gus_teryt_pelne_nazwy.json')
pelny = {**teryt, **teryt_pel}
convert_to_json(pelny, './slowniki/pelny_slownik.json')
print(len(pelny))
# for key, value in pelny.items():
#     print(key,'>>>>>', value)
print(pelny['stanisława żółkiewskiego'])
print(pelny['żółkiewskiego stanisława'])
print(pelny['żółkiewskiego'])



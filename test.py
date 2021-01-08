import funkcje_kody as sl
slownik = sl.teryt_load('slownik.csv',0 ,1,',')
sl.convert_to_json(slownik, 'new.json')
# slownik2 = sl.load_json_dict('probny_lot.geojson')
# slownik3 = sl.load_json_dict('new.json')
# slownik_feat = slownik2['features']   
# # print(slownik_feat[0])
# kod = 1
# for rekord in slownik_feat:
#     rekord_num = rekord['properties']
#     # print(rekord_num)
#     # print(rekord['properties'])
#     rekord_num['nowsze'] = kod
#     imie = rekord_num['IMIE']
#     # print(imie)
#     insert = slownik3[imie]
#     print(f" to jest watrość wstawiona do pliku json {insert}")
#     rekord_num['nowsze'] = insert 
#     kod = kod + 1
#     print(rekord_num)
#     # for atr in rekord_num:
#     #     print(atr)
#     #     atr['nowsze'] = kod
#     # kod = kod + 1        
#     # print(rekord['properties'])
# print(slownik_feat)    
# print(slownik2)
# sl.convert_to_json(slownik2, 'after_change.geojson')
print(slownik)
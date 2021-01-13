from funkcje_kody import *

slownik = load_json_dict('./slowniki/pelny_slownik.json')
adresy = load_json_dict('./input_file_dir/pkt_adresowe.geojson')

# print(adresy['features'])
# for key in adresy:
#     print(key)
# feat = adresy['features']
# print(feat)
for pkt in adresy['features']:
    kod = slownik.get(pkt['properties']['ulica'].lower())
    pkt['properties']['teryt'] = kod 
    print(pkt['properties']['ulica'], '>>', kod)
    # print(pkt['properties'])
# print(adresy['features'][:100])
convert_to_json(adresy, './input_file_dir/nowy.json')
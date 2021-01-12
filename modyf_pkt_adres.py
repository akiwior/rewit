from funkcje_kody import *

adresy = load_json_dict('./input_file_dir/pkt_adresowe.geojson')
print(adresy['type'])
# for key in adresy:
#     print(key)
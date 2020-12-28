import slownik_kody
import json
slownik = slownik_kody.teryt_load("E:/slownik-git/rewit/slownik.csv")
print(slownik)
# filename = 'slow.json'
# with open(filename, 'w') as f:
#     json.dump(slownik, f)
slownik_kody.convert_to_json(slownik, 'nowy222.json')

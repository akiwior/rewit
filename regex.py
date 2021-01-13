import re
import funkcje_kody as fk


tabelka = fk.load_json_dict('C:\\Users\\Tata Swinka\\Desktop\\python_ksiazka\\regex\\pelny_slownik.json')
# jednostka = {"01": ["11-1", "12-2", "13-3"], "02": ["02-1", "02-2", "02-3"]}
# dane = {"3-go maja": 20, "12-2": 10}
ulica1 = input("podaj ulicę: ")
ulica2 = "aleja 3-go maja"
lista = ''
# if re.search(ulica1, ulica2):
#     print(f"{ulica1} została odnaleziona w {ulica2}")
# else:
#     print(f"{ulica1} nie została odnaleziona w {ulica2}")

for litera in ulica1[:5]:
    stri = f"[{litera}]"
    lista = lista + stri
# print(lista)
klucz = ''
mesage =""

for key in tabelka:
# print(key)
    if re.search(lista, key) and mesage != 'tak':
        print(f"{ulica1} wpisana ulica pasuje do {key}\n kod ulicy {key} to {tabelka.get(key)} ")
        klucz = key
        mesage = input("napicz 'tak' jeśli się zgadzasz (- jednocześnie zakończysz)?: ")
    else:
        # print('nie wiem o co chodi wpisz co najmniej pięć liter')
        continue

wybrana_ulica = {klucz: tabelka[klucz]}
print(wybrana_ulica)
    


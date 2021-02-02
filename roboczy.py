a = {1: None, 2: 2, 3: None}
print(a)
b =[value for key, value in a.items()]
print(b)
for key, value in a.items():
    if value == None:
        a[key] = 0
    else:
        continue
print(a)
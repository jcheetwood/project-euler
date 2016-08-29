a = []
b = 0
for i in range(100,999):
    for l in range(100, 999):
        a.append(i * l)
for x in a:
    if str(x) == str(x)[::-1]:
        if x > b:
            b = x
        else:
            continue
    else:
        continue
print(b)
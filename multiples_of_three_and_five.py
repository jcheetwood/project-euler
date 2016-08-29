a = [*range(1,1000)]
b = 0
for i in a:
    if i % 3 == 0 or i % 5 == 0:
        b += i
        print(i)
print(b)
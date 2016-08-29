a, b = 1, 1
total = 0

while a <= 4000000:
    if a % 2 == 0:
        total += a
        print(a)
    a, b = b, a + b

print(total)


def fibonacci(n):
    a = 1
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

a = fibonacci(40000000)
print(a)
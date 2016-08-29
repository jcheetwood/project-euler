num_range = [*range(11, 21)]

def smallest():
    for n in range(20, 999999999, 20):
        if all(n % num == 0 for num in num_range):
            return n
    return None

b = smallest()
print(b)
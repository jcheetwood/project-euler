"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

num_range = [*range(11, 21)]

def smallest():
    for n in range(20, 999999999, 20):
        if all(n % num == 0 for num in num_range):
            return n
    return None

b = smallest()
print(b)
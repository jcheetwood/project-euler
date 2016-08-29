"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
n = 600851475143
i = 2
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i
print(n)
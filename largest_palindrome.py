"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
 is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
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
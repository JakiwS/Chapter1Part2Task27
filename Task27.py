from random import random
a = []
b = []
for i in range(20):
    n = int(random() * 11) - 5
    print(n, end=', ')
    if n > 0:
        a.append(n)
    elif n < 0 :
        b.append(n)
print()
print(a)
print(b)

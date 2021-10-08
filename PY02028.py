# sắp xếp nguyên tố
import math

def tc(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

n = int(input())
a = [int(i) for i in input().split()]
b = []

for i in a:
    if tc(i):
        b.append(i)
if len(b) == 0:
    for i in a:
        print(i, end = ' ')
else:
    b.sort()
    k = 0
    for i in a:
        if tc(i):
            print(b[k], end = ' ')
            k += 1
        else:
            print(i, end = ' ')
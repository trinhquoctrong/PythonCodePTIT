# PHÂN CHIA NGUYÊN TỐ

import math

def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

n = int(input())
A = [int(x) for x in input().split()]
B = []
for x in A:
    if x not in B:
        B.append(x)
s = sum(B)
index = 'NOT FOUND'
s1 = 0
for i in range(len(B)):
    s1 += B[i]
    if nt(s1) and nt(s-s1):
        index = i
        break
print(index)
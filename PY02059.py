# SỐ NGUYÊN TỐ TRONG MA TRẬN

import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
A = []
val = -1
for i in range(n):
    B = [int(x) for x in input().split()]
    A.append(B)
    for x in B:
        if prime(x) and val < x:
            val = x
res = []  
for i in range(n):
    for j in range(m):
        if A[i][j] == val:
            res.append([i, j])

if len(res) == 0:
    print('NOT FOUND')
else:
    print(val)
    for i in res:
        print('Vi tri [%d][%d]' % (i[0], i[1]))
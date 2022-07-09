# BÀI TOÁN TỔ HỢP

import itertools

n, k = map(int, input().split())
s = [int(x) for x in input().split()]
A = []
for i in s:
    if i not in A:
        A.append(i)
A.sort()

res = list(itertools.combinations(A, k))

for i in res:
    print(*i, end = '\n')
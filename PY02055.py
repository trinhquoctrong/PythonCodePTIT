# số nguyên tố lớn nhất trong ma trận

import math

def nto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(int(i) for i in input().split()))

b = []
max = 0
for i in range(n):
    for j in range(m):
        if max < a[i][j] and nto(a[i][j]):
            max = a[i][j]
            b.clear()
            b.append('[' + str(i) + '][' + str(j) + ']')
        elif max == a[i][j]:
            b.append('[' + str(i) + '][' + str(j) + ']')

if max:
    print(max)
    for i in b:
        print('Vi tri ' + i)
else:
    print('NOT FOUND')
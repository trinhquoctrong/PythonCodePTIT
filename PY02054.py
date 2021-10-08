# biến đổi về ma trận vuông

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(int(i) for i in input().split()))
if n > m:
    k = n - m
    for i in range(2*k-2, -1, -2):
        del a[i]
elif n < m:
    k = m - n
    for i in range(n):
        for j in range(2*k-1, 0, -2):
            del a[i][j]
    
x = min(m, n)
for i in range(x):
    for j in range(x):
        print(a[i][j], end = ' ')
    print()
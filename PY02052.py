# tính cân đối của ma trận

n = int(input())
a = []
for t in range(n):
    a.append([int(i) for i in input().split()])
k = int(input())
s = 0
for i in range(n):
    for j in range(n):
        if i < j:
            s += a[i][j]
        elif i > j:
            s -= a[i][j]
s = abs(s)
if s > k:
    print('NO')
else:
    print('YES')
print(s)
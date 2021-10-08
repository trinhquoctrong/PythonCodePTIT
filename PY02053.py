# tính cân đối của ma trận - 2

n = int(input())
a = []
for i in range(n):
    a.append(list(int(i) for i in input().split()))
k = int(input())
s = 0
for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            s += a[i][j]
        elif i + j >= n:
            s -= a[i][j]
s = abs(s)
if s > k:
    print('NO')
else:
    print('YES')
print(s)
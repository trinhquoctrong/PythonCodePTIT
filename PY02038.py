# đếm cặp đồng xu

def tohop(n):
    if n < 2:
        return 0
    else:
        return n * (n-1) // 2

n = int(input())
a = []
for i in range(n):
    s = input()
    tmp = []
    for j in s:
        tmp.append(j)
    a.append(tmp)

x = 0

for i in range(n):
    dem = 0
    for j in range(n):
        if a[i][j] == 'C':
            dem += 1
    x += tohop(dem)

for j in range(n):
    dem = 0
    for i in range(n):
        if a[i][j] == 'C':
            dem += 1
    x += tohop(dem)
print(x)
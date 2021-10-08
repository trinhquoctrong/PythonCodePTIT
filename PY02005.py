# cặp nghịch thế

n = int(input())
a = input().split(' ')
x = 0

for u in range(0, n-1):
    for v in range(u+1, n):
        if int(a[u]) > int(a[v]):
            x += 1

print(x)
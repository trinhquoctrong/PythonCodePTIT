# dãy số nhị phân

n = int(input())
a = [int(i) for i in input().split()]
d = 0
for i in range(n-1):
    if a[i] != a[i+1]:
        d += 1
print(d)
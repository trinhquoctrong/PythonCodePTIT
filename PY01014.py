# chia hết cho k

a = [int(i) for i in input().split()]
d = -1
x = []
k = a[1] - a[0] % a[1]
i = 0
while a[0] + (k + a[1]*i) <= a[2]:
    d = 1
    print(k+a[1]*i, end = ' ')
    i += 1
if d == -1:
    print(d)

# sắp xếp chắn lẻ

n = int(input())
a = []
while len(a) < n:
    a = a + [int(i) for i in input().split()]
a = a[0:n]
b = [0] * n
chan = []
le = []
for i in range(n):
    if a[i] % 2 == 0:
        chan.append(a[i])
    else:
        le.append(a[i])
        b[i] = 1
chan.sort()
le.sort(reverse = True)
i = 0
j = 0
for x in b:
    if x == 0:
        print(chan[i], end = ' ')
        i += 1
    else:
        print(le[j], end = ' ')
        j += 1
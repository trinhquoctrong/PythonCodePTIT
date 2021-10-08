# số may mắn trong ma trận

n, m = map(int, input().split())
a = []
Min = 0
Max = 0
for x in range(n):
    s = [int(i) for i in input().split()]
    a.append(s)
    if x == 0:
        Min = min(s)
        Max = max(s)
    else:
        if Min > min(s):
            Min = min(s)
        if Max < max(s):
            Max = max(s)

k = Max - Min
b = []
for i in range(n):
    for j in range(m):
        if a[i][j] == k:
            b.append('[' + str(i) + '][' + str(j) + ']')
if len(b):
    print(k)
    for i in b:
        print('Vi tri ' + i)
else:
    print('NOT FOUND')
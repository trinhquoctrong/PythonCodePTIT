# trúng thưởng

t = int(input())
for o in range(t):
    n = int(input())
    max = val = 0
    a = []
    b = {}
    for u in range(n):
        a.append(int(input()))
    a.sort()
    for i in a:
        if i not in b:
            b[i] = 0
        b[i] += 1
    for i in b:
        if max < b[i]:
            max = b[i]
            val = i
    print(val)
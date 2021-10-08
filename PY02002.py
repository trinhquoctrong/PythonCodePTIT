# liệt số fibonacci

F = [None] * 93
F[0] = 0
F[1] = F[2] = 1
for i in range(2, 93):
    F[i] = F[i-1] + F[i-2]

t = int(input())
for o in range(t):
    a = [int(x) for x in input().split()]
    for i in range(a[0], a[1]+1):
        print(F[i], end = ' ')
    print("")
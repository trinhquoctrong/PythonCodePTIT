# SẮP XẾP DÃY SỐ

for test in range(int(input())):
    n, m = map(int, input().split())
    A = [int(x) for x in input().split()]
    val = max(A)
    idx = A.index(val)
    A.insert(idx, m)
    am = []
    duong = []
    for i in A:
        if i < 0:
            am.append(i)
        else:
            duong.append(i)
    X = am + duong
    print(*X, sep = ' ')
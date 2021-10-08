# ước số của giai thừa

for t in range(int(input())):
    n, p = map(int, input().split())
    x = 0
    for i in range(p, n+1, p):
        while i % p == 0:
            i //= p
            x += 1
    print(x)

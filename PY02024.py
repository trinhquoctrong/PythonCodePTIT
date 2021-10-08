# sắp xếp theo tích chữ số

def mul(n):
    m = 1
    while n > 0:
        m *= n % 10
        n = int(n/10)
    return m

t = int(input())
for o in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    b = {}
    for i in a:
        if i not in b:
            b[i] = 0
        b[i] = mul(i)

    c = sorted(b.items(), key = lambda x : x[1])
    for i in c:
        print(i[0], end = ' ')
    print()

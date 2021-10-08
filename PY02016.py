# xuất hiện nhiều lần nhất

t = int(input())

while t > 0:
    n = int(input())
    a = [ int(x) for x in input().split()]
    b = {}
    max = val = int(0)
    for i in a:
        if i not in b:
            b[i] = 0
        b[i] += 1

    for i in b:
        if b[i] > max:
            max = b[i]
            val = i
    if max > n/2:
        print(val)
    else:
        print("NO")
    t -= 1
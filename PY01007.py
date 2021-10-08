# lãi suất ngân hàng

t = int(input())
for o in range(t):
    a = [float(i) for i in input().split()]
    n = a[0]
    x = a[1]
    m = a[2]
    i = 1
    while True:
        s = n * ((1+x/100)**i)
        if s >= m:
            print(i)
            break
        else:
            i += 1


# ĐỔI CƠ SỐ

p = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for test in range(int(input())):
    n, k = map(int, input().split())
    s = p[0:k]
    res = ''
    while n != 0:
        res = p[n%k] + res
        n //= k
        
    print(res)
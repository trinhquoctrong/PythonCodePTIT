# đổi cơ số

p = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for t in range(int(input())):
    n, b = map(int, input().split())
    res = ''
    while n > 0:
        k = n % b
        n //= b
        res = p[k] + res
    print(res)

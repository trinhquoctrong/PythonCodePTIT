# nguyên tố cùng nhau

def tc(a, b):
    while b > 0:
        c = b
        b = a % b
        a = c
    if a == 1:
        return True
    else:
        return False

n, k = map(int, input().split())
d = 0
for i in range(10**(k-1), 10**k):
    if tc(n, i):
        print(i, end = ' ')
        d += 1
        if d == 10:
            d = 0
            print()
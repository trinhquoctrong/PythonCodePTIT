# biến đổi về 1

n = int(input())
while n != 0:
    d = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        d += 1
    print(d)
    n = int(input())
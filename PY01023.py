# phân tích thừa số nguyên tố

def PhanTich(n):
    s = '1 '
    i = 2
    while n != 1:
        if n % i == 0:
            d = 0
            while n % i == 0:
                n /= i
                d += 1
            s = s + '* ' + str(i) + '^' + str(d) + ' '
        else:
            i += 1
    print(s)

t = int(input())
for o in range(t):
    n = int(input())
    PhanTich(n)

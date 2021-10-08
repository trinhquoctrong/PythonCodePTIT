# khoảng cách nguyên tố
import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


nx = [int(i) for i in input().split()]
arrPrime = [None] * nx[0]
arrPrime[0] = 2
k = 1
x = 3
while k < nx[0]:
    if isPrime(x):
        arrPrime[k] = x
        k += 1
    x += 2

a = [None] * (nx[0] + 1)
for i in range(0, nx[0]+1):
    if i == 0:
        a[i] = nx[1]
    else:
        a[i] = a[i-1] + arrPrime[i-1]
    print(a[i], end = ' ')
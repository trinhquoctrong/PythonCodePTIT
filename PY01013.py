# ước số chung nguyên tố
import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b > 0:
        c = b
        b = a % b
        a = c
    n = 0
    while(a != 0):
        n += a % 10
        a = int(a/10)
    if isPrime(n):
        return "YES"
    else:
        return "NO"

t = int(input())
for o in range(t):
    a = [int(i) for i in input().split()]
    print(gcd(a[0], a[1]))

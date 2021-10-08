# liệt kê số nguyên tố trong dãy
import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = [int(i) for i in input().split()]
b = {}

for i in a:
    if i not in b:
        b[i] = 0
    b[i] += 1

for i in b:
    if isPrime(i):
        print(i, b.get(i))

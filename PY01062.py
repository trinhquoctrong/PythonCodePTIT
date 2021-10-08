# ưu thế nguyên tố
import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def tc1(s):
    return isPrime(len(s))

def tc2(s):
    l = len(s)
    countPrime = 0
    for i in s:
        if isPrime(int(i)):
            countPrime += 1
    if countPrime > l - countPrime:
        return True
    else:
        return False

for t in range(int(input())):
    s = input()
    if tc1(s) and tc2(s):
        print('YES')
    else:
        print('NO')

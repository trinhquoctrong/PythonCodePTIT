# PERFECT PRIME

import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def check(n):
    if isPrime(int(n)) == False:
        return 'No'
    if isPrime(int(n[::-1])) == False:
        return 'No'
    if isPrime(sum([int(x) for x in n])) == False:
        return 'No'
    for i in n:
        if isPrime(int(i)) == False:
            return 'No'
    return 'Yes'

for test in range(int(input())):
    print(check(input()))
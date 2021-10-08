# đầu cuối nguyên tố
import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

for t in range(int(input())):
    s = input()
    dau = s[0:3]
    cuoi = s[len(s)-3:len(s)]
    if isPrime(int(dau)) and isPrime(int(cuoi)):
        print('YES')
    else:
        print('NO')
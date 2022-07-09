import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

for T in range(int(input())):
    s = input()
    n = int(s[len(s)-4:len(s)])
    if isPrime(n) == True:
        print('YES')
    else:
        print('NO')
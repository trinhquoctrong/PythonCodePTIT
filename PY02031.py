# kiểm tra nguyên tố
import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

nm = [int(j) for j in input().split()]

a = []
for i in range(nm[0]):
    x = [int(j) for j in input().split()]
    a.append(x)

for i in range(nm[0]):
    for j in range(nm[1]):
        if(isPrime(a[i][j]) == True):
            print(1, end = ' ')
        else:
            print(0, end = ' ')
    print('\n')

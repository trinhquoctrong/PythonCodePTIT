# tổng chữ số nguyên tố
import math

def nto(s):
    n = 0
    while len(s) > 0:
        n += int(s[0])
        s = s[1:len(s)]
    if n < 2:
        return "NO"
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return "NO"
    return "YES"

t = int(input())
for o in range(t):
    print(nto(input()))
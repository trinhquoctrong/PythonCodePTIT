# vị trí nguyên tố

import math

def nto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def vtNto(s):
    for i in range(len(s)):
        if nto(i) != nto(int(s[i])):
            return "NO"
    return "YES"

t = int(input())
for o in range(t):
    print(vtNto(input()))
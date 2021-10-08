# đoạn cuối nguyên tố
import math

def nto(n):
    if n < 2:
        return "NO"
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return "NO"
    return "YES"

t = int(input())
for o in range(t):
    s = input()
    l = len(s)
    s = s[l-4:l]
    print(nto(int(s)))
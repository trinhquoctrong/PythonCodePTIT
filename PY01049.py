# CHỮ SỐ NGUYÊN TỐ

import math

def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def solve(n):
    if nt(len(n)) == False:
        return 'NO'

    cnt = 0
    for i in n:
        if i == '2' or i == '3' or i == '5' or i == '7':
            cnt += 1
    if cnt <= len(n)-cnt:
        return 'NO'
    return 'YES'

for test in range(int(input())):
    print(solve(input()))
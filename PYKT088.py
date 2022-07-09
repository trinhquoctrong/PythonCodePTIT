# SỐ CÓ 9 ƯỚC SỐ

import math

d = [1] * 100000
p = []
def sang():
    d[0] = d[1] = 0
    for i in range(2, 100000):
        if d[i] == 1:
            p.append(i)
            for j in range(i*i, 100000, i):
                d[j] = 0
sang()

n = int(input())
m = math.sqrt(n)
cnt = 0
for i in range(len(p)):
    if p[i] > math.sqrt(m):
        break
    if p[i] ** 8 <= n:
        cnt += 1
    for j in range(i+1, len(p)):
        if (p[i] * p[j]) ** 2 <= n:
            cnt += 1
        else:
            break
        
print(cnt)
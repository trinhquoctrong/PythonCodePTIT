# SỐ 2 ƯU THẾ

p = []
res = []

def check(s):
    cnt = s.count('2')
    return cnt > len(s)/2

def lietke(s):
    if len(s) >= 10:
        return
    if check(s) and s not in p:
        p.append(int(s))
    lietke(s + '0')
    lietke(s + '1')
    lietke(s + '2')
    
lietke('1')
lietke('2')
p.sort()
print(p[1000])
for test in range(int(input())):
    n = int(input())
    for i in range(n):
        print(p[i], end = ' ')
    print()
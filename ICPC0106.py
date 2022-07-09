# ĐỔI CƠ SỐ - 2

p = '0123456789ABCDEF'

def chuyenDoi(s):
    s = s[::-1]
    res = 0
    for i in range(len(s)):
        res += int(s[i]) * (2 ** i)
    return p[res]

for test in range(int(input())):
    b = int(input())
    s = input()

    k = 0
    if b == 2:      k = 1
    elif b == 4:    k = 2
    elif b == 8:    k = 3
    else:           k = 4
    
    while len(s) % k != 0:
        s = '0' + s

    res = ''
    for i in range(0, len(s), k):
        res = res + chuyenDoi(s[i: i+k])
    print(res)
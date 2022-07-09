# HỆ CƠ SỐ 8

def chuyenDoi(s):
    s = s[::-1]
    res = 0
    for i in range(len(s)):
        res += int(s[i]) * (2 ** i)
    return res

s = input()
while len(s) % 3 != 0:
    s = '0' + s

res = ''
for i in range(0, len(s), 3):
    res = res + str(chuyenDoi(s[i:i+3]))

print(res)
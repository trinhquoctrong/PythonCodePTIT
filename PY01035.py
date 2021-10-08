# hệ cơ số 8

n = input()
if len(n) % 3:
    for i in range(3 - len(n)%3):
        n = '0' + n
l = len(n)
res = ''
for i in range(l-1, -1, -3):
    s = int(n[i]) + int(n[i-1]) * 2 + int(n[i-2]) * 4
    res = str(s) + res
print(res)
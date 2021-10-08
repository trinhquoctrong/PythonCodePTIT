# mã hóa 2

p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

s = input().split()
k = int(s[0])

while k != 0:
    if len(s) > 1:
        s = s[1]
        res = ''
        for i in s:
            index = p.find(i)
            res = p[(index+k)%28] + res
        print(res)
        s = input().split()
        k = int(s[0])
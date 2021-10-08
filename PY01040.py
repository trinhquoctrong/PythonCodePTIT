# mã hóa 3

p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for t in range(int(input())):
    s = input()
    s1 = list(str(i) for i in s[0 : len(s)//2])
    s2 = list(str(i) for i in s[len(s)//2 : len(s)])
    dems1 = 0
    dems2 = 0
    for i in s1:
        dems1 += p.find(i)
    for i in s2:
        dems2 += p.find(i)
    for i in range(len(s1)):
        x = p.find(s1[i])
        s1[i] = p[(x + dems1) % 26]
    for i in range(len(s2)):
        x = p.find(s2[i])
        s2[i] = p[(x + dems2) % 26]
    for i in range(len(s1)):
        x = p.find(s2[i])
        y = p.find(s1[i])
        s1[i] = p[(x + y) % 26]
        print(s1[i], end = '')
    print()

# tách đôi và tính tổng

n = input()
while len(n) != 1:
    s1 = int(n[0:len(n)//2])
    s2 = int(n[len(n)//2: len(n)])
    n = str(s1+s2)
    print(n)
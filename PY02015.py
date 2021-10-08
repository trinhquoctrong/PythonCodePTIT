# biến đổi dẫy số
a = [int(x) for x in input().split()]
while((a[0] == a[1] == a[2] == a[3] == 0)  == False):
    d = int(0)
    while((a[0] == a[1] == a[2] == a[3]) == False):
        tmp = a[0]
        a[0] = abs(a[0] - a[1])
        a[1] = abs(a[1] - a[2])
        a[2] = abs(a[2] - a[3])
        a[3] = abs(a[3] - tmp)
        d += 1
    print(d)
    a = [int(x) for x in input().split()]

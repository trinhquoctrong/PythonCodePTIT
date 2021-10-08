# làm tròn số

t = int(input())
for o in range(t):
    n = input()
    l = len(n)
    if l <= 1:
        print(n)
    else:
        a = []
        for i in range(l-1, -1, -1):
            a.append(int(n[i]))

        for i in range(l-1):
            if a[i] < 5:
                a[i] = 0
            elif a[i] <= 10:
                a[i] = 0
                a[i+1] += 1
        if a[l-1] == 10:
            a[l-1] = 0
            a.append(int(1))
        s = ''
        for i in range(len(a)-1, -1, -1):
            s = s + str(a[i])
        print(s)

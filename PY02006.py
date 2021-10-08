# dãy số phù hợp

t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    kt = True
    for i in range(n):
        if(a[i] > b[i]):
            kt = False
            break
    if(kt == True):
        print("YES")
    else:
        print("NO")

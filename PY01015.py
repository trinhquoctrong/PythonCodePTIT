# số không giảm

t = int(input())
while t>0:
    n = input()
    kt = True

    for i in range(0, len(n)-1):
        if(int(n[i]) <= int(n[i+1])):
            continue
        else:
            kt = False
            break
    if kt == True:
        print("YES")
    else:
        print("NO")
    t = t-1
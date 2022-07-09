

for test in range(int(input())):
    cnt = 0
    check = False
    n = int(input())
    while cnt <= 1000:    
        if n % 7 == 0:
            check = True
            break
        else:
            s = int(str(n)[::-1])
            n += s
            cnt += 1
    if check:
        print(n)
    else:
        print(-1)

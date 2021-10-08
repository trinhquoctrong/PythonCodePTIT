# chẵn lẻ

def check(a):
    kt = True
    for i in range(0, len(a)-1):
        if (int(a[i]) != int(a[i+1])+2) and (int(a[i]) != int(a[i+1])-2):
            kt = False
            break
    return kt



t = int(input())

while t:
    t -= 1

    n = input()
    x = 0
    for i in range(len(n)):
        x += int(n[i])
        x %= 10
    
    if x == 0 and check(n) == True:
        print("YES")
    else:
        print("NO")
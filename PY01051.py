# tổng chữ số thuận nghịch

def thuanNghich(a):
    n = 0
    while len(a) > 0:
        n += int(a[0])
        a = a[1:len(a)]
    n = str(n)    
    l = len(n)
    if l <= 1:
        return "NO"
    else:
        for i in range(int(l/2)):
            if n[i] != n[l-1-i]:
                return "NO"
    return "YES"

t = int(input())
for o in range(t):
    a = input()
    print(thuanNghich(a))

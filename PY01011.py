# số thuận nghịch chẵn

def thuanNghich(s):
    s = str(s)
    return s == s[::-1]

def numChan(s):
    s = str(s)
    for i in s:
        if int(i) % 2:
            return False
    return True

def soChuso(s):
    s = str(s)
    return len(s) % 2 == 0

t = int(input())
for o in range(t):
    n = int(input())
    for i in range(22, n):
        if thuanNghich(i) and numChan(i) and soChuso(i):
            print(i, end = ' ')
    print()
# tích chữ số

def tich(s):
    n = 1
    while len(s) > 0:
        if int(s[0]) != 0:
            n *= int(s[0])
        s = s[1:len(s)]
    return n

t = int(input())
for o in range(t):
    print(tich(input()))
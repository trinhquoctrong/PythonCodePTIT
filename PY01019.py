# xâu "thăng bằng"

def xauTB(s):
    l = len(s)
    for i in range(int(l/2)):
        if abs(ord(s[i])-ord(s[i+1])) != abs(ord(s[l-1-i])-ord(s[l-1-i-1])):
            return False
    return True

t = int(input())
for o in range(t):
    s = input()
    if xauTB(s):
        print("YES")
    else:
        print("NO")
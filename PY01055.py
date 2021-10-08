# số xen kẽ

def xenke(s):
    l = len(s)
    if l == 1:
        return "YES"
    if l % 2 == 0:
        return "NO"
    if s[0] == s[1]:
        return "NO"
    for i in range(0, l - 2, 2):
        if s[i] != s[i+2]:
            return "NO"
    return "YES"

t = int(input())
for o in range(t):
    print(xenke(input()))
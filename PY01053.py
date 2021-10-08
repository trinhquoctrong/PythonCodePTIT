# số chia hết cho 3

def chia(s):
    n = 0
    while len(s) > 0:
        n += int(s[0])
        n %= 3
        s = s[1:len(s)]
    if n == 0:
        return "YES"
    else:
        return "NO"

t = int(input())
for i in range(t):
    print(chia(input()))
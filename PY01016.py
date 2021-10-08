# giải mã

t = int(input())
while t > 0:
    s = str(input())
    n = len(s)
    result = ""
    for i in range(0, n, 2):
        result += s[i] * int(s[i+1])
    print(result)
    t = t - 1
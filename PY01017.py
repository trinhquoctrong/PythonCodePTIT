# mã hóa 1

t = int(input())
for o in range(t):
    s = input() + '#'
    res = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            res = res + str(count) + s[i-1]
            count = 1
    print(res)
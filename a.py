# từ điển

k = int(input())
if k > 10:
    print('INVALID INPUT')
else:
    d = {}
    a = []
    for i in range(k):
        s = input().split()
        if s[1].isdigit():
            a.append(int(s[1]))
    mul = 1
    for i in a:
        mul *= i
    print(sum(a), mul)

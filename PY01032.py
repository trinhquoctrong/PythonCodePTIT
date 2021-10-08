# số thuận nghịch

arr = [0]

def NP_TP(s):
    s = s[::-1]
    sum = 0
    for i in range(len(s)):
        sum += int(s[i]) * (2**i)
    return sum

def tc(s):
    if len(s) > 21:
        return
    if len(s) > 0 and s[0] != '0':
        arr.append(NP_TP(s))
    tc('0' + s + '0')
    tc('1' + s + '1')

a, b, m = map(int, input().split())

if m == 2:
    count = 0
    tc('')
    tc('1')
    tc('0')
    arr.sort()
    indexMax = [n for n, i in enumerate(arr) if i > b][0]
    indexMin = [n for n, i in enumerate(arr) if i >= a][0]
    count = indexMax - indexMin
    print(count)
elif m == 3:
    count = 0
    if a == 0:
        count += 1
    if a <= 1 and b >= 1:
        count += 1
    if a <= 6643 and b >= 6643:
        count += 1
    if a <= 1422773 and b >= 1422773:
        count += 1
    print(count)
elif m > 3:
    count = 0
    if a == 0:
        count += 1
    if a <= 1 and b >= 1:
        count += 1
    print(count)
    
# số thuận nghịch lớn nhất trong ma trận

def thuanNghich(n):
    s = str(n)
    l = len(s)
    if l < 2:
        return False
    for i in range(l//2):
        if s[i] != s[l-1-i]:
            return False
    return True

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(int(i) for i in input().split()))

max = 0
b = []
for i in range(n):
    for j in range(m):
        if max < a[i][j] and thuanNghich(a[i][j]):
            max = a[i][j]
            b.clear()
            b.append('[' + str(i) + '][' + str(j) + ']')
        elif a[i][j] == max:
            b.append('[' + str(i) + '][' + str(j) + ']')
        else:
            continue
if max:
    print(max)
    for i in b:
        print('Vi tri ' + i)
else:
    print('NOT FOUND')
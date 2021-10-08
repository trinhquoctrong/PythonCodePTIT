# tính tổng các chữ số

for t in range(int(input())):
    s = input()
    sum = 0
    a = []
    for i in s:
        if i.isdecimal():
            sum += int(i)
        else:
            a.append(i)
    a.sort()
    res = ''
    for i in a:
        res = res + i
    res = res + str(sum)
    print(res)
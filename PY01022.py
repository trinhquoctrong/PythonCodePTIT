# tổng chữ số

n = input()
if int(n) >= 0 and int(n) < 10:
    print(1)
else:
    count = 0
    while len(n) != 1:
        s = 0
        for i in n:
            s += ord(i) - ord('0')
        n = str(s)
        count += 1
    print(count)

# tính điểm trung bình

n = int(input())
a = [float(i) for i in input().split()]
d = 0
s = 0
for i in a:
    if i > min(a) and i < max(a):
        s += i
        d += 1

if d:
    s = s / d
    print('%.2f' % s)

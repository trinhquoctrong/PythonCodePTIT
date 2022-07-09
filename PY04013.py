# TÍNH TOÁN LƯỢNG MƯA

from datetime import datetime


def tinhTG(s1, s2):
    f = '%H:%M'
    return float((datetime.strptime(s2, f) - datetime.strptime(s1, f)).seconds / 3600)


map = {}
for t in range(int(input())):
    tram = input()
    tg = tinhTG(input(), input())
    luongMua = float(input())
    if tram not in map:
        map[tram] = [float(0), float(0)]
    map[tram][0] += float(tg)
    map[tram][1] += float(luongMua)
    
i = 1
for tram in map:
    print('T%02d' % i, tram, '%.2f' % (map[tram][1]/map[tram][0]))
    i += 1
    
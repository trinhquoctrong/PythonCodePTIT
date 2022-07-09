# TÌM SỐ LỚN NHẤT

p = 'abcdefghijklmnopqrstuvwxyz'

for test in range(int(input())):
    s = input()
    for i in p:
        s = s.replace(i, ' ')
    a = [int(x) for x in s.split()]
    print(max(a))
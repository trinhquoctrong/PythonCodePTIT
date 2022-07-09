# XỬ LÝ XÂU KÝ TỰ

s1 = sorted(input().lower().split())
s2 = input().lower().split()

x = sorted(list(set(s1+s2)))
print(*x)
s1 = list(set(s1))
s1.sort()
for i in s1:
    if i in s2:
        print(i, end = ' ')

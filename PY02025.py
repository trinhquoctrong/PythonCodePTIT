# tập hợp số nguyên

n = input()
A = set(int(i) for i in input().split())
B = set(int(i) for i in input().split())
a = []
b = []
c = []
for i in A:
    if i in B:
        a.append(i)
    else:
        b.append(i)

for i in B:
    if i not in A:
        c.append(i)
a.sort()
b.sort()
c.sort()
for i in a:
    print(i, end = ' ')
print()
for i in b:
    print(i, end = ' ')
print()
for i in c:
    print(i, end = ' ')

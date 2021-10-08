# tách số và sắp xếp

s = ''
for t in range(int(input())):
    s = s + ' ' + input()

for i in range(len(s)):
    if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
        s = s.replace(s[i], ' ')
a = list(int(i) for i in s.split())
a.sort()
for i in a:
    print(i)

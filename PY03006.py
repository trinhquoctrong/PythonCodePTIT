# thống kê từ khác nhau không chữa chứ số

s = ''
dict = {}
for t in range(int(input())):
    s = s + ' ' + input().lower()
for i in s:
    if (i >= 'a' and i <= 'z') == False:
        s = s.replace(i, ' ')

a = list(s.split())
a.sort()
for i in a:
    if i not in dict:
        dict[i] = 0
    dict[i] += 1

b = sorted(dict.items(), key = lambda x : x[1], reverse = True)

for i in range(len(b)):
    print(b[i][0], b[i][1])
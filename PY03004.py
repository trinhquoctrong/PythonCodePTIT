# thống kê từ khác nhau

dict = {}
s = ''
for n in range(int(input())):
    s = s + ' ' + input().lower()
for i in range(len(s)):
    if (s[i] >= 'a' and s[i] <= 'z') == False and (s[i] >= '0' and s[i] <= '9') == False:
        s = s.replace(s[i], ' ')
a = list(s.split())
a.sort()
for i in a:
    if i not in dict:
        dict[i] = 0
    dict[i] += 1

dict = sorted(dict.items(), key = lambda x:x[1], reverse = True)

for i in range(len(dict)):
    print(dict[i][0], dict[i][1])
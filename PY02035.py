# ngưỡng tối thiểu

s = input()
k = int(input())
a = []
for i in range(0, len(s) - len(s)%2, 2):
    a.append(int(s[i] + s[i+1]))
a.sort()
dict = {}
for i in a:
    if i not in dict:
        dict[i] = 0
    dict[i] += 1
check = False
for i in dict:
    if dict.get(i) >= k:
        check = True
        print(i, dict.get(i))
if check == False:
    print('NOT FOUND')